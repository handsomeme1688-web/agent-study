# D09｜真实语料导入

**唯一项目根目录：** `~/agent-study/repo-qa-agent/`。今日任务卡：`~/agent-study/handbook/days/day09.md`。

## 1. 今天具体看哪个文件、读到哪里

|顺序|完整路径与准确范围|只抓住什么|
|---|---|---|
|1|`~/agent-study/materials/hello-agents/docs/chapter8/第八章 记忆与检索.md`<br>**L1085–L1100**<br>[打开固定版本相同行范围](https://github.com/datawhalechina/hello-agents/blob/b4aca1af44b7a492b4bfdec5aa100d556c65db54/docs/chapter8/%E7%AC%AC%E5%85%AB%E7%AB%A0%20%E8%AE%B0%E5%BF%86%E4%B8%8E%E6%A3%80%E7%B4%A2.md#L1085-L1100)|资料准备与检索生成流程|
|2|`~/agent-study/materials/hello-agents/docs/chapter8/第八章 记忆与检索.md`<br>**L1275–L1320**<br>[打开固定版本相同行范围](https://github.com/datawhalechina/hello-agents/blob/b4aca1af44b7a492b4bfdec5aa100d556c65db54/docs/chapter8/%E7%AC%AC%E5%85%AB%E7%AB%A0%20%E8%AE%B0%E5%BF%86%E4%B8%8E%E6%A3%80%E7%B4%A2.md#L1275-L1320)|结构感知分块说明与部分实现|
|3|`~/agent-study/materials/notes/09_ingest.md`<br>**L1–L25**<br>本包已提供；本次补课讲义，不是教材原文。|D09 补课：固定版本、稳定ID和原文还原（本次补课讲义）|

**学到这里停：** 能说出今天目标函数接什么输入、返回什么、至少一个错误分支；接着按下表写代码。源码中的图像不需要下载，未指定内容本日不读。

## 2. 先准备文件，再动手

```bash
cd "$HOME/agent-study/repo-qa-agent"
python "$HOME/agent-study/tools/start_day.py" 9
python "$HOME/agent-study/tools/read_today.py" 9
```

自动生成的阅读页：`~/agent-study/handbook/readings/day09.html`；对应带行号文本：`~/agent-study/handbook/readings/day09.txt`。

## 3. 今天所有文件的完整路径

|动作|完整路径|你在这里做什么|
|---|---|---|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/agent_lab/ingest.py`|读取固定源区间，围栏处理，稳定ID和来源行号|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/scripts/ingest.py`|根据source_manifest导入公开资料|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/data/source_manifest.json`|4个固定源文件、提交、选定行范围|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/tests/test_d09_ingest.py`|重导入、围栏与行号还原测试|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/algorithms/d09_longest_substring_rewrite.py`|算法独立实现；闭卷日新文件不覆盖旧答案|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/algorithm_tests/test_d09_longest_substring_rewrite.py`|已给最小样例，你另补2个有效边界|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/notes/d09.md`|今日复盘、算法用时、错误与下一步|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/career/d09_action.md`|今日求职动作与真实证据|
|修改既有文件|`~/agent-study/repo-qa-agent/agent_lab/chunking.py`|保留D2函数契约；新增真实Markdown处理函数，不破坏旧样例|
|修改既有文件|`~/agent-study/repo-qa-agent/career/applications.md`|仅记录真实岗位资格、申请和反馈|
|运行或录制后生成|`~/agent-study/repo-qa-agent/data/chunks.jsonl`|正式限定语料片段|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d09/ingest.json`|文件摘要、片段数与5条人工位置核验|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d09/unittest.txt`|check_day.py自动保存主项目测试输出|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d09/algorithm.txt`|check_day.py自动保存算法测试输出|

**“新建一次”已由准备工具完成时，你只需要打开并填内容；不要删掉重建。报告初始状态NOT_DONE不是成绩。程序生成项没有实际运行结果前不要填写成功。**

## 4. 要写的接口、具体操作和停止标准

```text
ingest_manifest(manifest_path: str, output_path: str) -> list[dict]
每块含 id/source/revision/start_line/end_line/text；source是登记的仓库内逻辑路径，不是任意可读路径。
```

**前置：** D2/3绿灯。

**步骤：** 从本任务书固定提交链接保存4个文本源：[第4章][H4]、[第7章][H7]、[第8章][H8]和[ReAct.py][REACT]。只选第4章ReAct原理、第7章消息/工具注册、第8章RAG基本流程及ReAct代码，目标20–40个片段。不要索引完整仓库。新建`~/agent-study/repo-qa-agent/data/source_manifest.json`记录仓库提交、路径、选择的原文行范围及本地原始文件摘要。

扩展D2：Markdown围栏中的`#`不作标题；长段落按完整行继续切分，保存真实原文行号。Python文件按连续约20行窗口切，不把注释当Markdown标题。先无重叠，超长单行不偷偷截断；记录该片段为需处理。ID加入源提交/路径/行范围；同一版本重复导入ID不变，版本改变先整体重建该小语料索引，避免遗留旧块。

**验收：** 新建`~/agent-study/repo-qa-agent/tests/test_d09_ingest.py`，测试重复导入不翻倍、代码围栏标题不误切、源行可准确还原。命令**见本日运行区的完整命令**。随机抽5块，在固定版本原文中找到完全相同的文字及行号；5/5定位一致即通过。交manifest与chunks.jsonl。

**口述：** 为什么来源版本必须保存？原文更新会使旧行号/证据失效。为什么只导少量语料？为了能人工核证，不是宣称覆盖全库。

**卡住：** 先只取ReAct.py的两段代码跑通行号映射，再加Markdown；把支持格式写入README，不做“万能文件解析器”。

**求职：** 记录1个新岗位的硬条件；原计划中的旧岗位链接只作查找入口，当前状态需你重新确认。

### 本版锁定的固定输入 / 预期

重导入字节或记录内容稳定、无重复ID；抽5块行号与原文5/5一致。Python按连续窗口切，不按#标题切。

### 本版已经替你固定的语料清单

`~/agent-study/repo-qa-agent/data/source_manifest.json` 已提供4个源文件和准确行范围、`chunk_max_lines=15`。今天只实现读取、切分和核对，暂不自行扩展语料；源路径中的`~`必须用`Path(...).expanduser()`展开。15行是本轮默认上限，不是教材的通用最佳参数。

## 5. 写完以后，运行哪些命令

**下面业务入口需要先完成本日骨架，首次NotImplementedError不是环境故障。**

```bash
cd "$HOME/agent-study/repo-qa-agent"
python -m scripts.ingest --manifest "$HOME/agent-study/repo-qa-agent/data/source_manifest.json" --out "$HOME/agent-study/repo-qa-agent/data/chunks.jsonl" --report "$HOME/agent-study/repo-qa-agent/reports/d09/ingest.json"
python "$HOME/agent-study/tools/check_day.py" 9
```

固定测试+已创建的过去测试输出：`~/agent-study/repo-qa-agent/reports/d09/unittest.txt`。当前算法测试输出：`~/agent-study/repo-qa-agent/reports/d09/algorithm.txt`。有意未做的集成验收不在此命令中冒充通过。

## 6. 算法也固定文件，不临时找题

本日题目：**最长子串闭卷**。网页题目范围：[只看这道题的题面、输入输出和约束](https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/)；闭卷日不打开题解。

代码：`~/agent-study/repo-qa-agent/algorithms/d09_longest_substring_rewrite.py`。测试：`~/agent-study/repo-qa-agent/algorithm_tests/test_d09_longest_substring_rewrite.py`。记录：`~/agent-study/repo-qa-agent/notes/d09.md`。

本地统一接口：`solve(s: str) -> int`。最小输入：`""`；预期：`0`。

运行：从 `~/agent-study/repo-qa-agent/` 执行 `python -m unittest algorithm_tests.test_d09_longest_substring_rewrite -v`。再补2个不同边界；树/链表必须补至少一个非空正常输入，不能只有空输入测试。45分钟后记录真正卡点，不另外开新题。

## 7. 收工前确认

把“是否独立、失败原因、测试输出完整路径、仍未测项、下一次第一步”写入 `~/agent-study/repo-qa-agent/notes/d09.md`。把本日岗位/简历动作写入 `~/agent-study/repo-qa-agent/career/d09_action.md`；只有真实申请才更新 `~/agent-study/repo-qa-agent/career/applications.md`。

**绿灯：** 固定测试与自加边界符合预期，关键逻辑能解释并修改，业务产物真实生成；需要真实模型的学习日另有真实证据。**黄/红灯：** 在当前日卡定位未过函数，不翻页堆欠账。

路径不对先重新运行 `python "$HOME/agent-study/tools/start_day.py" 9` 看打印出的实际地址；它不会覆盖现有文件。模块找不到先确认终端根目录与解释器，不要盲目重装所有依赖。


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
