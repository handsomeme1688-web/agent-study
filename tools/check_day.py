"""Run available tests up to a day and retain real stdout/stderr, including failures."""
from pathlib import Path
import argparse, json, re, subprocess, sys
ROOT=Path(__file__).resolve().parents[1]; PROJECT=ROOT/"repo-qa-agent"
def run_log(command,path):
    result=subprocess.run(command,cwd=PROJECT,text=True,encoding="utf-8",errors="replace",capture_output=True)
    text="$ "+" ".join(command)+"\n"+result.stdout+result.stderr+f"\nEXIT_CODE={result.returncode}\n"
    path.parent.mkdir(parents=True,exist_ok=True);path.write_text(text,encoding="utf-8");print(text);print(f"已保存：{path}")
    return result.returncode

def main():
    p=argparse.ArgumentParser();p.add_argument("day",type=int,choices=range(1,31));p.add_argument("--only-current",action="store_true");args=p.parse_args()
    meta=json.loads((ROOT/"handbook/manifest.json").read_text(encoding="utf-8"));day=meta["days"][str(args.day)]
    modules=[]
    for path in sorted((PROJECT/"tests").glob("test_d*.py")):
        match=re.match(r"test_d(\d+)",path.name)
        if match and (int(match[1])==args.day if args.only_current else int(match[1])<=args.day):modules.append("tests."+path.stem)
    out=PROJECT/f"reports/d{args.day:02d}"
    main_code=run_log([sys.executable,"-m","unittest",*modules,"-v"],out/"unittest.txt") if modules else 0
    algorithm=PROJECT/day["algorithm"]["test"]
    if algorithm.exists():
        module=day["algorithm"]["test"][:-3].replace("/",".")
        algo_code=run_log([sys.executable,"-m","unittest",module,"-v"],out/"algorithm.txt")
    else:
        algo_code=1;out.mkdir(parents=True,exist_ok=True);(out/"algorithm.txt").write_text(f"NOT_RUN: 缺少{algorithm}\n",encoding="utf-8")
        print("请先执行start_day.py创建当天算法练习。")
    print("本命令只检查离线测试；真实模型/人工核证/协议/容器/简历验收仍按任务卡完成。")
    sys.exit(1 if main_code or algo_code else 0)
if __name__=="__main__":main()
