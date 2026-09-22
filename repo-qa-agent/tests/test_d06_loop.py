import copy
import json
import unittest
from unittest.mock import Mock
from agent_lab.loop import run_agent

class ScriptedModel:
    def __init__(self, outputs): self.outputs=iter(outputs);self.seen=[]
    def __call__(self,messages):
        self.seen.append(copy.deepcopy(messages));value=next(self.outputs)
        if isinstance(value,Exception): raise value
        return json.dumps(value,ensure_ascii=False) if isinstance(value,dict) else value

TOOL={'type':'tool','name':'search_docs','arguments':{'query':'工具'}}
FINAL={'type':'final','answer':'宿主程序执行工具','citations':['a']}

class TestD06(unittest.TestCase):
    def test_tool_then_final_and_observation(self):
        model=ScriptedModel([TOOL,FINAL]);execute=Mock(return_value={'text':'OBS_CODE_123'})
        out=run_agent('谁执行工具？',model,execute,4)
        self.assertEqual(out['status'],'ok');self.assertEqual(out['steps'],2)
        self.assertEqual(out['answer'],'宿主程序执行工具');self.assertIsInstance(out['trace'],list)
        self.assertIn('OBS_CODE_123',json.dumps(model.seen[1],ensure_ascii=False));execute.assert_called_once()
    def test_immediate_final(self):
        execute=Mock();out=run_agent('问题',ScriptedModel([FINAL]),execute)
        self.assertEqual(out['status'],'ok');self.assertEqual(out['steps'],1);execute.assert_not_called()
    def test_limit(self):
        model=ScriptedModel([TOOL]*8);execute=Mock(return_value=[])
        out=run_agent('问题',model,execute,2)
        self.assertEqual(out['status'],'step_limit');self.assertEqual(len(model.seen),2)
        self.assertEqual(execute.call_count,2)
    def test_bad_decision_blocks_tool(self):
        execute=Mock();out=run_agent('问题',ScriptedModel(['not-json']),execute)
        self.assertEqual(out['status'],'bad_decision');execute.assert_not_called()
    def test_model_timeout(self):
        out=run_agent('问题',ScriptedModel([TimeoutError('timeout')]),Mock())
        self.assertEqual(out['status'],'timeout');self.assertEqual(out['steps'],1)
    def test_tool_error(self):
        out=run_agent('问题',ScriptedModel([TOOL]),Mock(side_effect=KeyError('unknown')))
        self.assertEqual(out['status'],'tool_error')
    def test_run_isolation(self):
        run_agent('RUN_A_SECRET',ScriptedModel([FINAL]),Mock())
        model=ScriptedModel([FINAL]);run_agent('RUN_B',model,Mock())
        self.assertNotIn('RUN_A_SECRET',json.dumps(model.seen,ensure_ascii=False))
    def test_invalid_input(self):
        for q,n in [('',4),('  ',4),('q',0),('q',True)]:
            with self.subTest(q=q,n=n),self.assertRaises(ValueError): run_agent(q,Mock(),Mock(),n)
