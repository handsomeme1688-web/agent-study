from pathlib import Path
import json
ROOT = Path(__file__).resolve().parents[1]
def save_json(relative, value):
    p = ROOT / relative
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")
    return p

from agent_lab.retrieval import search_docs, read_chunk
def main():
    source = ROOT / "workspace/d02/chunks.jsonl"
    if not source.exists():
        raise FileNotFoundError(f"请先运行D02演示生成：{source}")
    chunks = [json.loads(line) for line in source.read_text(encoding="utf-8").splitlines() if line.strip()]
    result = {q: search_docs(chunks, q) for q in ["工具 执行", "检索", "不存在的词"]}
    if chunks: result["read_first"] = read_chunk(chunks, chunks[0]["id"])
    path = save_json("reports/d03/search.json", result); print(path)
if __name__ == "__main__":
    main()
