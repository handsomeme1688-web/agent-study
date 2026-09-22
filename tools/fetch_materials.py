"""Download only the pinned text sources; never install tutorial dependencies."""
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.parse import quote
import argparse, hashlib, json, shutil, sys
ROOT=Path(__file__).resolve().parents[1]
def blob_sha(data):return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()
def main():
    p=argparse.ArgumentParser();p.add_argument("--day",type=int,choices=range(1,31));p.add_argument("--from-repo",type=Path);args=p.parse_args()
    m=json.loads((ROOT/"handbook/manifest.json").read_text(encoding="utf-8"));revision=m["source_revision"]
    sources=m["sources"]
    if args.day:
        keys={r["source"] for r in m["days"][str(args.day)]["readings"] if r["source"]}
        sources={k:v for k,v in sources.items() if k in keys}
    results=[];failed=False
    for key,item in sources.items():
        rel=item["path"];dest=ROOT/"materials/hello-agents"/rel
        url=f"https://raw.githubusercontent.com/datawhalechina/hello-agents/{revision}/"+quote(rel,safe="/")
        try:
            if dest.exists(): data=dest.read_bytes()
            elif args.from_repo:data=(args.from_repo.expanduser()/rel).read_bytes()
            else:
                with urlopen(Request(url,headers={"User-Agent":"HelloAgentsStudyPathGuide/2.0"}),timeout=30) as response:data=response.read()
            expected=item.get("git_blob_sha1")
            if expected and blob_sha(data)!=expected:raise ValueError("源码与固定版本不符；不要更改行号，将该文件移走后从固定提交重新获取")
            data.decode("utf-8")
            if not dest.exists():dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
            results.append({"path":str(dest),"source_url":url,"revision":revision,"git_blob_sha1":blob_sha(data),"sha256":hashlib.sha256(data).hexdigest(),"lines":len(data.decode("utf-8").splitlines()),"status":"verified" if expected else "pinned_url_saved"})
            print(f"OK {dest}")
        except Exception as exc:
            failed=True;results.append({"path":str(dest),"status":"failed","error":str(exc),"url":url});print(f"FAILED {dest}: {exc}\n原始文件地址：{url}")
    audit=ROOT/"materials/source_download_audit.json";audit.parent.mkdir(parents=True,exist_ok=True);audit.write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding="utf-8")
    print(f"获取记录：{audit}\n网络失败时可在浏览器打开日卡固定GitHub链接；不需要重装Python。")
    sys.exit(1 if failed else 0)
if __name__=="__main__":main()
