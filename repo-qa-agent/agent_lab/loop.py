import json
from collections.abc import Callable
from .tools import parse_decision

def run_agent(question: str, model: Callable, execute: Callable,
              max_steps: int = 4) -> dict:
    """D6：model(messages)->教学协议JSON字符串；execute(name, arguments)->结果。
    每次调用创建新的 messages；必须至少含当前 user 问题。
    每步一次 model 调用；tool 结果追加到 messages 后才可进入下一步。
    教学协议可把动作作为assistant消息、工具结果作为带标签的user消息回填。
    原生工具协议在 D8 单独适配，不能伪造缺少 tool_call_id 的 tool 消息。
    final -> status='ok'；耗尽 -> 'step_limit'；模型或工具 TimeoutError -> 'timeout'；
    解析失败 -> 'bad_decision'；工具 KeyError/ValueError -> 'tool_error'。
    上述错误立即返回，不重试。输入空白问题或非法 max_steps 抛 ValueError。
    返回至少含 status, answer, steps, trace。steps=已实际发起的model调用数。
    trace 为列表，保存动作/结果或错误摘要，不要求记录模型内部推理。
    """
    raise NotImplementedError("D6: 实现 run_agent")
