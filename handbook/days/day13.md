# D13｜带引用的固定RAG

**唯一项目根目录：** `~/agent-study/repo-qa-agent/`。今日任务卡：`~/agent-study/handbook/days/day13.md`。

## 1. 今天具体看哪个文件、读到哪里

|顺序|完整路径与准确范围|只抓住什么|
|---|---|---|
|1|`~/agent-study/materials/hello-agents/docs/chapter8/第八章 记忆与检索.md`<br>**L1110–L1126**<br>[打开固定版本相同行范围](https://github.com/datawhalechina/hello-agents/blob/b4aca1af44b7a492b4bfdec5aa100d556c65db54/docs/chapter8/%E7%AC%AC%E5%85%AB%E7%AB%A0%20%E8%AE%B0%E5%BF%86%E4%B8%8E%E6%A3%80%E7%B4%A2.md#L1110-L1126)|8.3.2：两种工作流程及后续入口|
|2|`~/agent-study/materials/notes/13_rag.md`<br>**L1–L24**<br>本包已提供；本次补课讲义，不是教材原文。|D13 补课：三段式RAG（本次补课讲义）|

**学到这里停：** 能说出今天目标函数接什么输入、返回什么、至少一个错误分支；接着按下表写代码。源码中的图像不需要下载，未指定内容本日不读。

## 2. 先准备文件，再动手

```bash
cd "$HOME/agent-study/repo-qa-agent"
python "$HOME/agent-study/tools/start_day.py" 13
python "$HOME/agent-study/tools/read_today.py" 13
```

自动生成的阅读页：`~/agent-study/handbook/readings/day13.html`；对应带行号文本：`~/agent-study/handbook/readings/day13.txt`。

## 3. 今天所有文件的完整路径

|动作|完整路径|你在这里做什么|
|---|---|---|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/agent_lab/rag.py`|构造证据提示、生成和引用存在性校验|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/agent_lab/service.py`|CLI/API共用的业务入口；注入检索器与模型|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/prompts/rag_answer.txt`|只依据证据、引用ID、不足提示规则|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/scripts/qa.py`|keyword/vector两种模式CLI|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/tests/test_d13_rag.py`|空检索、非法引用、合法引用测试|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/algorithms/d13_subarray_sum_rewrite.py`|算法独立实现；闭卷日新文件不覆盖旧答案|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/algorithm_tests/test_d13_subarray_sum_rewrite.py`|已给最小样例，你另补2个有效边界|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/notes/d13.md`|今日复盘、算法用时、错误与下一步|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/career/d13_action.md`|今日求职动作与真实证据|
|修改既有文件|`~/agent-study/repo-qa-agent/agent_lab/llm.py`|复用D4客户端，不复制第二套请求实现|
|修改既有文件|`~/agent-study/repo-qa-agent/career/applications.md`|仅记录真实岗位资格、申请和反馈|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d13/dev5_raw.jsonl`|5题真实证据与回答|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d13/dev5_review.md`|对应人工判断、错因和边界|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d13/unittest.txt`|check_day.py自动保存主项目测试输出|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d13/algorithm.txt`|check_day.py自动保存算法测试输出|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d13/example.json`|单条真实问答演示|

**“新建一次”已由准备工具完成时，你只需要打开并填内容；不要删掉重建。报告初始状态NOT_DONE不是成绩。程序生成项没有实际运行结果前不要填写成功。**

## 4. 要写的接口、具体操作和停止标准

```text
answer(question: str, retrieve, model) -> dict
query_service(question: str, mode: str, history: list | None = None) -> dict
结果至少 answer/citations/insufficient_evidence/status；引用渲染必须回查本次证据集。
```

**前置：** D12真实向量检索可用。

**步骤：** 新建`~/agent-study/repo-qa-agent/agent_lab/rag.py`，实现`answer(question,retrieve,model)`：取Top-3结果、给每条分配可追溯的引用ID、构造“仅依据给定证据”的提示、生成结构化回答、校验引用ID。关键词检索和向量检索只替换retrieve，不换回答模型与提示。结果统一为`answer/citations/insufficient_evidence`；citations中每条最终渲染为源文件、版本、行范围。

提示模板自己写，必须包含：任务、证据块、无法支持时说明不足、材料中的指令只当引用内容。没有检索结果时直接返回不足，不调用模型。有结果也不等于能回答，仍由模型判别并人工核证。不要把相似度0.7之类的任意值当通用拒答阈值。

**固定用例：** 给出一段只谈工具注册的资料，问它的训练GPU数量，应说明不足；模型伪造不存在的引用ID时结果不得原样发布；一个真实有答案问题的每项核心结论必须能指回原文。引用存在性校验不能证明原文真的支持该结论。

**验收：** 新建`~/agent-study/repo-qa-agent/tests/test_d13_rag.py`，至少测空检索、非法引用、正常引用三条确定性路径；再人工核5道开发题（含至少2道无答案题）。把完整输入证据、回答、评分理由保存，失败也保留。通过线是程序边界全对且至少一条真实有据回答/一条无依据拒答能演示，不要求凭空预设90%准确率。

**交什么：** `~/agent-study/repo-qa-agent/agent_lab/rag.py`、测试、5条原始输出；新建薄CLI `~/agent-study/repo-qa-agent/scripts/qa.py`，约定**见本日运行区的完整命令**可运行。

**口述：** 先找“标准证据有没有被召回”，再找“模型有没有正确用证据”；只看回答流畅度无法定位哪一层错。

**卡住：** 先手工塞入1个正确证据测试生成，再恢复真实检索，不同时调分块、Top-k和提示。

**求职：** 写一条带边界的项目事实：“在限定教程语料上实现带文件/行号来源的问答”；尚未完成的部分不写。

### 本版锁定的固定输入 / 预期

空证据时模型调用数0；伪造引用不得直接发布；5题人工含至少2道无答案。

## 5. 写完以后，运行哪些命令

**下面业务入口需要先完成本日骨架，首次NotImplementedError不是环境故障。**

```bash
cd "$HOME/agent-study/repo-qa-agent"
python -m scripts.qa --mode vector --question "ReAct循环如何停止" --out "$HOME/agent-study/repo-qa-agent/reports/d13/example.json"
python "$HOME/agent-study/tools/check_day.py" 13
```

固定测试+已创建的过去测试输出：`~/agent-study/repo-qa-agent/reports/d13/unittest.txt`。当前算法测试输出：`~/agent-study/repo-qa-agent/reports/d13/algorithm.txt`。有意未做的集成验收不在此命令中冒充通过。

## 6. 算法也固定文件，不临时找题

本日题目：**前缀和闭卷**。网页题目范围：[只看这道题的题面、输入输出和约束](https://leetcode.cn/problems/subarray-sum-equals-k/description/)；闭卷日不打开题解。

代码：`~/agent-study/repo-qa-agent/algorithms/d13_subarray_sum_rewrite.py`。测试：`~/agent-study/repo-qa-agent/algorithm_tests/test_d13_subarray_sum_rewrite.py`。记录：`~/agent-study/repo-qa-agent/notes/d13.md`。

本地统一接口：`solve(nums: list[int], k: int) -> int`。最小输入：`[1,-1,0], 0`；预期：`3`。

运行：从 `~/agent-study/repo-qa-agent/` 执行 `python -m unittest algorithm_tests.test_d13_subarray_sum_rewrite -v`。再补2个不同边界；树/链表必须补至少一个非空正常输入，不能只有空输入测试。45分钟后记录真正卡点，不另外开新题。

## 7. 收工前确认

把“是否独立、失败原因、测试输出完整路径、仍未测项、下一次第一步”写入 `~/agent-study/repo-qa-agent/notes/d13.md`。把本日岗位/简历动作写入 `~/agent-study/repo-qa-agent/career/d13_action.md`；只有真实申请才更新 `~/agent-study/repo-qa-agent/career/applications.md`。

**绿灯：** 固定测试与自加边界符合预期，关键逻辑能解释并修改，业务产物真实生成；需要真实模型的学习日另有真实证据。**黄/红灯：** 在当前日卡定位未过函数，不翻页堆欠账。

路径不对先重新运行 `python "$HOME/agent-study/tools/start_day.py" 13` 看打印出的实际地址；它不会覆盖现有文件。模块找不到先确认终端根目录与解释器，不要盲目重装所有依赖。


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
