from pathlib import Path
import json
ROOT = Path(__file__).resolve().parents[1]
def save_json(relative, value):
    p = ROOT / relative
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")
    return p

from agent_lab.io import read_text, write_jsonl
def main():
    text = read_text(str(ROOT / "fixtures/mini.md"))
    records = [{"id": 1, "text": "工具\n下一行"}, {"id": 2, "text": "检索"}]
    output = ROOT / "workspace/d01/records.jsonl"
    write_jsonl(records, str(output))
    back = [json.loads(line) for line in read_text(str(output)).splitlines()]
    message = f"source_chars={len(text)}\nrecords={len(back)}\nroundtrip={back == records}\noutput={output}\n"
    log = ROOT / "reports/d01/demo.txt"
    log.parent.mkdir(parents=True, exist_ok=True)
    log.write_text(message, encoding="utf-8")
    print(message)
if __name__ == "__main__":
    main()
