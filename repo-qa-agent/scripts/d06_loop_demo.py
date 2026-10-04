from pathlib import Path
import json
ROOT = Path(__file__).resolve().parents[1]
def save_json(relative, value):
    p = ROOT / relative
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")
    return p

from agent_lab.loop import run_agent
from agent_lab.tools import dispatch
from agent_lab.testing import ScriptedModel
def main():
    source = ROOT / "workspace/d02/chunks.jsonl"
    if not source.exists():
        raise FileNotFoundError(f"请先运行D02演示生成：{source}")
    chunks = [json.loads(line) for line in source.read_text(encoding="utf-8").splitlines() if line.strip()]
    model = ScriptedModel([
        {"type":"tool", "name":"search_docs", "arguments":{"query":"工具 执行", "k":3}},
        {"type":"final", "answer":"宿主程序执行工具", "citations": [chunks[0]["id"]]}
    ])
    result = run_agent("谁执行工具？", model, lambda name, args: dispatch(chunks, name, args), 4)
    result["mode"] = "mock"; result["model_seen_messages"] = model.seen
    path = save_json("reports/d06/trace.json", result)
    print(f"status={result['status']} steps={result['steps']} mode=mock"); print(path)
if __name__ == "__main__":
    main()
