"""Print exact source line windows and write a local numbered reading page."""
from pathlib import Path
from urllib.parse import quote
import argparse, html, json
ROOT=Path(__file__).resolve().parents[1]
def main():
    p=argparse.ArgumentParser();p.add_argument("day",type=int,choices=range(1,31));args=p.parse_args()
    m=json.loads((ROOT/"handbook/manifest.json").read_text(encoding="utf-8"));d=m["days"][str(args.day)]
    text=[];blocks=[]
    for r in d["readings"]:
        path=ROOT/r["path"];start=r["start"];end=r["end"]
        header=f"{r['title']}\n文件：{path}\n原文件行号：L{start}–L{end}（两端包含）"
        text.append(header)
        if not path.exists():
            message=f"MISSING：请先运行 python \"{ROOT/'tools/fetch_materials.py'}\" --day {args.day:02d}"
            if r["source"]:
                rel=m["sources"][r["source"]]["path"]
                url=f"https://github.com/datawhalechina/hello-agents/blob/{m['source_revision']}/"+quote(rel,safe="/")+f"#L{start}-L{end}"
                message+="\n在线精确范围："+url
            text.append(message);blocks.append("<h2>"+html.escape(header)+"</h2><p>"+html.escape(message)+"</p>");continue
        lines=path.read_text(encoding="utf-8").splitlines()
        if end>len(lines):raise ValueError(f"范围越界：{path}只有{len(lines)}行；请确认固定版本")
        numbered=[f"{i:>5} | {lines[i-1]}" for i in range(start,end+1)]
        text.extend(numbered);text.append("")
        rows=''.join(f'<div class="line"><b>{i}</b><span>{html.escape(lines[i-1])}</span></div>' for i in range(start,end+1))
        blocks.append('<h2>'+html.escape(header)+'</h2>'+rows)
    output=ROOT/f"handbook/readings/day{args.day:02d}.txt";output.parent.mkdir(parents=True,exist_ok=True);output.write_text("\n".join(text),encoding="utf-8")
    page='<!doctype html><html lang="zh"><meta charset="utf-8"><title>今日指定阅读</title><style>body{font:16px/1.7 system-ui;max-width:1100px;margin:40px auto;padding:0 24px}h2{font-size:18px;white-space:pre-wrap;overflow-wrap:anywhere}.line{display:flex;gap:14px;border-bottom:1px solid #eee}.line b{min-width:4em;text-align:right;color:#697586}.line span{white-space:pre-wrap;overflow-wrap:anywhere;font-family:monospace}</style><h1>D%02d 指定阅读</h1><p>数字是原文件行号，不是PDF页码；教材和补课讲义已经分栏标明。</p>'%args.day+''.join(blocks)+'</html>'
    output.with_suffix('.html').write_text(page,encoding="utf-8")
    print("\n".join(text));print(f"\n阅读页：{output.with_suffix('.html')}")
if __name__=="__main__":main()
