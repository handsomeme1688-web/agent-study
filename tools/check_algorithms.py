"""Run each algorithm's tests independently and retain real execution logs."""

import argparse
import re
import subprocess
import sys
from pathlib import Path

from algorithm_support import load_catalog, parse_day, problem_paths, safe_path, select_problems

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "repo-qa-agent"


def save(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def check_algorithms(root, project, number, problem=None, report=None):
    _, problems = select_problems(load_catalog(root), number, problem)
    directory = safe_path(project, f"reports/algorithms/a{number:02d}")
    logs, passed = [], 0
    for spec in problems:
        _, relative = problem_paths(spec)
        path = safe_path(project, relative)
        command = [sys.executable, "-m", "unittest", relative[:-3].replace("/", "."), "-v"]
        if not path.is_file():
            code = 1
            output = f"NOT_RUN: 缺少算法测试文件：{path}\n请先运行 tools/start_algorithms.py A{number:02d}。\n"
        else:
            try:
                result = subprocess.run(command, cwd=project, text=True, encoding="utf-8", errors="replace", capture_output=True, timeout=30)
                code, output = result.returncode, result.stdout + result.stderr
            except subprocess.TimeoutExpired as error:
                code = 1
                parts = [part.decode("utf-8", errors="replace") if isinstance(part, bytes) else part or "" for part in (error.stdout, error.stderr)]
                output = "".join(parts) + "\nCHECK_FAILED: 单题测试超过 30 秒，请检查死循环或复杂度。\n"
            counts = re.findall(r"Ran (\d+) tests? in", output)
            if counts and int(counts[-1]) == 0 or code == 0 and not counts:
                code = code or 1
                output += "\nCHECK_FAILED: 没有运行任何测试，请保留并完成真实断言。\n"
            elif code == 0 and re.search(rf"OK \(skipped={counts[-1]}\)", output):
                code = 1
                output += "\nCHECK_FAILED: 全部测试被跳过，不能作为验收通过。\n"
        text = f"LC {spec['id']} {spec['title']}\n$ {' '.join(command)}\n{output}\nEXIT_CODE={code}\n"
        log = directory / f"lc{int(spec['id']):04d}.txt"
        save(log, text)
        print(text)
        print(f"已保存：{log}")
        logs.append(text)
        passed += code == 0
    code = 0 if passed == len(problems) and problems else 1
    summary = f"A{number:02d}：{passed}/{len(problems)} 题本地测试通过。\nEXIT_CODE={code}\n"
    combined = "\n".join(logs) + "\n" + summary
    # A single-problem attempt must not overwrite the full day's aggregate.
    aggregate = directory / (f"summary_lc{problem:04d}.txt" if problem is not None else "summary.txt")
    save(aggregate, combined)
    if report is not None:
        save(report, combined)
        print(f"每日算法汇总：{report}")
    print(summary)
    print(f"汇总：{aggregate}")
    print("本地通过后继续提交力扣；掌握还需要独立重写和解释复杂度。")
    return code


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("day", help="算法日 A01–A30")
    parser.add_argument("--problem", type=int, help="仅检查当天某一题，填写 LeetCode 题号")
    args = parser.parse_args()
    try:
        code = check_algorithms(ROOT, PROJECT, parse_day(args.day), args.problem)
    except (ValueError, KeyError, FileNotFoundError) as error:
        parser.error(str(error))
    raise SystemExit(code)


if __name__ == "__main__":
    main()
