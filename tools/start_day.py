"""Create exactly today's files, without overwriting completed work."""
from pathlib import Path
import argparse, json, shutil, sys
ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "repo-qa-agent"
def main():
    p=argparse.ArgumentParser(); p.add_argument("day",type=int,choices=range(1,31));p.add_argument("--skip-optional",action="store_true")
    args=p.parse_args()
    if args.skip_optional and args.day != 25: p.error("--skip-optional仅用于D25")
    m=json.loads((ROOT/"handbook/manifest.json").read_text(encoding="utf-8"));d=m["days"][str(args.day)]
    print(f"D{args.day:02d}: {d['title']}\n项目根目录：{PROJECT}")
    for path,description in d["new"]:
        if args.skip_optional and (path.startswith("agent_lab/") or path.startswith("tests/")): continue
        target=(PROJECT/path).resolve()
        if not target.is_relative_to(PROJECT.resolve()):raise ValueError("非法输出路径")
        if target.exists():print(f"KEEP   {target}");continue
        source=ROOT/m["files"][path]["template"]
        target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source,target);print(f"CREATE {target}")
    for path,description in d["edit"]:
        target=PROJECT/path
        if not target.exists():
            if path=="tests/test_d25_graph.py": print(f"OPTIONAL_NOT_CREATED {target}")
            else: print(f"PREREQUISITE_MISSING {target} —— 先补前面的学习日")
        else: print(f"EDIT   {target}")
    for path,description in d["out"]:
        target=PROJECT/path
        if path.endswith("/"):target.mkdir(parents=True,exist_ok=True)
        else:target.parent.mkdir(parents=True,exist_ok=True)
        print(f"OUTPUT {target} —— 只建目录，不伪造结果")
    print(f"\n打开当天任务卡：{ROOT/f'handbook/days/day{args.day:02d}.html'}")
    print("教材文件只读；业务骨架与后期测试尚未实现。")
if __name__=="__main__":main()
