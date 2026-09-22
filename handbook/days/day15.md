# D15｜第二关：Agent接入RAG

**唯一项目根目录：** `~/agent-study/repo-qa-agent/`。今日任务卡：`~/agent-study/handbook/days/day15.md`。

## 1. 今天具体看哪个文件、读到哪里

|顺序|完整路径与准确范围|只抓住什么|
|---|---|---|
|1|`~/agent-study/materials/hello-agents/code/chapter4/ReAct.py`<br>**L32–L74**<br>[打开固定版本相同行范围](https://github.com/datawhalechina/hello-agents/blob/b4aca1af44b7a492b4bfdec5aa100d556c65db54/code/chapter4/ReAct.py#L32-L74)|复用工具循环，不另写框架|
|2|`~/agent-study/materials/notes/15_agent_rag.md`<br>**L1–L23**<br>本包已提供；本次补课讲义，不是教材原文。|D15 补课：把工具与证据接起来（本次补课讲义）|

**学到这里停：** 能说出今天目标函数接什么输入、返回什么、至少一个错误分支；接着按下表写代码。源码中的图像不需要下载，未指定内容本日不读。

## 2. 先准备文件，再动手

```bash
cd "$HOME/agent-study/repo-qa-agent"
python "$HOME/agent-study/tools/start_day.py" 15
python "$HOME/agent-study/tools/read_today.py" 15
```

自动生成的阅读页：`~/agent-study/handbook/readings/day15.html`；对应带行号文本：`~/agent-study/handbook/readings/day15.txt`。

## 3. 今天所有文件的完整路径

|动作|完整路径|你在这里做什么|
|---|---|---|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/agent_lab/qa_agent.py`|绑定search_docs/read_chunk，记录已见证据与引用|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/tests/test_d15_agent.py`|跨片段、证据不足、限次补查与非法引用测试|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/reports/d15/gate2.md`|五类场景的真实/模拟验收|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/career/resume_v01.md`|只写已完成功能的简历第一版|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/algorithms/d15_level_order_rewrite.py`|算法独立实现；闭卷日新文件不覆盖旧答案|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/algorithm_tests/test_d15_level_order_rewrite.py`|已给最小样例，你另补2个有效边界|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/notes/d15.md`|今日复盘、算法用时、错误与下一步|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/career/d15_action.md`|今日求职动作与真实证据|
|修改既有文件|`~/agent-study/repo-qa-agent/agent_lab/service.py`|增加agent模式|
|修改既有文件|`~/agent-study/repo-qa-agent/scripts/qa.py`|增加--mode agent|
|修改既有文件|`~/agent-study/repo-qa-agent/agent_lab/loop.py`|保留旧字段意义，增加最终citations与工具次数|
|修改既有文件|`~/agent-study/repo-qa-agent/README.md`|可解释演示版本及未完成列表|
|修改既有文件|`~/agent-study/repo-qa-agent/career/applications.md`|仅记录真实岗位资格、申请和反馈|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d15/fact.json`|真实事实问答|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d15/cross.json`|真实跨片段问答|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d15/no_answer.json`|真实材料不足处理|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d15/demo.mp4`|2–3分钟演示|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d15/unittest.txt`|check_day.py自动保存主项目测试输出|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d15/algorithm.txt`|check_day.py自动保存算法测试输出|

**“新建一次”已由准备工具完成时，你只需要打开并填内容；不要删掉重建。报告初始状态NOT_DONE不是成绩。程序生成项没有实际运行结果前不要填写成功。**

## 4. 要写的接口、具体操作和停止标准

```text
run_qa_agent(question: str, model, chunks: list[dict], retriever) -> dict
最多4轮模型、3次工具；额外补检索最多1次；本日无自动重试。
```

**前置：** 固定RAG可用，第一关真实模型证据补齐。

**步骤：** 将D12检索与D3原文补读接入D6手写Agent，或已通过D8测试的原生工具循环。固定RAG继续作为基线，不能因为加入Agent就删掉。限制模型最多4轮、检索/补读等工具总计最多3次；资料不足时允许至多1次新的补检索，其余按证据结束。不要强迫每个问题必须多轮。

把D6结果扩展为可携带最终citations，并通过D13的来源校验与渲染后再展示；返回字段可以新增，但不改变旧测试中steps/status的含义。将`--mode agent`加入D13 CLI。固定演示5个场景：单片段事实、跨片段、无答案、工具不存在/参数错误、达到调用上限。其中前三种用真实模型；错误与上限用脚本模型稳定复现。追问功能尚未做，D16再验收。

**通过线：** 5类场景均有可复现执行路径；有答案例子引用可定位；无答案不编造；异常不会无限调用。对模型答错的个案保存失败说明，不伪造全部正确。20开发题/10留出题、至少两个基线文件仍可访问。用5分钟解释一条请求经过哪些函数。

**交什么：** `~/agent-study/repo-qa-agent/reports/d15/gate2.md`、2–3分钟演示、README首版、项目已完成/未完成清单。当前项目只证明限定语料原型能力，不称生产系统。

**未过：** D16先替换为修复日；删掉融合、重排、界面、复杂规划。只有15天硬期限时，交到这里并从真实能力出发投递，后半程不压缩成虚假的已完成清单。

**求职：** 基于真实演示与CRUD经历写简历v0.1；找到资格/语言/出勤均匹配的岗位后开始小批投递，不等“全书学完”。项目尚不能解释时先修材料，不为完成数量硬投。

### 本版锁定的固定输入 / 预期

前三类使用真实模型；未知工具/次数上限用假模型可重复触发。不能只演示漂亮的一例就说五类全过。

## 5. 写完以后，运行哪些命令

**下面业务入口需要先完成本日骨架，首次NotImplementedError不是环境故障。**

```bash
cd "$HOME/agent-study/repo-qa-agent"
python -m scripts.qa --mode agent --question "ReAct如何查找工具，又如何在未知工具时处理" --out "$HOME/agent-study/repo-qa-agent/reports/d15/fact.json"
python "$HOME/agent-study/tools/check_day.py" 15
```

固定测试+已创建的过去测试输出：`~/agent-study/repo-qa-agent/reports/d15/unittest.txt`。当前算法测试输出：`~/agent-study/repo-qa-agent/reports/d15/algorithm.txt`。有意未做的集成验收不在此命令中冒充通过。

## 6. 算法也固定文件，不临时找题

本日题目：**层序遍历闭卷**。网页题目范围：[只看这道题的题面、输入输出和约束](https://leetcode.cn/problems/binary-tree-level-order-traversal/description/)；闭卷日不打开题解。

代码：`~/agent-study/repo-qa-agent/algorithms/d15_level_order_rewrite.py`。测试：`~/agent-study/repo-qa-agent/algorithm_tests/test_d15_level_order_rewrite.py`。记录：`~/agent-study/repo-qa-agent/notes/d15.md`。

本地统一接口：`solve(root) -> list[list[int]]`。最小输入：`None`；预期：`[]`。

运行：从 `~/agent-study/repo-qa-agent/` 执行 `python -m unittest algorithm_tests.test_d15_level_order_rewrite -v`。再补2个不同边界；树/链表必须补至少一个非空正常输入，不能只有空输入测试。45分钟后记录真正卡点，不另外开新题。

## 7. 收工前确认

把“是否独立、失败原因、测试输出完整路径、仍未测项、下一次第一步”写入 `~/agent-study/repo-qa-agent/notes/d15.md`。把本日岗位/简历动作写入 `~/agent-study/repo-qa-agent/career/d15_action.md`；只有真实申请才更新 `~/agent-study/repo-qa-agent/career/applications.md`。

**绿灯：** 固定测试与自加边界符合预期，关键逻辑能解释并修改，业务产物真实生成；需要真实模型的学习日另有真实证据。**黄/红灯：** 在当前日卡定位未过函数，不翻页堆欠账。

路径不对先重新运行 `python "$HOME/agent-study/tools/start_day.py" 15` 看打印出的实际地址；它不会覆盖现有文件。模块找不到先确认终端根目录与解释器，不要盲目重装所有依赖。


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
