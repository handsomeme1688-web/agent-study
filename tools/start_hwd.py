#!/usr/bin/env python3
"""Create one day's offline HWD learning skeleton; never overwrite user work."""
from __future__ import annotations

import argparse
from pathlib import Path
import shlex
from textwrap import dedent

DEFAULT_ROOT = Path(__file__).resolve().parents[1] / "labs" / "hwd_project"


def source(body: str) -> str:
    return dedent(body).lstrip()


DAYS = {
    1: {
        "src/contracts.py": '''
            """H1：会话初始契约。只使用合成字段，不连接 HWD。"""
            def new_draft(session_id):
                """返回 session_id, fields={}, revision=0, confirmed_revision=None,
                phase='collecting_min'；空 session_id 抛 ValueError。"""
                raise NotImplementedError("请实现 new_draft")

            def validate_message(text):
                """只接受去掉首尾空白后非空的 str；返回清理后的文本。"""
                raise NotImplementedError("请实现 validate_message")
        ''',
        "tests/test_day01.py": '''
            import unittest
            from src.contracts import new_draft, validate_message

            class ContractTests(unittest.TestCase):
                def test_new_draft(self):
                    self.assertEqual(new_draft('DEMO-S1'), dict(session_id='DEMO-S1', fields={}, revision=0, confirmed_revision=None, phase='collecting_min'))
                def test_independent_sessions(self):
                    a, b = new_draft('A'), new_draft('B')
                    a['fields']['quantity'] = 100
                    self.assertEqual(b['fields'], {})
                def test_valid_message(self):
                    self.assertEqual(validate_message('  合成货源  '), '合成货源')
                def test_invalid_input(self):
                    for value in ['', '  ', None, 123]:
                        with self.subTest(value=value), self.assertRaises(ValueError):
                            validate_message(value)
                    with self.assertRaises(ValueError):
                        new_draft('')
        ''',
    },
    2: {
        "src/extraction.py": '''
            """H2：结构化输出边界；本练习不调用真实 LLM。"""
            ALLOWED_FIELDS = {'customer', 'cargo_name', 'quantity', 'from_port', 'to_port'}

            def parse_model_reply(raw):
                """支持纯 JSON / 外层 ```json 围栏。格式为 {'patch': {...}}。
                成功：{'patch': 白名单字段, 'error': None}。
                非法 JSON、patch 非对象、quantity 非正数/为 bool：
                {'patch': {}, 'error': 'INVALID_MODEL_OUTPUT'}。"""
                raise NotImplementedError("请实现 parse_model_reply")
        ''',
        "tests/test_day02.py": '''
            import unittest
            from src.extraction import parse_model_reply

            class ExtractionTests(unittest.TestCase):
                def test_plain_json(self):
                    self.assertEqual(parse_model_reply('{"patch":{"quantity":1000}}'), {'patch': {'quantity': 1000}, 'error': None})
                def test_fence_and_whitelist(self):
                    raw = '```json\\n{"patch":{"cargo_name":"合成煤炭","admin":true}}\\n```'
                    self.assertEqual(parse_model_reply(raw), {'patch': {'cargo_name': '合成煤炭'}, 'error': None})
                def test_invalid_shapes(self):
                    for raw in ['oops', '{}', '[]', '{"patch":[]}', '{"patch":null}']:
                        with self.subTest(raw=raw):
                            self.assertEqual(parse_model_reply(raw), {'patch': {}, 'error': 'INVALID_MODEL_OUTPUT'})
                def test_invalid_quantity(self):
                    for value in ['-1', '0', 'true', '"很多"']:
                        with self.subTest(value=value):
                            self.assertEqual(parse_model_reply('{"patch":{"quantity":' + value + '}}')['error'], 'INVALID_MODEL_OUTPUT')
        ''',
    },
    3: {
        "src/memory.py": '''
            """H3：多轮增量更新与确认失效。"""
            def apply_patch(draft, patch):
                """不修改入参；仅更新五个允许字段，忽略 None/空白字符串/未知键。
                有实际字段变化时 revision + 1、confirmed_revision=None、phase='collecting_min'。
                无实际变化则保持所有值。返回独立的深拷贝。"""
                raise NotImplementedError("请实现 apply_patch")
        ''',
        "tests/test_day03.py": '''
            import unittest
            from src.memory import apply_patch

            def draft():
                return dict(session_id='DEMO-S1', fields={'quantity':100, 'cargo_name':'煤'}, revision=2, confirmed_revision=2, phase='ready_submit')

            class MemoryTests(unittest.TestCase):
                def test_revision_and_confirmation(self):
                    result = apply_patch(draft(), {'quantity':200})
                    self.assertEqual((result['revision'],result['confirmed_revision'],result['phase']), (3,None,'collecting_min'))
                    self.assertEqual(result['fields']['cargo_name'], '煤')
                def test_ignores_empty_and_unknown(self):
                    self.assertEqual(apply_patch(draft(), {'quantity':None,'cargo_name':'  ','admin':True}), draft())
                def test_unchanged_patch_does_not_increment(self):
                    self.assertEqual(apply_patch(draft(), {'quantity':100}), draft())
                def test_no_mutation_or_aliasing(self):
                    original = draft()
                    result = apply_patch(original, {'quantity':200})
                    result['fields']['cargo_name']='changed'
                    self.assertEqual(original, draft())
        ''',
    },
    4: {
        "src/catalog.py": '''
            """H4：名称到业务 ID 的消歧；catalog 是合成目录列表。"""
            def resolve_name(name, catalog):
                """去除名称首尾空白后精确匹配 name 或 aliases。
                按 id 排序、按 id 去重；返回 {'status': exact|ambiguous|not_found,
                'candidates': [{'id': ..., 'name': ...}, ...]}。不猜测不存在的 ID。"""
                raise NotImplementedError("请实现 resolve_name")
        ''',
        "tests/test_day04.py": '''
            import unittest
            from src.catalog import resolve_name

            CATALOG=[{'id':'P2','name':'示例北港二号','aliases':['北港']}, {'id':'P1','name':'示例北港一号','aliases':['北港']}, {'id':'P3','name':'示例南港','aliases':['南港']}]

            class CatalogTests(unittest.TestCase):
                def test_exact(self):
                    self.assertEqual(resolve_name(' 南港 ',CATALOG), {'status':'exact','candidates':[{'id':'P3','name':'示例南港'}]})
                def test_ambiguous(self):
                    result=resolve_name('北港', CATALOG)
                    self.assertEqual(result['status'],'ambiguous')
                    self.assertEqual([x['id'] for x in result['candidates']], ['P1','P2'])
                def test_no_hallucinated_id(self):
                    self.assertEqual(resolve_name('火星港', CATALOG), {'status':'not_found','candidates':[]})
                def test_deduplicates_id(self):
                    result=resolve_name('南港', CATALOG+[CATALOG[2]])
                    self.assertEqual(len(result['candidates']),1)
                    self.assertEqual(result['status'],'exact')
        ''',
    },
    5: {
        "src/workflow.py": '''
            """H5：教学版状态机，只保留货源录入的最小闭环。"""
            REQUIRED = ['customer', 'cargo_name', 'quantity', 'from_port', 'to_port']
            ARCHIVES = ['customer', 'cargo_name', 'from_port', 'to_port']

            def evaluate_draft(fields, resolutions, confirmed=False):
                """依次：缺必填=>collecting_min；目录缺失/非exact=>awaiting_disambiguation；
                未确认=>awaiting_confirm；已确认=>ready_submit。
                返回 {'phase':阶段, 'missing_fields':按 REQUIRED 顺序排列的缺字段}。
                quantity 必须是非 bool 的正数；字符串仅空白也算缺失。"""
                raise NotImplementedError("请实现 evaluate_draft")
        ''',
        "tests/test_day05.py": '''
            import unittest
            from src.workflow import evaluate_draft

            FIELDS=dict(customer='示例客户',cargo_name='煤',quantity=100,from_port='北港',to_port='南港')
            RES={key:{'status':'exact','candidates':[{'id':'DEMO-'+key,'name':key}]} for key in ['customer','cargo_name','from_port','to_port']}

            class WorkflowTests(unittest.TestCase):
                def test_missing(self):
                    self.assertEqual(evaluate_draft({'quantity':0},{},True), {'phase':'collecting_min','missing_fields':['customer','cargo_name','quantity','from_port','to_port']})
                def test_ambiguous_before_confirmation(self):
                    resolution=dict(RES,from_port={'status':'ambiguous','candidates':[]})
                    self.assertEqual(evaluate_draft(FIELDS,resolution,True)['phase'],'awaiting_disambiguation')
                def test_must_confirm(self):
                    self.assertEqual(evaluate_draft(FIELDS,RES)['phase'],'awaiting_confirm')
                def test_ready(self):
                    self.assertEqual(evaluate_draft(FIELDS,RES,True), {'phase':'ready_submit','missing_fields':[]})
        ''',
    },
    6: {
        "src/submit.py": '''
            """H6：离线 Mock LIS 提交与幂等；gateway 由调用方注入。"""
            def submit_draft(draft, request_id, gateway, receipts):
                """仅 phase=ready_submit 且 confirmed_revision=revision 可提交，否则 ValueError。
                gateway(fields) -> {'goods_id': 'DEMO-G001'}。
                receipts 是请求缓存：相同 request_id+相同字段/版本仅调用一次 gateway；
                相同 request_id+不同字段/版本抛 ValueError。gateway 异常传播，不缓存失败。
                不修改 draft；返回 gateway 结果。"""
                raise NotImplementedError("请实现 submit_draft")
        ''',
        "tests/test_day06.py": '''
            import unittest
            from unittest.mock import Mock
            from src.submit import submit_draft

            def draft():
                return dict(fields={'quantity':100}, revision=1, confirmed_revision=1, phase='ready_submit')

            class SubmitTests(unittest.TestCase):
                def test_duplicate_only_writes_once(self):
                    gateway=Mock(return_value={'goods_id':'DEMO-G001'})
                    receipts={}
                    first=submit_draft(draft(),'R1',gateway,receipts)
                    second=submit_draft(draft(),'R1',gateway,receipts)
                    self.assertEqual(first,second)
                    self.assertEqual(first['goods_id'],'DEMO-G001')
                    self.assertEqual(gateway.call_count,1)
                def test_stale_confirmation(self):
                    gateway=Mock()
                    with self.assertRaises(ValueError):
                        submit_draft(dict(draft(),revision=2),'R2',gateway,{})
                    gateway.assert_not_called()
                def test_not_ready(self):
                    gateway=Mock()
                    with self.assertRaises(ValueError):
                        submit_draft(dict(draft(),phase='awaiting_confirm'),'R3',gateway,{})
                    gateway.assert_not_called()
                def test_request_id_conflict(self):
                    gateway=Mock(return_value={'goods_id':'DEMO-G001'})
                    receipts={}
                    submit_draft(draft(),'R1',gateway,receipts)
                    with self.assertRaises(ValueError):
                        submit_draft(dict(draft(),fields={'quantity':200}),'R1',gateway,receipts)
                    self.assertEqual(gateway.call_count,1)
                def test_failure_is_not_cached(self):
                    gateway=Mock(side_effect=[TimeoutError('mock'),{'goods_id':'DEMO-G001'}])
                    receipts={}
                    with self.assertRaises(TimeoutError):
                        submit_draft(draft(),'R1',gateway,receipts)
                    self.assertEqual(submit_draft(draft(),'R1',gateway,receipts)['goods_id'],'DEMO-G001')
                    self.assertEqual(gateway.call_count,2)
        ''',
    },
    7: {
        "src/stream.py": '''
            """H7：可测试的 SSE 编码边界。"""
            def build_events(session_id, trace_id, payloads):
                """payloads=[(event_name, payload_dict), ...]。返回 SSE 字符串列表。
                每项 data: {JSON}\\n\\n；JSON 含 event,sessionId,streamTraceId,seq(从1递增)。
                payload 不能覆盖这四个保留字段；保留中文。"""
                raise NotImplementedError("请实现 build_events")
        ''',
        "src/api.py": '''
            """H7：纯 Python 请求适配层；不启动服务器。"""
            def dispatch_message(body, run_turn):
                """body 需含非空 str 类型 session_id 和 message，否则返回 {'status':400,'events':[]}。
                run_turn(session_id, message.strip()) 返回 (event,payload) 列表；
                用 build_events(..., body.get('trace_id','DEMO-TRACE'), ...) 编码，返回 status=200。
                下游 TimeoutError 返回 status=504、events=[]；其他异常不吞掉。"""
                raise NotImplementedError("请实现 dispatch_message")
        ''',
        "tests/test_day07.py": '''
            import json
            import unittest
            from unittest.mock import Mock
            from src.stream import build_events
            from src.api import dispatch_message

            def decode(item):
                if not item.startswith('data: ') or not item.endswith('\\n\\n'):
                    raise AssertionError('SSE frame missing delimiter')
                return json.loads(item[6:-2])

            class StreamTests(unittest.TestCase):
                def test_frames(self):
                    frames=build_events('S1','T1',[('start',{}),('delta',{'text':'中文'}),('done',{})])
                    self.assertEqual([decode(x)['seq'] for x in frames],[1,2,3])
                    self.assertEqual(decode(frames[-1])['event'],'done')
                    self.assertEqual(decode(frames[1])['text'],'中文')
                def test_reserved_keys(self):
                    result=decode(build_events('S1','T1',[('done',{'seq':100,'sessionId':'evil','event':'wrong','streamTraceId':'wrong'})])[0])
                    self.assertEqual(result,dict(seq=1,sessionId='S1',event='done',streamTraceId='T1'))
                def test_dispatch(self):
                    runner=Mock(return_value=[('done',{'phase':'awaiting_confirm'})])
                    result=dispatch_message({'session_id':'S1','message':'  货源  '},runner)
                    runner.assert_called_once_with('S1','货源')
                    self.assertEqual(result['status'],200)
                    self.assertEqual(decode(result['events'][0])['phase'],'awaiting_confirm')
                def test_invalid_request(self):
                    runner=Mock()
                    self.assertEqual(dispatch_message({'message':'x'},runner),{'status':400,'events':[]})
                    runner.assert_not_called()
                def test_timeout(self):
                    self.assertEqual(dispatch_message({'session_id':'S1','message':'x'},Mock(side_effect=TimeoutError())), {'status':504,'events':[]})
        ''',
    },
    8: {
        "src/checkpoint.py": '''
            """H8：只保存本地合成会话状态，使用 JSON，不使用 pickle。"""
            def save_checkpoint(path, state):
                """写入 {'schema_version':1,'state':state}，临时文件写完后原子替换目标。
                创建所需父目录。不修改 state。"""
                raise NotImplementedError("请实现 save_checkpoint")

            def load_checkpoint(path):
                """不存在返回 None；合法版本返回 state；损坏/未知版本/非dict state 抛 ValueError。"""
                raise NotImplementedError("请实现 load_checkpoint")
        ''',
        "tests/test_day08.py": '''
            import json
            from pathlib import Path
            import tempfile
            import unittest
            from src.checkpoint import save_checkpoint,load_checkpoint

            class CheckpointTests(unittest.TestCase):
                def test_roundtrip_and_replace(self):
                    with tempfile.TemporaryDirectory() as tmp:
                        path=Path(tmp)/'nested'/'state.json'
                        one={'session_id':'S1','fields':{'quantity':100},'revision':1,'confirmed_revision':None,'phase':'awaiting_confirm'}
                        save_checkpoint(path,one)
                        self.assertEqual(load_checkpoint(path),one)
                        two=dict(one,revision=2,confirmed_revision=2,phase='ready_submit')
                        save_checkpoint(path,two)
                        self.assertEqual(load_checkpoint(path),two)
                        self.assertEqual(json.loads(path.read_text())['schema_version'],1)
                def test_missing(self):
                    with tempfile.TemporaryDirectory() as tmp:
                        self.assertIsNone(load_checkpoint(Path(tmp)/'missing.json'))
                def test_corrupt(self):
                    with tempfile.TemporaryDirectory() as tmp:
                        path=Path(tmp)/'state.json'
                        path.write_text('{broken',encoding='utf-8')
                        with self.assertRaises(ValueError): load_checkpoint(path)
                def test_unknown_version(self):
                    with tempfile.TemporaryDirectory() as tmp:
                        path=Path(tmp)/'state.json'
                        path.write_text('{"schema_version":99,"state":{}}',encoding='utf-8')
                        with self.assertRaises(ValueError): load_checkpoint(path)
        ''',
    },
    9: {
        "src/evaluation.py": '''
            """H9：离线评测指标。这些指标不代表生产或真实 LLM 效果。"""
            def summarize(records):
                """records 含 parse_ok,expected_patch,predicted_patch,submitted,allowed_submit,latency_ms。
                返回 total,parse_success_rate,field_accuracy,unsafe_submit_count,p95_latency_ms。
                field_accuracy=所有 expected_patch 键的准确值数/预期键总数；多余预测键不计分。
                p95 使用 nearest-rank，即排序后第 ceil(.95*n) 项；空集所有指标为0。"""
                raise NotImplementedError("请实现 summarize")
        ''',
        "tests/test_day09.py": '''
            import unittest
            from src.evaluation import summarize

            class EvaluationTests(unittest.TestCase):
                def test_metrics(self):
                    rows=[
                        dict(parse_ok=True,expected_patch={'a':1,'b':2},predicted_patch={'a':1,'b':2},submitted=True,allowed_submit=True,latency_ms=10),
                        dict(parse_ok=False,expected_patch={'a':2,'b':3},predicted_patch={'a':2},submitted=True,allowed_submit=False,latency_ms=30),
                    ]
                    self.assertEqual(summarize(rows),dict(total=2,parse_success_rate=.5,field_accuracy=.75,unsafe_submit_count=1,p95_latency_ms=30))
                def test_empty(self):
                    self.assertEqual(summarize([]),dict(total=0,parse_success_rate=0,field_accuracy=0,unsafe_submit_count=0,p95_latency_ms=0))
                def test_p95(self):
                    rows=[dict(parse_ok=True,expected_patch={},predicted_patch={},submitted=False,allowed_submit=False,latency_ms=i) for i in range(1,21)]
                    self.assertEqual(summarize(rows)['p95_latency_ms'],19)
                def test_extra_prediction_not_extra_credit(self):
                    row=dict(parse_ok=True,expected_patch={'a':1},predicted_patch={'a':1,'other':'x'},submitted=False,allowed_submit=False,latency_ms=1)
                    self.assertEqual(summarize([row])['field_accuracy'],1)
        ''',
    },
    10: {
        "src/demo.py": '''
            """H10：组合 H1—H9 的真实实现，全部使用合成数据/Mock gateway。"""
            import json

            def run_scenario(name):
                """name: happy_path / ambiguous / revised_after_confirm / duplicate_submit。
                结果仅含 phase, gateway_calls, goods_id, blocked_reason。
                happy_path 与 duplicate_submit: submitted,1,'DEMO-G001',None。
                ambiguous: awaiting_disambiguation,0,None,'AMBIGUOUS_ARCHIVE'。
                revised_after_confirm: awaiting_confirm,0,None,'STALE_CONFIRMATION'。
                必须串联前9天模块；不得按 name 直接硬编码结果。"""
                raise NotImplementedError("请实现 run_scenario")

            if __name__ == '__main__':
                for scenario in ['happy_path','ambiguous','revised_after_confirm','duplicate_submit']:
                    print(json.dumps({'scenario':scenario,**run_scenario(scenario)},ensure_ascii=False))
        ''',
        "tests/test_day10.py": '''
            import unittest
            from src.demo import run_scenario

            class EndToEndTests(unittest.TestCase):
                def test_happy_path(self):
                    self.assertEqual(run_scenario('happy_path'),dict(phase='submitted',gateway_calls=1,goods_id='DEMO-G001',blocked_reason=None))
                def test_ambiguous(self):
                    self.assertEqual(run_scenario('ambiguous'),dict(phase='awaiting_disambiguation',gateway_calls=0,goods_id=None,blocked_reason='AMBIGUOUS_ARCHIVE'))
                def test_revised_after_confirm(self):
                    self.assertEqual(run_scenario('revised_after_confirm'),dict(phase='awaiting_confirm',gateway_calls=0,goods_id=None,blocked_reason='STALE_CONFIRMATION'))
                def test_duplicate_submit(self):
                    self.assertEqual(run_scenario('duplicate_submit'),dict(phase='submitted',gateway_calls=1,goods_id='DEMO-G001',blocked_reason=None))
        ''',
    },
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('day', type=int, choices=range(1, 11))
    parser.add_argument('--root', type=Path, default=DEFAULT_ROOT)
    args = parser.parse_args()
    root = args.root.expanduser().resolve()
    hwd = Path('/home/handsomeme/PythonProjects/hwd').resolve()
    if root == hwd or hwd in root.parents:
        parser.error('学习骨架不能写入原 hwd 项目；请使用独立实验目录。')
    files = {'src/__init__.py': '', 'tests/__init__.py': '', **DAYS[args.day]}
    for relative, body in files.items():
        target = root / relative
        resolved_target = target.resolve()
        if root not in resolved_target.parents:
            parser.error(f'目标路径通过符号链接离开实验目录，停止写入：{target}')
        target.parent.mkdir(parents=True, exist_ok=True)
        try:
            with target.open('x', encoding='utf-8') as handle:
                handle.write(source(body))
        except FileExistsError:
            print(f'保留已有文件：{target}')
        else:
            print(f'新建：{target}')
    for relative in DAYS[args.day]:
        if relative.startswith('src/'):
            print(f'现在编写：{root / relative}')
    print(f'验收用例：{root / f"tests/test_day{args.day:02d}.py"}')
    print('然后执行：')
    print(f'cd {shlex.quote(str(root))}')
    print(f'python3 -m unittest tests.test_day{args.day:02d} -v')
    print('首次运行出现 NotImplementedError 是预期；完成实现后应全部 OK。')


if __name__ == '__main__':
    main()
