from pathlib import Path
import json
ROOT = Path(__file__).resolve().parents[1]
def save_json(relative, value):
    p = ROOT / relative
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")
    return p

from agent_lab.io import read_text, write_jsonl
from agent_lab.chunking import split_markdown
def main():
    text = read_text(str(ROOT / "fixtures/mini.md"))
    chunks = split_markdown(text, "fixtures/mini.md")
    write_jsonl(chunks, str(ROOT / "workspace/d02/chunks.jsonl"))
    result = "\n".join(f"{c['id']} | {c['title']} | {c['start_line']}-{c['end_line']}" for c in chunks)
    p = ROOT / "reports/d02/chunks.txt"; p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(result, encoding="utf-8"); print(result)
if __name__ == "__main__":
    main()
