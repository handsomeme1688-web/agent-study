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

    obj = json.loads(text)
    
    if not isinstance(obj,dict):
        raise ValueError("校验失败")
    kind = obj.get("type")
    if kind != "tool" and kind != "final":
        raise ValueError("只接受'tool'和 'final'")
    if kind == "tool":
        keys = set(obj.keys())
        if keys != {"type","name","arguments"}:
            raise ValueError("校验失败")
        if obj.get("name") not in ["search_docs","read_chunk"]:
            raise ValueError("校验失败")
        arguments = obj["arguments"]
        if not isinstance(arguments,dict):
            raise ValueError("校验失败")
        
        if obj.get("name") == "search_docs":
            query = arguments.get("query")
            if not set(arguments.keys()).issubset({"query","k"}) or type(query) is not str or query.strip()=="":
                raise ValueError("校验失败")
            if arguments.get("k") == None:
                arguments["k"] = 3
            elif type(arguments.get("k")) is not int  or not 1<=arguments["k"]<=5:
                raise ValueError("校验失败") 
        if obj.get("name") == "read_chunk":
            chunk_id = arguments.get("chunk_id")
            if set(arguments.keys()) != {"chunk_id"} or type(chunk_id) is not str or chunk_id.strip() == "":
                raise ValueError("校验失败") 
        return obj
    if kind =="final":
        keys = set(obj.keys())
        if not keys.issubset({"type", "answer", "citations"}) or not {"type", "answer"}.issubset(keys):
            raise ValueError("校验失败")
        answer = obj.get("answer")
        if answer is None or answer.strip() == "":
            raise ValueError("校验失败")
        citations = obj.get("citations")
        if citations == None:
            citations =[]
            obj["citations"]=citations
        if type(citations) != list or not all(isinstance(item,str) for item in citations):
            raise ValueError("校验失败")
        return obj
        
        
        




# 必须再校验一遍 name 和 arguments——不能因为"调用方是模型"就信任输入。
# 注意 dispatch 是公开函数，parse_decision 之外也可能有人直接调它
def dispatch(chunks: list[dict], name: str, arguments: dict) -> dict | list:
    """D5：再次校验名称/参数，合法后调用 D3 函数；非法输入不执行工具。"""
    if not name in {"search_docs", "read_chunk"} :
        raise ValueError("校验失败")
    if type(arguments)!=dict:
        raise ValueError("校验失败")
    if name == "search_docs":
        keys = set(arguments.keys())
        if not keys.issubset({"query","k"}):
            raise ValueError("校验失败")
        query = arguments.get("query")
        if type(query)!=str or query.strip()== "":
            raise ValueError("校验失败")
        k = arguments.get("k")
        if k is None:
            k=3
        elif type(k) is not int or not 1<=k<=5:
            raise ValueError("校验失败")
        return search_docs(chunks,query,k)
    else:
        keys=set(arguments.keys())
        if keys!={"chunk_id"}:
            raise ValueError("校验失败")
        chunk_id = arguments["chunk_id"]
        if type(chunk_id) != str or chunk_id.strip()=="":
            raise ValueError("校验失败")
        return read_chunk(chunks,chunk_id)
        
