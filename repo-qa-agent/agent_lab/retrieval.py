import copy


def search_docs(chunks: list[dict], query: str, k: int = 3) -> list[dict]:
    """D3：query 按空白拆词，casefold，去重。
    score = 出现在 chunk['text'].casefold() 中的不同查询词数量。
    仅保留 score>0；按 (-score, id) 排序，返回前 k 个副本并加 score。
    空 query 返回 []；k 必须是非 bool 的整数且 1<=k<=5，否则 ValueError。
    不得修改 chunks。中文没有自动分词，需要输入空格分隔的关键词。
    """
    if type(k)!=int or type(k)==bool or k < 1 or k > 5:
        raise ValueError("k 必须是非 bool 的整数且 1<=k<=5")
    if not query.strip():
        return []
    search_results = []
    query_keys = [query_key for query_key in set(query.casefold().split())]

    query_scores = []
    '''
    "外层查询词、内层 chunk"，累加出来的是某个词出现在多少个 chunk 里——这是词的文档频率，不是 chunk 的分数。
    讲义 L11：score 属于 chunk，每个 chunk 的分数 = 它正文里出现了多少个不同的查询词。所以外层该是 chunk、内层是词。
    '''
    for chunk in chunks:
        score = 0
        for query_key in query_keys:
            if query_key in chunk['text'].casefold():
                score += 1
        if score > 0 :
            query_scores.append((-score,chunk['id']))
    results = sorted(query_scores)

    for result in results[:k]:
        for chunk in chunks:
            if chunk.get('id') == result[1]:
                chunk_tmp = copy.copy(chunk) 
                chunk_tmp["score"]=-result[0]
        search_results.append(chunk_tmp)
    return search_results


def read_chunk(chunks: list[dict], chunk_id: str) -> dict:
    """D3：仅按已登记 id 读片段；不存在抛 KeyError；不接受任意文件路径。"""
    for chunk in chunks:
        if chunk['id'] == chunk_id:
            return chunk
    raise KeyError("id 不存在！")
