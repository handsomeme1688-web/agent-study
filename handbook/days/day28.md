# D28｜干净环境复现

**唯一项目根目录：** `~/agent-study/repo-qa-agent/`。今日任务卡：`~/agent-study/handbook/days/day28.md`。

## 1. 今天具体看哪个文件、读到哪里

|顺序|完整路径与准确范围|只抓住什么|
|---|---|---|
|1|`~/agent-study/materials/hello-agents/LICENSE.txt`<br>**L1–L1**<br>[打开固定版本相同行范围](https://github.com/datawhalechina/hello-agents/blob/b4aca1af44b7a492b4bfdec5aa100d556c65db54/LICENSE.txt#L1-L1)|识别固定版本许可证名称；发布前再读完整许可|
|2|`~/agent-study/materials/notes/28_reproduce.md`<br>**L1–L22**<br>本包已提供；本次补课讲义，不是教材原文。|D28 验收：从说明书重建（本次补课讲义）|

**学到这里停：** 能说出今天目标函数接什么输入、返回什么、至少一个错误分支；接着按下表写代码。源码中的图像不需要下载，未指定内容本日不读。

## 2. 先准备文件，再动手

```bash
cd "$HOME/agent-study/repo-qa-agent"
python "$HOME/agent-study/tools/start_day.py" 28
python "$HOME/agent-study/tools/read_today.py" 28
```

自动生成的阅读页：`~/agent-study/handbook/readings/day28.html`；对应带行号文本：`~/agent-study/handbook/readings/day28.txt`。

## 3. 今天所有文件的完整路径

|动作|完整路径|你在这里做什么|
|---|---|---|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/docs/architecture.md`|请求链路及实际模块路径|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/docs/attribution.md`|教材版本、复用部分、个人改动与许可说明|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/reports/d28/reproduce.md`|不看旧终端历史的重建过程|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/algorithms/d28_two_sum_cli.py`|算法独立实现；闭卷日新文件不覆盖旧答案|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/algorithm_tests/test_d28_two_sum_cli.py`|已给最小样例，你另补2个有效边界|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/notes/d28.md`|今日复盘、算法用时、错误与下一步|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/career/d28_action.md`|今日求职动作与真实证据|
|修改既有文件|`~/agent-study/repo-qa-agent/README.md`|补完全部可复制启动步骤和边界|
|修改既有文件|`~/agent-study/repo-qa-agent/career/applications.md`|仅记录真实岗位资格、申请和反馈|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d28/demo.mp4`|3分钟真实演示，故障注入标mock|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d28/clean_setup.txt`|干净venv的安装与测试输出|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d28/unittest.txt`|check_day.py自动保存主项目测试输出|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d28/algorithm.txt`|check_day.py自动保存算法测试输出|

**“新建一次”已由准备工具完成时，你只需要打开并填内容；不要删掉重建。报告初始状态NOT_DONE不是成绩。程序生成项没有实际运行结果前不要填写成功。**

## 4. 要写的接口、具体操作和停止标准

```text
干净复现位置为 ~/agent-study/reproduce/repo-qa-agent；不得复用旧workspace或.venv冒充重建。
```

**今天不加新技术。** 先不要看旧终端历史，新建干净工作目录，严格按README从第一条命令做起。能请同学执行更好；无人协助也做一次干净环境复现，并如实注明是自己执行。

**README必须回答：** 解决什么问题；限定语料是什么；与Hello-Agents关系；真实实现和未实现功能；Python/依赖/模型要求；如何配置但不暴露密钥；离线与真实运行如何区分；启动、测试、导入、评测命令；引用规则；权限边界；已知失败与报告链接。

录制3分钟演示：约30秒说明范围，60秒带引用问答与原文定位，30秒无答案处理，30秒一次可控错误，30秒展示测试/报告。超时/限步演示可以使用标明mock的故障注入，不伪装成真实模型失败统计。

**验收：** 干净环境中离线检查通过；条件具备时真实问答也通过；5类演示能找到对应证据。所复用代码按原仓库当前LICENSE及说明保留来源和适用要求，不将教程框架当作个人原创。尚未检查许可证的部分先补查再公开，不能凭印象填写许可类型。

**交什么：** README定稿、架构图、3分钟视频、`~/agent-study/repo-qa-agent/reports/d28/reproduce.md`、来源/个人改动表。D24/D25未完成时只列“后续计划”。

**口述：** 别人拿到你仓库，需要几步看到第一个结果？最容易失败的一步怎么诊断？

**没过：** 删掉不影响主线的框架/界面，先修文档遗漏、依赖或配置。所有阻塞启动的错误优先于新增特色功能。

**求职：** 用新的干净环境实际打开简历中每个链接；投递材料与仓库版本同步。

### 本版锁定的固定输入 / 预期

代码来源、模型配置、语料、依赖、测试、导入、启动、评测全部可按README定位；未实现项公开列出。

### 独立复现的所有位置

|用途|完整路径|
|---|---|
|隔离的第二份项目根|`~/agent-study/reproduce/repo-qa-agent/`|
|复制清单|`~/agent-study/reproduce/copy_manifest.json`|
|新的虚拟环境|`~/agent-study/reproduce/repo-qa-agent/.venv/`|
|新依赖清单|`~/agent-study/reproduce/repo-qa-agent/requirements.lock.txt`|
|新语料文件|`~/agent-study/reproduce/repo-qa-agent/data/chunks.jsonl`|
|新向量索引|`~/agent-study/reproduce/repo-qa-agent/workspace/qdrant/`|
|本次安装与测试的实际日志|`~/agent-study/repo-qa-agent/reports/d28/clean_setup.txt`|

准备工具复制主项目的相同相对路径，但排除旧环境、密钥、workspace、Git目录和报告。重复准备时拒绝覆盖。这里是唯一允许的第二项目目录，只用于验证原项目，不开发新业务。

离线通过后，另开终端，macOS/Linux执行：

```bash
source "$HOME/agent-study/reproduce/repo-qa-agent/.venv/bin/activate"
cd "$HOME/agent-study/reproduce/repo-qa-agent"
```

Windows PowerShell执行：

```powershell
function python { & "$HOME/agent-study/reproduce/repo-qa-agent/.venv/Scripts/python.exe" @args }
cd "$HOME/agent-study/reproduce/repo-qa-agent"
```

在新位置从 `.env.example` 手动填写自己的 `.env`（两个文件完整路径分别为 `~/agent-study/reproduce/repo-qa-agent/.env.example`、`~/agent-study/reproduce/repo-qa-agent/.env`）。不要复制旧密钥文件到报告或Git。重新构建索引并做真实问答：

```bash
python -m scripts.build_index --chunks "$HOME/agent-study/reproduce/repo-qa-agent/data/chunks.jsonl" --db "$HOME/agent-study/reproduce/repo-qa-agent/workspace/qdrant" --report "$HOME/agent-study/reproduce/repo-qa-agent/reports/index.json"
python -m scripts.qa --question "如何注册工具？" --mode agent --out "$HOME/agent-study/reproduce/repo-qa-agent/reports/live_answer.json"
```

以上为本轮约定入口；先检查自己的配置确实指向新workspace，不能回读旧索引。`~/agent-study/reproduce/repo-qa-agent/reports/index.json` 与 `~/agent-study/reproduce/repo-qa-agent/reports/live_answer.json` 是本次实际运行后生成的证据。

## 5. 写完以后，运行哪些命令

**下面业务入口需要先完成本日骨架，首次NotImplementedError不是环境故障。**

```bash
cd "$HOME/agent-study/repo-qa-agent"
python "$HOME/agent-study/tools/reproduce.py" prepare
# 阅读它打印的目标清单：不会复制旧环境、旧索引、旧密钥或历史报告
python "$HOME/agent-study/tools/reproduce.py" check
# check会新建独立虚拟环境、按锁文件安装并执行离线测试；结果据实保存
# 完成后返回主项目，继续下面的日常检查
cd "$HOME/agent-study/repo-qa-agent"
python "$HOME/agent-study/tools/check_day.py" 28
```

固定测试+已创建的过去测试输出：`~/agent-study/repo-qa-agent/reports/d28/unittest.txt`。当前算法测试输出：`~/agent-study/repo-qa-agent/reports/d28/algorithm.txt`。有意未做的集成验收不在此命令中冒充通过。

## 6. 算法也固定文件，不临时找题

本日题目：**两数之和改脚本输入输出**。网页题目范围：[只看这道题的题面、输入输出和约束](https://leetcode.cn/problems/two-sum/description/)；闭卷日不打开题解。

代码：`~/agent-study/repo-qa-agent/algorithms/d28_two_sum_cli.py`。测试：`~/agent-study/repo-qa-agent/algorithm_tests/test_d28_two_sum_cli.py`。记录：`~/agent-study/repo-qa-agent/notes/d28.md`。

本地统一接口：`solve(nums: list[int], target: int) -> list[int]`。最小输入：`[2,7,11,15], 9`；预期：`[0,1]`。

运行：从 `~/agent-study/repo-qa-agent/` 执行 `python -m unittest algorithm_tests.test_d28_two_sum_cli -v`。再补2个不同边界；树/链表必须补至少一个非空正常输入，不能只有空输入测试。45分钟后记录真正卡点，不另外开新题。

## 7. 收工前确认

把“是否独立、失败原因、测试输出完整路径、仍未测项、下一次第一步”写入 `~/agent-study/repo-qa-agent/notes/d28.md`。把本日岗位/简历动作写入 `~/agent-study/repo-qa-agent/career/d28_action.md`；只有真实申请才更新 `~/agent-study/repo-qa-agent/career/applications.md`。

**绿灯：** 固定测试与自加边界符合预期，关键逻辑能解释并修改，业务产物真实生成；需要真实模型的学习日另有真实证据。**黄/红灯：** 在当前日卡定位未过函数，不翻页堆欠账。

路径不对先重新运行 `python "$HOME/agent-study/tools/start_day.py" 28` 看打印出的实际地址；它不会覆盖现有文件。模块找不到先确认终端根目录与解释器，不要盲目重装所有依赖。


[COMMIT]: https://github.com/datawhalechina/hello-agents/commit/b4aca1af44b7a492b4bfdec5aa100d556c65db54
[REACT]: https://github.com/datawhalechina/hello-agents/blob/b4aca1af44b7a492b4bfdec5aa100d556c65db54/code/chapter4/ReAct.py
[H1]: https://github.com/datawhalechina/hello-agents/blob/b4aca1af44b7a492b4bfdec5aa100d556c65db54/docs/chapter1/%E7%AC%AC%E4%B8%80%E7%AB%A0%20%E5%88%9D%E8%AF%86%E6%99%BA%E8%83%BD%E4%BD%93.md
[H3]: https://github.com/datawhalechina/hello-agents/blob/b4aca1af44b7a492b4bfdec5aa100d556c65db54/docs/chapter3/%E7%AC%AC%E4%B8%89%E7%AB%A0%20%E5%A4%A7%E8%AF%AD%E8%A8%80%E6%A8%A1%E5%9E%8B%E5%9F%BA%E7%A1%80.md
[H4]: https://github.com/datawhalechina/hello-agents/blob/b4aca1af44b7a492b4bfdec5aa100d556c65db54/docs/chapter4/%E7%AC%AC%E5%9B%9B%E7%AB%A0%20%E6%99%BA%E8%83%BD%E4%BD%93%E7%BB%8F%E5%85%B8%E8%8C%83%E5%BC%8F%E6%9E%84%E5%BB%BA.md
[H6]: https://github.com/datawhalechina/hello-agents/blob/b4aca1af44b7a492b4bfdec5aa100d556c65db54/docs/chapter6/%E7%AC%AC%E5%85%AD%E7%AB%A0%20%E6%A1%86%E6%9E%B6%E5%BC%80%E5%8F%91%E5%AE%9E%E8%B7%B5.md
[H7]: https://github.com/datawhalechina/hello-agents/blob/b4aca1af44b7a492b4bfdec5aa100d556c65db54/docs/chapter7/%E7%AC%AC%E4%B8%83%E7%AB%A0%20%E6%9E%84%E5%BB%BA%E4%BD%A0%E7%9A%84Agent%E6%A1%86%E6%9E%B6.md
[H8]: https://github.com/datawhalechina/hello-agents/blob/b4aca1af44b7a492b4bfdec5aa100d556c65db54/docs/chapter8/%E7%AC%AC%E5%85%AB%E7%AB%A0%20%E8%AE%B0%E5%BF%86%E4%B8%8E%E6%A3%80%E7%B4%A2.md
[H9]: https://github.com/datawhalechina/hello-agents/blob/b4aca1af44b7a492b4bfdec5aa100d556c65db54/docs/chapter9/%E7%AC%AC%E4%B9%9D%E7%AB%A0%20%E4%B8%8A%E4%B8%8B%E6%96%87%E5%B7%A5%E7%A8%8B.md
[H10]: https://github.com/datawhalechina/hello-agents/blob/b4aca1af44b7a492b4bfdec5aa100d556c65db54/docs/chapter10/%E7%AC%AC%E5%8D%81%E7%AB%A0%20%E6%99%BA%E8%83%BD%E4%BD%93%E9%80%9A%E4%BF%A1%E5%8D%8F%E8%AE%AE.md
[H12]: https://github.com/datawhalechina/hello-agents/blob/b4aca1af44b7a492b4bfdec5aa100d556c65db54/docs/chapter12/%E7%AC%AC%E5%8D%81%E4%BA%8C%E7%AB%A0%20%E6%99%BA%E8%83%BD%E4%BD%93%E6%80%A7%E8%83%BD%E8%AF%84%E4%BC%B0.md
[H13]: https://github.com/datawhalechina/hello-agents/blob/b4aca1af44b7a492b4bfdec5aa100d556c65db54/docs/chapter13/%E7%AC%AC%E5%8D%81%E4%B8%89%E7%AB%A0%20%E6%99%BA%E8%83%BD%E6%97%85%E8%A1%8C%E5%8A%A9%E6%89%8B.md
[H16]: https://github.com/datawhalechina/hello-agents/blob/b4aca1af44b7a492b4bfdec5aa100d556c65db54/docs/chapter16/%E7%AC%AC%E5%8D%81%E5%85%AD%E7%AB%A0%20%E6%AF%95%E4%B8%9A%E8%AE%BE%E8%AE%A1.md
[PY_IO]: https://docs.python.org/zh-cn/3.12/tutorial/inputoutput.html
[PY_FLOW]: https://docs.python.org/zh-cn/3.12/tutorial/controlflow.html
[PY_DATA]: https://docs.python.org/zh-cn/3.12/tutorial/datastructures.html
[PY_JSON]: https://docs.python.org/zh-cn/3.12/library/json.html
[PY_UNITTEST]: https://docs.python.org/zh-cn/3.12/library/unittest.html
[FC]: https://developers.openai.com/api/docs/guides/function-calling
[BGE]: https://huggingface.co/BAAI/bge-small-zh-v1.5
[QDRANT]: https://github.com/qdrant/qdrant-client
[FAST_BODY]: https://fastapi.tiangolo.com/tutorial/body/
[FAST_TEST]: https://fastapi.tiangolo.com/tutorial/testing/
[FAST_ERRORS]: https://fastapi.tiangolo.com/tutorial/handling-errors/
[FAST_ASYNC]: https://fastapi.tiangolo.com/async/
[FAST_SECURITY]: https://fastapi.tiangolo.com/reference/security/
[SQLITE]: https://docs.python.org/zh-cn/3.12/library/sqlite3.html
[MCP_SERVER]: https://modelcontextprotocol.io/docs/develop/build-server
[MCP_CLIENT]: https://modelcontextprotocol.io/docs/develop/build-client
[LANGGRAPH]: https://docs.langchain.com/oss/python/langgraph/graph-api
[DOCKER]: https://docs.docker.com/get-started/docker-concepts/building-images/writing-a-dockerfile/
[CI]: https://docs.github.com/en/actions/tutorials/build-and-test-code/python
[PYTEST]: https://docs.pytest.org/en/stable/getting-started.html
[LC1]: https://leetcode.cn/problems/two-sum/description/
[LC20]: https://leetcode.cn/problems/valid-parentheses/description/
[LC206]: https://leetcode.cn/problems/reverse-linked-list/description/
[LC3]: https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/
[LC704]: https://leetcode.cn/problems/binary-search/description/
[LC560]: https://leetcode.cn/problems/subarray-sum-equals-k/description/
[LC102]: https://leetcode.cn/problems/binary-tree-level-order-traversal/description/
[LC200]: https://leetcode.cn/problems/number-of-islands/description/
[LC46]: https://leetcode.cn/problems/permutations/description/
[LC347]: https://leetcode.cn/problems/top-k-frequent-elements/description/
[LC198]: https://leetcode.cn/problems/house-robber/description/
[LC322]: https://leetcode.cn/problems/coin-change/description/
