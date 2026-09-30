"""D05：合法调用和坏参数演示。

逐行解析夹具里的 4 条决策，tool 才 dispatch，final 直接记回答；
每行单独捕获 ValueError，把结果或错误类型写进输出 JSONL。
"""
from pathlib import Path
import argparse
import json

from agent_lab.io import write_jsonl
from agent_lab.tools import dispatch, parse_decision

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def load_chunks():
    source = PROJECT_ROOT / "workspace/d02/chunks.jsonl"
    if not source.exists():
        raise FileNotFoundError(f"请先运行D02演示生成：{source}")
    return [json.loads(line) for line in source.read_text(encoding="utf-8").splitlines() if line.strip()]


def main():
    parser = argparse.ArgumentParser(description="解析并分发教学 JSON 决策")
    parser.add_argument("--out", default=str(PROJECT_ROOT / "reports/d05/dispatch.jsonl"))
    args = parser.parse_args()

    out_path = Path(args.out)
    if not out_path.is_absolute():
        out_path = PROJECT_ROOT / out_path

    chunks = load_chunks()
    decisions_path = PROJECT_ROOT / "fixtures/d05_decisions.jsonl"
    lines = [line for line in decisions_path.read_text(encoding="utf-8").splitlines() if line.strip()]

    records = []
    for lineno, line in enumerate(lines, start=1):
        try:
            decision = parse_decision(line)
        except ValueError as e:
            records.append({"line": lineno, "ok": False, "error": type(e).__name__})
            continue

        if decision["type"] == "tool":
            try:
                result = dispatch(chunks, decision["name"], decision["arguments"])
            except ValueError as e:
                records.append({"line": lineno, "ok": False, "error": type(e).__name__})
                continue
            records.append({"line": lineno, "ok": True, "type": "tool",
                            "name": decision["name"], "result": result})
        else:
            records.append({"line": lineno, "ok": True, "type": "final",
                            "answer": decision["answer"]})

    write_jsonl(records, str(out_path))
    for record in records:
        print(f"第{record['line']}行：{'正常' if record['ok'] else record['error']}")
    print(f"输出：{out_path}")


if __name__ == "__main__":
    main()
