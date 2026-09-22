"""课程提供的离线模型替身；不代表任何真实模型能力。"""
import copy
import json
class ScriptedModel:
    def __init__(self, outputs):
        self.outputs = iter(outputs)
        self.seen = []
    def __call__(self, messages):
        self.seen.append(copy.deepcopy(messages))
        value = next(self.outputs)
        if isinstance(value, Exception):
            raise value
        return json.dumps(value, ensure_ascii=False) if isinstance(value, dict) else value
