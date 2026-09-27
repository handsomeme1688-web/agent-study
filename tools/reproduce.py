"""D28: safely copy only project sources and test in a separately created environment."""
from pathlib import Path
import argparse, json, os, shutil, subprocess, sys, venv
ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "repo-qa-agent"
TARGET = ROOT / "reproduce/repo-qa-agent"
REPORT = SOURCE / "reports/d28/clean_setup.txt"
IGNORED = {".venv", "workspace", ".git", "__pycache__", ".pytest_cache", ".env", "reports", "*.pyc"}

def prepare():
    if TARGET.exists():
        raise SystemExit(f"目标已存在，未覆盖：{TARGET}。保留旧复现证据，先自行备份或移走该目录再重试。")
    shutil.copytree(SOURCE, TARGET, ignore=shutil.ignore_patterns(*IGNORED))
    (TARGET / "workspace").mkdir()
    (TARGET / "reports").mkdir()
    files = [str(p.relative_to(TARGET)) for p in sorted(TARGET.rglob("*")) if p.is_file()]
    manifest = TARGET.parent / "copy_manifest.json"
    manifest.write_text(json.dumps({"source": str(SOURCE), "target": str(TARGET), "files": files,
                                    "excluded": sorted(IGNORED)}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"复制完成：{TARGET}\n清单：{manifest}\n没有复制密钥、虚拟环境、workspace和历史报告。")

def check():
    if not TARGET.exists():
        raise SystemExit("请先运行 reproduce.py prepare。")
    lock = TARGET / "requirements.lock.txt"
    lock_text = lock.read_text(encoding="utf-8") if lock.is_file() else ""
    requirements = [line for line in lock_text.splitlines() if line.strip() and not line.lstrip().startswith("#")]
    if not requirements or "NOT_DONE" in lock_text:
        raise SystemExit(f"请先完成真实依赖锁文件：{lock}；空文件、仅注释或占位文件不能用于复现。")
    env = TARGET / ".venv"
    if not env.exists():
        venv.EnvBuilder(with_pip=True).create(env)
    executable = env / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    commands = [[str(executable), "-m", "pip", "install", "-r", str(lock)],
                [str(executable), "-m", "unittest", "discover", "-s", "tests", "-v"]]
    logs = [f"CWD={TARGET}\nPYTHON={executable}\n"]
    code = 0
    for command in commands:
        print("RUN", " ".join(command), flush=True)
        result = subprocess.run(command, cwd=TARGET, capture_output=True, text=True,
                                encoding="utf-8", errors="replace")
        block = "$ " + " ".join(command) + "\n" + result.stdout + result.stderr + f"\nEXIT_CODE={result.returncode}\n"
        logs.append(block)
        print(block)
        if result.returncode:
            code = result.returncode
            break
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(logs), encoding="utf-8")
    print(f"结果：{REPORT}。只覆盖独立环境与离线测试，真实索引和模型需另验收。")
    raise SystemExit(code)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["prepare", "check"])
    args = parser.parse_args()
    prepare() if args.action == "prepare" else check()
