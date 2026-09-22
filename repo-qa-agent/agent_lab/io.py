from pathlib import Path
import json

def read_text(path: str) -> str:
    """D1：UTF-8 读取全文；空文件返回空串；坏路径保留 FileNotFoundError。"""
    raise NotImplementedError("D1: 实现 read_text")

def write_jsonl(records: list[dict], path: str) -> None:
    """D1：创建父目录，覆盖写；一行一个 JSON 对象，中文不转义。"""
    raise NotImplementedError("D1: 实现 write_jsonl")
