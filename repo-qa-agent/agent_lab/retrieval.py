def search_docs(chunks: list[dict], query: str, k: int = 3) -> list[dict]:
    """D3：query 按空白拆词，casefold，去重。
    score = 出现在 chunk['text'].casefold() 中的不同查询词数量。
    仅保留 score>0；按 (-score, id) 排序，返回前 k 个副本并加 score。
    空 query 返回 []；k 必须是非 bool 的整数且 1<=k<=5，否则 ValueError。
    不得修改 chunks。中文没有自动分词，需要输入空格分隔的关键词。
    """
    raise NotImplementedError("D3: 实现 search_docs")

def read_chunk(chunks: list[dict], chunk_id: str) -> dict:
    """D3：仅按已登记 id 读片段；不存在抛 KeyError；不接受任意文件路径。"""
    raise NotImplementedError("D3: 实现 read_chunk")
