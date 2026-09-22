# Hello-Agents 30天任务书 · 路径与行号版

版本：2026-09-19 / v2。沿用上一版30学习日的项目和验收标准；这次补齐精确阅读范围、所有作业路径、创建顺序、入口命令和输出位置。**这不是重新开一门课，也不要求你每天建立一个新项目。**

## 0. 先把文件放到唯一位置

把压缩包中的整个 **agent-study** 文件夹解压到你的用户主目录，不要解压成两层 `agent-study/agent-study`。

本书唯一缩写是 `~`：表示“当前用户主目录”，不是要求你创建名为波浪号的文件夹。

|用途|本书的完整路径|是否改动|
|---|---|---|
|本说明|`~/agent-study/START_HERE.md`|只读|
|全部30天任务书|`~/agent-study/handbook/30_days.md`|只读，日记另写|
|第1天单独任务卡|`~/agent-study/handbook/days/day01.md`|只读；后续为day02.md到day30.md|
|教程材料目录|`~/agent-study/materials/hello-agents/`|只读；运行获取脚本后出现指定原文件|
|离线补课讲义|`~/agent-study/materials/notes/`|已提供；每张日卡指定具体文件及行号|
|你自己的项目根目录|`~/agent-study/repo-qa-agent/`|所有业务代码都在这里|
|准备当日文件的工具|`~/agent-study/tools/start_day.py`|已提供，不需要你编写|
|显示今日指定阅读的工具|`~/agent-study/tools/read_today.py`|已提供，不需要你编写|
|获取固定教材的工具|`~/agent-study/tools/fetch_materials.py`|已提供，只获取文本，不安装教程依赖|
|运行并保存测试的工具|`~/agent-study/tools/check_day.py`|已提供，不代替真实集成或人工评分|
|D28干净复现辅助工具|`~/agent-study/tools/reproduce.py`|已提供，不复制旧环境和结果|
|完整文件清单|`~/agent-study/handbook/file_index.md`|按文件逐项列首次创建日及用途|

Windows中的同一个位置为 `C:\Users\你的用户名\agent-study\`；例如代码文件为 `C:\Users\你的用户名\agent-study\repo-qa-agent\agent_lab\io.py`。macOS通常为 `/Users/你的用户名/agent-study/`，Linux通常为 `/home/你的用户名/agent-study/`。**这不是对你电脑用户名的判断，以终端打印的主目录为准。**

已有旧作业先备份，只迁移你自己完成的业务函数；不要用新骨架覆盖旧成果。教材不改，项目不与教程同名，不在教程目录执行整本教材的依赖安装。

## 1. 第一次操作：只建立一个环境

推荐沿用可用的Python 3.11/3.12环境；已有兼容3.13也可先运行标准库练习。不因为路径版强制更换系统Python。

### macOS / Linux：在终端逐行执行

```bash
python3 -m venv "$HOME/agent-study/repo-qa-agent/.venv"
source "$HOME/agent-study/repo-qa-agent/.venv/bin/activate"
python -c "from pathlib import Path; import sys; print(Path.home()); print(sys.executable)"
cd "$HOME/agent-study/repo-qa-agent"
```

### Windows：在PowerShell逐行执行

```powershell
py -3 -m venv "$HOME/agent-study/repo-qa-agent/.venv"
function python { & "$HOME/agent-study/repo-qa-agent/.venv/Scripts/python.exe" @args }
python -c "from pathlib import Path; import sys; print(Path.home()); print(sys.executable)"
cd "$HOME/agent-study/repo-qa-agent"
```

PowerShell这里的临时函数只为当前终端把 `python` 指向同一虚拟环境，不修改系统执行策略。新终端重新执行该函数；macOS/Linux新终端重新执行activate。后面的 `python` 一律指这个环境。命令中的 `$HOME` 由Bash/PowerShell自动展开，不要复制成Python代码里的字面量。

文件扩展名必须是真正的 `.py/.md/.jsonl`，不是隐藏扩展名后的 `.py.txt`。编辑器打开整个 `~/agent-study/repo-qa-agent/` 文件夹，而不是只打开一个孤立文件。所有 `python -m scripts.xxx` 都从这个项目根目录执行。

## 2. “哪几页”改为不漂移的定位

本轮主教材是仓库内的Markdown和Python源文件，不是一个已指定版本的PDF。**它们没有固定的书页页码；我不填写不存在的“第几页”。** 统一给：固定提交 + 完整文件路径 + 原文件起止行号 + 小节/函数用途。

固定提交：`b4aca1af44b7a492b4bfdec5aa100d556c65db54`。以下数字是原始文件行号，空行也计数，不是网页解析工具的行号。两端均包含。不要切换到不断变化的main分支后继续按旧行号找。

例如第6天打开 `~/agent-study/materials/hello-agents/code/chapter4/ReAct.py`，阅读L25–L74；自己的实现写到 `~/agent-study/repo-qa-agent/agent_lab/loop.py`。在线链接也带固定提交和 `#L25-L74`，可以直接跳到范围。编辑器切换到源码视图、显示行号；用“转到行”跳到起点，再读到终点，不继续整章通读。

