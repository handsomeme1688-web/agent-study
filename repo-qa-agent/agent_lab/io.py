from pathlib import Path
import json

def read_text(path: str) -> str:
    """D1：UTF-8 读取全文；空文件返回空串；坏路径保留 FileNotFoundError。"""
    with open(path,'r',encoding='utf-8') as f:
        text = f.read()
    return text

def write_jsonl(records: list[dict], path: str) -> None:
    """D1：创建父目录，覆盖写；一行一个 JSON 对象，中文不转义。"""
    prt_path = Path(path)
    prt_path.parent.mkdir(parents=True, exist_ok=True)
    with open(prt_path, 'w', encoding='utf-8') as f:
        for record in records:
            json.dump(record,f,ensure_ascii=False)
            f.write('\n')
    # raise NotImplementedError("D1: 实现 write_jsonl")
