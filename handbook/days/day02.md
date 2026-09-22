# D02｜带行号的分块

**唯一项目根目录：** `~/agent-study/repo-qa-agent/`。今日任务卡：`~/agent-study/handbook/days/day02.md`。

## 1. 今天具体看哪个文件、读到哪里

|顺序|完整路径与准确范围|只抓住什么|
|---|---|---|
|1|`~/agent-study/materials/hello-agents/docs/chapter8/第八章 记忆与检索.md`<br>**L1085–L1100**<br>[打开固定版本相同行范围](https://github.com/datawhalechina/hello-agents/blob/b4aca1af44b7a492b4bfdec5aa100d556c65db54/docs/chapter8/%E7%AC%AC%E5%85%AB%E7%AB%A0%20%E8%AE%B0%E5%BF%86%E4%B8%8E%E6%A3%80%E7%B4%A2.md#L1085-L1100)|RAG概念与数据准备流程|
|2|`~/agent-study/materials/notes/02_python_chunking.md`<br>**L1–L28**<br>本包已提供；本次补课讲义，不是教材原文。|D02 补课：行号与切片（本次补课讲义）|
|最后|`~/agent-study/repo-qa-agent/tests/test_d02_chunking.py`<br>**L1–L28，读完整文件，不修改固定预期。**|先读每个测试名，再读输入和断言；这是当天作业的精确契约。|
|样例|`~/agent-study/repo-qa-agent/fixtures/mini.md`<br>**L1–L8**|今天唯一小样例；不要换成整本教程。|

**学到这里停：** 能说出今天目标函数接什么输入、返回什么、至少一个错误分支；接着按下表写代码。源码中的图像不需要下载，未指定内容本日不读。

## 2. 先准备文件，再动手

```bash
cd "$HOME/agent-study/repo-qa-agent"
python "$HOME/agent-study/tools/start_day.py" 2
python "$HOME/agent-study/tools/read_today.py" 2
```

自动生成的阅读页：`~/agent-study/handbook/readings/day02.html`；对应带行号文本：`~/agent-study/handbook/readings/day02.txt`。

## 3. 今天所有文件的完整路径

|动作|完整路径|你在这里做什么|
|---|---|---|
|只读：已提供|`~/agent-study/repo-qa-agent/tests/test_d02_chunking.py`|固定验收用例；不改预期值来刷绿。|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/scripts/d02_chunk_demo.py`|调用昨日读写与今日分块|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/tests/test_d02_extra.py`|自己补连续标题用例|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/algorithms/d02_two_sum_rewrite.py`|算法独立实现；闭卷日新文件不覆盖旧答案|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/algorithm_tests/test_d02_two_sum_rewrite.py`|已给最小样例，你另补2个有效边界|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/notes/d02.md`|今日复盘、算法用时、错误与下一步|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/career/d02_action.md`|今日求职动作与真实证据|
|修改既有文件|`~/agent-study/repo-qa-agent/agent_lab/chunking.py`|已有骨架：只实现限定Markdown分块|
|修改既有文件|`~/agent-study/repo-qa-agent/career/applications.md`|仅记录真实岗位资格、申请和反馈|
|运行或录制后生成|`~/agent-study/repo-qa-agent/workspace/d02/chunks.jsonl`|固定样例分成3块|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d02/chunks.txt`|打印每块ID、标题、起止行|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d02/unittest.txt`|check_day.py自动保存主项目测试输出|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d02/algorithm.txt`|check_day.py自动保存算法测试输出|

**“新建一次”已由准备工具完成时，你只需要打开并填内容；不要删掉重建。报告初始状态NOT_DONE不是成绩。程序生成项没有实际运行结果前不要填写成功。**

## 4. 要写的接口、具体操作和停止标准

```text
split_markdown(text: str, source: str) -> list[dict]
```

**前置：** D1绿灯。**今天结束时：** 给一份小Markdown，能说清每块来自原文第几行。



**步骤：** 纸上给`~/agent-study/repo-qa-agent/fixtures/mini.md`标行号1–8，找到标题行1、4、7。实现`split_markdown(text,source)`：先收集标题起点，再把下一标题前一行作为当前终点；最后一块终点是总行数。标题行保留在正文里；标题前的非空文字单独标“未分节”。把结果接D1写出到`~/agent-study/repo-qa-agent/workspace/d02/chunks.jsonl`。

**契约/样例：** 每条含`id/source/title/start_line/end_line/text`；`id=source#L起点-L终点`。`~/agent-study/repo-qa-agent/fixtures/mini.md`必须得到3块，范围分别`1–3 / 4–6 / 7–8`，标题“工具/检索/安全”。行号从1开始且包含两端，正文等于原文相应行拼接。

**验收：** **见本日运行区的完整命令**，6项全过。自加连续标题或只有标题的用例；同名标题产生不同ID；最后一块不能丢。把`##`改成`###`结果仍正确。交代码、JSONL和一张手画行号图。

**口述：** Python切片右端不包含，但本项目原文行号两端包含；转换是`lines[start-1:end]`。为什么不能只用标题作ID？关键词：标题可重复、来源定位。

**卡住：** 先只支持单个`#`标题；2块样例过后再支持1–6个`#`。这不是完整Markdown解析器；围栏代码块内的`#`暂不支持，D9再补。不要因为解析边界去学AST/语法分析全套。

**求职：** 从官方招聘入口找1个Python/多语言Agent应用实习JD，保存链接与查询日期；没有匹配项也记录原因。

### 本版锁定的固定输入 / 预期

已有6个固定测试全过。mini.md 共8行，切块范围为1–3、4–6、7–8。起止行包含两端，正文可原样还原。

## 5. 写完以后，运行哪些命令

**下面业务入口需要先完成本日骨架，首次NotImplementedError不是环境故障。**

```bash
cd "$HOME/agent-study/repo-qa-agent"
python -m scripts.d02_chunk_demo
python "$HOME/agent-study/tools/check_day.py" 2
```

固定测试+已创建的过去测试输出：`~/agent-study/repo-qa-agent/reports/d02/unittest.txt`。当前算法测试输出：`~/agent-study/repo-qa-agent/reports/d02/algorithm.txt`。有意未做的集成验收不在此命令中冒充通过。

## 6. 算法也固定文件，不临时找题

本日题目：**两数之和闭卷**。网页题目范围：[只看这道题的题面、输入输出和约束](https://leetcode.cn/problems/two-sum/description/)；闭卷日不打开题解。

代码：`~/agent-study/repo-qa-agent/algorithms/d02_two_sum_rewrite.py`。测试：`~/agent-study/repo-qa-agent/algorithm_tests/test_d02_two_sum_rewrite.py`。记录：`~/agent-study/repo-qa-agent/notes/d02.md`。

本地统一接口：`solve(nums: list[int], target: int) -> list[int]`。最小输入：`[3, 3], 6`；预期：`[0, 1]`。

运行：从 `~/agent-study/repo-qa-agent/` 执行 `python -m unittest algorithm_tests.test_d02_two_sum_rewrite -v`。再补2个不同边界；树/链表必须补至少一个非空正常输入，不能只有空输入测试。45分钟后记录真正卡点，不另外开新题。

## 7. 收工前确认

把“是否独立、失败原因、测试输出完整路径、仍未测项、下一次第一步”写入 `~/agent-study/repo-qa-agent/notes/d02.md`。把本日岗位/简历动作写入 `~/agent-study/repo-qa-agent/career/d02_action.md`；只有真实申请才更新 `~/agent-study/repo-qa-agent/career/applications.md`。

**绿灯：** 固定测试与自加边界符合预期，关键逻辑能解释并修改，业务产物真实生成；需要真实模型的学习日另有真实证据。**黄/红灯：** 在当前日卡定位未过函数，不翻页堆欠账。

路径不对先重新运行 `python "$HOME/agent-study/tools/start_day.py" 2` 看打印出的实际地址；它不会覆盖现有文件。模块找不到先确认终端根目录与解释器，不要盲目重装所有依赖。


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
