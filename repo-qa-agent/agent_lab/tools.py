import json
from .retrieval import search_docs, read_chunk

def parse_decision(text: str) -> dict:
    """D5：json.loads 解析教学 JSON 协议，校验失败统一 ValueError。
    tool: {'type':'tool','name':..., 'arguments':{...}}
      search_docs: query 是非空字符串，k 默认3、严格整数1..5；只允许query/k。
      read_chunk: chunk_id 是非空字符串；只允许chunk_id。
      tool 顶层只允许 type/name/arguments，名称必须在上述白名单。
    final: {'type':'final','answer':非空字符串,'citations':字符串列表(缺省[])}
      final 顶层只允许 type/answer/citations。
    拒绝列表、未知 type、额外字段；不得 eval/exec。
    返回补好缺省字段的字典。此协议不是供应商原生 Function Calling。
    """
    raise NotImplementedError("D5: 实现 parse_decision")

def dispatch(chunks: list[dict], name: str, arguments: dict) -> dict | list:
    """D5：再次校验名称/参数，合法后调用 D3 函数；非法输入不执行工具。"""
    raise NotImplementedError("D5: 实现 dispatch")
