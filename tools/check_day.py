"""Run offline project/algorithm tests and retain their actual stdout/stderr."""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "repo-qa-agent"
OPTIONAL_TEST = "tests/test_d25_graph.py"


def save_log(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print(text)
    print(f"已保存：{path}")


def run_log(command, path):
    result = subprocess.run(
        command, cwd=PROJECT, text=True, encoding="utf-8", errors="replace", capture_output=True
    )
    output = result.stdout + result.stderr
    code = result.returncode
    # unittest reports success for an empty module; it is not a completed exercise.
    counts = re.findall(r"Ran (\d+) tests? in", output)
    if counts and int(counts[-1]) == 0 or code == 0 and not counts:
        code = code or 1
        output += "\nCHECK_FAILED: 没有运行任何测试，请保留并完成真实断言。\n"
    elif code == 0 and re.search(rf"OK \(skipped={counts[-1]}\)", output):
        code = 1
        output += "\nCHECK_FAILED: 全部测试被跳过，不能作为验收通过。\n"
    text = "$ " + " ".join(command) + "\n" + output + f"\nEXIT_CODE={code}\n"
    save_log(path, text)
    return code


def test_day(path):
    match = re.match(r"test_d(\d+)", Path(path).name)
    return int(match[1]) if match else None


def project_modules(manifest, day_number, only_current):
    required = {
        path for path in manifest.get("base_tests", [])
        if test_day(path) is not None and test_day(path) <= day_number
    }
    for number, day in manifest["days"].items():
        if int(number) <= day_number:
            for path, _ in day["new"] + day["edit"]:
                if path.startswith("tests/") and path.endswith(".py") and test_day(path) is not None:
                    required.add(path)
    available = {
        str(path.relative_to(PROJECT))
        for path in (PROJECT / "tests").glob("test_d*.py")
        if test_day(path) is not None and test_day(path) <= day_number
    }
    if OPTIONAL_TEST in required and not (PROJECT / OPTIONAL_TEST).exists() and not (PROJECT / "agent_lab/graph_agent.py").exists():
        required.remove(OPTIONAL_TEST)
        print("D25选修代码和测试均未创建：跳过LangGraph选修验收，继续检查已学习的业务。")
    if only_current:
        current = {path for path in required | available if test_day(path) == day_number}
        if current:
            required = {path for path in required if test_day(path) == day_number}
            available = {path for path in available if test_day(path) == day_number}
        else:
            print(f"D{day_number:02d}没有当日离线业务测试，改跑截至今天的累计业务测试。")
    missing = sorted(required - available)
    modules = [path[:-3].replace("/", ".") for path in sorted(available)]
    return modules, missing


def check_project(manifest, args, report):
    modules, missing = project_modules(manifest, args.day, args.only_current)
    if missing:
        text = "NOT_RUN: 缺少计划要求的业务测试文件：\n"
        text += "\n".join(str(PROJECT / path) for path in missing)
        text += "\n请先为对应学习日运行 start_day.py；已有文件不会被覆盖。\n"
        if set(missing) & set(manifest.get("base_tests", [])):
            text += "基础固定测试须从项目原始版本恢复，start_day.py 不会重新生成这些文件。\n"
        text += "EXIT_CODE=1\n"
        save_log(report, text)
        return 1
    if not modules:
        save_log(report, "NOT_RUN: 没有可运行的业务测试，不能判定通过。先创建对应学习日的文件。\nEXIT_CODE=1\n")
        return 1
    return run_log([sys.executable, "-m", "unittest", *modules, "-v"], report)


def check_algorithm(day, report):
    path = day["algorithm"]["test"]
    if not (PROJECT / path).is_file():
        save_log(report, f"NOT_RUN: 缺少算法测试文件：{PROJECT / path}\n请先执行 start_day.py 创建当天练习。\nEXIT_CODE=1\n")
        return 1
    module = path[:-3].replace("/", ".")
    return run_log([sys.executable, "-m", "unittest", module, "-v"], report)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("day", type=int, choices=range(1, 31))
    parser.add_argument("--only-current", action="store_true", help="只跑当日业务测试；无当日测试时回退累计业务测试")
    scope = parser.add_mutually_exclusive_group()
    scope.add_argument("--project-only", action="store_true", help="仅验收业务代码，暂不运行算法测试")
    scope.add_argument("--algorithm-only", action="store_true", help="仅验收当日算法")
    args = parser.parse_args()
    manifest = json.loads((ROOT / "handbook/manifest.json").read_text(encoding="utf-8"))
    day = manifest["days"][str(args.day)]
    out = PROJECT / f"reports/d{args.day:02d}"
    codes = []
    if not args.algorithm_only:
        codes.append(check_project(manifest, args, out / "unittest.txt"))
    if not args.project_only:
        if args.day >= 3 and (ROOT / "handbook/algorithms_110.json").is_file():
            from check_algorithms import check_algorithms
            codes.append(check_algorithms(ROOT, PROJECT, args.day - 2, report=out / "algorithm.txt"))
        else:
            codes.append(check_algorithm(day, out / "algorithm.txt"))
    print("本命令只检查离线测试；真实模型/人工核证/协议/容器/简历验收仍按任务卡完成。")
    raise SystemExit(1 if any(codes) else 0)


if __name__ == "__main__":
    main()