教材原文件**没有预先打包**；本包已提供补课讲义、作业骨架和工具。首次可一次获取10个指定文本文件，或每天仅获取当天需要的原文：

```bash
python "$HOME/agent-study/tools/fetch_materials.py"
# 或仅获取第6天涉及的教材文件：
python "$HOME/agent-study/tools/fetch_materials.py" --day 6
```

获取脚本固定提交，已知Git blob摘要的文件还会校验摘要，不下载全仓库图片或安装教材环境。网络不可达时，打开日卡的固定在线链接；也可以把自己已有的同版本源码交给脚本复制：

```bash
# 将下一行替换成你真实已有的仓库位置，不是要求创建这条示例路径：
python "$HOME/agent-study/tools/fetch_materials.py" --from-repo "/你的已有仓库/hello-agents"
```

复制后不符固定摘要会报错，不会悄悄接受错版。获取脚本在本次环境无法完成外网下载实测；目录/版本/失败处理逻辑已离线检查。源文件内容与指定窗口通过GitHub读取核对；只有实际成功获取后才存在本机原文文件。获取记录写 `~/agent-study/materials/source_download_audit.json`。

读取工具只显示当天指定范围，同时输出：`~/agent-study/handbook/readings/day01.txt` 和 `~/agent-study/handbook/readings/day01.html`（第2天为day02，以此类推）。教材缺失会明确显示MISSING及获取命令，不生成伪造教材。

## 3. 每天只做这一条操作链

```bash
# 第1天；后续把1替换成2、3……30
python "$HOME/agent-study/tools/start_day.py" 1
python "$HOME/agent-study/tools/read_today.py" 1
# 打开 ~/agent-study/handbook/days/day01.html，按文件表写代码
# 完成以后执行当天运行区命令，再做检查：
python "$HOME/agent-study/tools/check_day.py" 1
```

`~/agent-study/tools/start_day.py`自动建当天目录和骨架；已存在的文件显示KEEP，**绝不覆盖你已经写的文件**。文件表中的“新建”是当天首次创建，不是以后每天删掉重建；“修改”必须沿用前一天的同一文件；“程序生成”只预建父目录，不伪造成功结果。

D1–D6的6个业务模块、38个固定测试方法与小样例已提供，函数仍待你完成。后来新增的业务模块和主项目测试多数是待实现骨架，首次失败是预期。后期测试中的 `TODO_STUDENT_TEST` 必须替换为真实测试逻辑，不能删除后声称已通过。算法每天给一个最小样例，但链表/树的空输入测试远远不够，你还需按日卡补正常输入和边界。

每天都有代码路径、测试路径、结果路径、复盘路径与求职记录路径。技术细节写在“实现步骤与契约”；**命令以新日卡运行区为准**，不再使用上一版零散的相对路径。

## 4. 怎么判断完成

离线测试通过 + 自加边界 + 能解释/独立修改 + 结果保存，才算当日工程任务完成。真实API、Embedding、MCP、Docker、CI、模型质量分别留证；不因一栏测试成功就代替其他栏。

每天6小时为建议预算，未过就继续同一学习日。D7/D15/D23/D28是验收修复；D25为选修，主线有红灯就运行 `python "$HOME/agent-study/tools/start_day.py" 25 --skip-optional` 并记录后置。不要把“完成所有框架名字”当学习目标。

运行时第三方库会在 `.venv`、`workspace/qdrant`、缓存目录生成自己的内部文件；这些文件名由库管理，不要求你手工创建。**本书逐一规定的是所有需要你创建/修改/提交的项目文件、教材文件和验收产物，不是把第三方库的安装文件逐个抄进计划。**


从 `~/agent-study/handbook/index.html` 打开30天目录。
