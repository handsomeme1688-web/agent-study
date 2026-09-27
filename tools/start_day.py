"""Create today's files without overwriting work, then show the next action."""

import argparse
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "repo-qa-agent"


def project_path(relative):
    target = (PROJECT / relative).resolve()
    if not target.is_relative_to(PROJECT.resolve()):
        raise ValueError(f"非法输出路径：{relative}")
    return target


def next_action(day, day_number, skip_optional=False):
    """The sequential cards add guidance; the manifest remains sufficient."""
    if not skip_optional:
        metadata_path = ROOT / "handbook/sequential.json"
        if metadata_path.is_file():
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
            guidance = metadata.get("days", {}).get(str(day_number), {})
            if guidance.get("first_file") and guidance.get("first_task"):
                path = guidance["first_file"]
                if path.startswith("repo-qa-agent/"):
                    path = path[len("repo-qa-agent/"):]
                return path, guidance["first_task"]
        candidates = day["edit"] + day["new"]
        for path, description in candidates:
            if path.startswith("agent_lab/"):
                return path, description
        for path, description in day["new"] + day["edit"]:
            if not path.startswith(("algorithms/", "algorithm_tests/", "notes/", "career/d")):
                return path, description
    return day["algorithm"]["code"], "完成当日算法；D25选修业务代码已跳过。"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("day", type=int, choices=range(1, 31))
    parser.add_argument("--skip-optional", action="store_true")
    args = parser.parse_args()
    if args.skip_optional and args.day != 25:
        parser.error("--skip-optional仅用于D25")
    manifest = json.loads((ROOT / "handbook/manifest.json").read_text(encoding="utf-8"))
    day = manifest["days"][str(args.day)]
    new_algorithms = args.day >= 3 and (ROOT / "handbook/algorithms_110.json").is_file()
    print(f"D{args.day:02d}: {day['title']}\n项目根目录：{PROJECT}")
    for path, description in day["new"]:
        if new_algorithms and path.startswith(("algorithms/", "algorithm_tests/")):
            continue
        if args.skip_optional and path.startswith(("agent_lab/", "tests/")):
            continue
        target = project_path(path)
        if target.exists():
            print(f"KEEP   {target}")
            continue
        source = ROOT / manifest["files"][path]["template"]
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        print(f"CREATE {target}")
    for path, description in day["edit"]:
        if new_algorithms and path.startswith(("algorithms/", "algorithm_tests/")):
            continue
        target = project_path(path)
        if not target.exists():
            if path == "tests/test_d25_graph.py":
                print(f"OPTIONAL_NOT_CREATED {target}")
            else:
                print(f"PREREQUISITE_MISSING {target} —— 先补前面的学习日")
        else:
            print(f"EDIT   {target}")
    for path, description in day["out"]:
        target = project_path(path)
        if path.endswith("/"):
            target.mkdir(parents=True, exist_ok=True)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
        print(f"OUTPUT {target} —— 只建目录，不伪造结果")

    first_file, first_task = next_action(day, args.day, args.skip_optional)
    if new_algorithms and args.skip_optional:
        from algorithm_support import load_catalog, problem_paths, select_problems
        _, problems = select_problems(load_catalog(ROOT), args.day - 2)
        first_file = problem_paths(problems[0])[0]
        first_task = "按今日算法卡依次完成 3–4 题；D25选修业务代码已跳过。"
    print(f"\n下一步打开：{project_path(first_file)}\n在这个文件中：{first_task}")
    print(f"按顺序执行今日任务卡：{ROOT / f'handbook/顺序版/day{args.day:02d}.md'}")
    print(f"先完成业务代码并测试：{sys.executable} {ROOT / 'tools/check_day.py'} {args.day} --project-only")
    if new_algorithms:
        from algorithm_support import scaffold
        scaffold(ROOT, PROJECT, args.day - 2)
    else:
        print(f"业务测试通过后，再练算法：{project_path(day['algorithm']['code'])}")
    print(f"算法写完后测试：{sys.executable} {ROOT / 'tools/check_day.py'} {args.day} --algorithm-only")
    print("预期测试显示 Ran N tests、OK，且 EXIT_CODE=0；真实模型、演示和人工验收按今日任务卡继续完成。")
    if new_algorithms:
        print(f"现在下一步：打开 {project_path(first_file)}；{first_task}")
        print("按今日任务卡先完成业务，之后按上面的算法文件顺序逐题练习。")


if __name__ == "__main__":
    main()
