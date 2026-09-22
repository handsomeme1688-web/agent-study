# D14｜关键词与向量基线

**唯一项目根目录：** `~/agent-study/repo-qa-agent/`。今日任务卡：`~/agent-study/handbook/days/day14.md`。

## 1. 今天具体看哪个文件、读到哪里

|顺序|完整路径与准确范围|只抓住什么|
|---|---|---|
|1|`~/agent-study/materials/hello-agents/docs/chapter12/第十二章 智能体性能评估.md`<br>**L45–L52**<br>[打开固定版本相同行范围](https://github.com/datawhalechina/hello-agents/blob/b4aca1af44b7a492b4bfdec5aa100d556c65db54/docs/chapter12/%E7%AC%AC%E5%8D%81%E4%BA%8C%E7%AB%A0%20%E6%99%BA%E8%83%BD%E4%BD%93%E6%80%A7%E8%83%BD%E8%AF%84%E4%BC%B0.md#L45-L52)|对照与评估挑战|
|2|`~/agent-study/materials/hello-agents/docs/chapter12/第十二章 智能体性能评估.md`<br>**L81–L109**<br>[打开固定版本相同行范围](https://github.com/datawhalechina/hello-agents/blob/b4aca1af44b7a492b4bfdec5aa100d556c65db54/docs/chapter12/%E7%AC%AC%E5%8D%81%E4%BA%8C%E7%AB%A0%20%E6%99%BA%E8%83%BD%E4%BD%93%E6%80%A7%E8%83%BD%E8%AF%84%E4%BC%B0.md#L81-L109)|指标与人工验证|
|3|`~/agent-study/materials/notes/10_evaluation.md`<br>**L1–L31**<br>本包已提供；本次补课讲义，不是教材原文。|评测补课：题目、原始输出与人工分数（本次补课讲义）|

**学到这里停：** 能说出今天目标函数接什么输入、返回什么、至少一个错误分支；接着按下表写代码。源码中的图像不需要下载，未指定内容本日不读。

## 2. 先准备文件，再动手

```bash
cd "$HOME/agent-study/repo-qa-agent"
python "$HOME/agent-study/tools/start_day.py" 14
python "$HOME/agent-study/tools/read_today.py" 14
```

自动生成的阅读页：`~/agent-study/handbook/readings/day14.html`；对应带行号文本：`~/agent-study/handbook/readings/day14.txt`。

## 3. 今天所有文件的完整路径

|动作|完整路径|你在这里做什么|
|---|---|---|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/agent_lab/evaluation.py`|保存每题结果，汇总人工分数，不由回答流畅度自动判满分|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/scripts/evaluate.py`|逐题运行指定模式，先保存原始JSONL|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/scripts/score_report.py`|按评分文件汇总指标与分母|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/reports/d14/dev_scores.jsonl`|逐题人工评分，原始回答不得改写|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/reports/d14/baseline.md`|两个基线的配置、结果和错误分类|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/algorithms/d14_level_order.py`|算法独立实现；闭卷日新文件不覆盖旧答案|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/algorithm_tests/test_d14_level_order.py`|已给最小样例，你另补2个有效边界|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/notes/d14.md`|今日复盘、算法用时、错误与下一步|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/career/d14_action.md`|今日求职动作与真实证据|
|修改既有文件|`~/agent-study/repo-qa-agent/agent_lab/service.py`|确保仅替换检索方式而不换回答模型|
|修改既有文件|`~/agent-study/repo-qa-agent/career/applications.md`|仅记录真实岗位资格、申请和反馈|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d14/keyword_raw.jsonl`|20题关键词RAG原始输出|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d14/vector_raw.jsonl`|20题向量RAG原始输出|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d14/summary.json`|两个方案的计分结果|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d14/unittest.txt`|check_day.py自动保存主项目测试输出|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d14/algorithm.txt`|check_day.py自动保存算法测试输出|

**“新建一次”已由准备工具完成时，你只需要打开并填内容；不要删掉重建。报告初始状态NOT_DONE不是成绩。程序生成项没有实际运行结果前不要填写成功。**

## 4. 要写的接口、具体操作和停止标准

```text
evaluate_rows(rows: list[dict], query_fn, config: dict) -> list[dict]
summarize_scores(scores: list[dict]) -> dict
```

**前置：** D10题集与D13固定RAG。

**步骤：** 新建`~/agent-study/repo-qa-agent/scripts/evaluate.py`，从dev.jsonl逐题读取，用同一模型、提示、语料分别跑关键词RAG与向量RAG。每题保存qid、配置、检索ID、回答、引用、耗时、调用数、可取得的token用量；先写原始JSONL，再人工评分，不直接输出一个看不见分母的百分比。命令约定**见本日运行区的完整命令**与`--mode vector`。

**具体评分：** 可回答题检查预设答案要点、原文支持与来源；无答案题检查是否明确说明材料不足且未编造核心结论。检索指标只对16道可回答开发题统计，不能把4道无答案题塞进检索分母。每条失败标一种主原因：缺语料/没召回/上下文遗漏/生成错误/引用错误/执行失败。

**验收：** 两个基线各20条原始结果与20条人工评分，分母与无答案题数量一致；没有token字段时记null/未测，不填写0冒充实际消耗。随机抽3题从汇总数字追溯到原始输出和标准证据。交`reports/dev_keyword.*`、`dev_vector.*`及`~/agent-study/repo-qa-agent/reports/d14/baseline.md`。

**通过线：** 报告可复查、分母正确、失败可归类，不以“必须提升某个百分点”为门槛。若服务费用不足，明确哪部分未跑完整，不用mock输出填真实质量表。

**口述：** 检索Recall与最终任务成功是不同指标；同一批问题/模型/语料才能形成可解释比较。慢在哪里也要分阶段计时。

**卡住：** 先评3题把文件结构走通，再跑余下17题；不要先写可视化大屏。今天也可用于修复D13阻塞项，未完成的基线不能标绿。

**求职：** 把岗位要求和代码证据对照一遍，准备第15天首批真实项目描述。

### 本版锁定的固定输入 / 预期

两份原始输出各20题，每题都有状态；评分可追到qid。失败和无答案不能从分母中删除。

**评分文件的目标路径**为 `~/agent-study/repo-qa-agent/reports/d14/dev_scores.jsonl`，每个qid分别记录keyword与vector。原始JSONL只读不改。

## 5. 写完以后，运行哪些命令

**下面业务入口需要先完成本日骨架，首次NotImplementedError不是环境故障。**

```bash
cd "$HOME/agent-study/repo-qa-agent"
python -m scripts.evaluate --dataset "$HOME/agent-study/repo-qa-agent/data/dev.jsonl" --mode keyword --out "$HOME/agent-study/repo-qa-agent/reports/d14/keyword_raw.jsonl"
python -m scripts.evaluate --dataset "$HOME/agent-study/repo-qa-agent/data/dev.jsonl" --mode vector --out "$HOME/agent-study/repo-qa-agent/reports/d14/vector_raw.jsonl"
python -m scripts.score_report --scores "$HOME/agent-study/repo-qa-agent/reports/d14/dev_scores.jsonl" --out "$HOME/agent-study/repo-qa-agent/reports/d14/summary.json"
python "$HOME/agent-study/tools/check_day.py" 14
```

固定测试+已创建的过去测试输出：`~/agent-study/repo-qa-agent/reports/d14/unittest.txt`。当前算法测试输出：`~/agent-study/repo-qa-agent/reports/d14/algorithm.txt`。有意未做的集成验收不在此命令中冒充通过。

## 6. 算法也固定文件，不临时找题

本日题目：**二叉树层序遍历**。网页题目范围：[只看这道题的题面、输入输出和约束](https://leetcode.cn/problems/binary-tree-level-order-traversal/description/)；闭卷日不打开题解。

代码：`~/agent-study/repo-qa-agent/algorithms/d14_level_order.py`。测试：`~/agent-study/repo-qa-agent/algorithm_tests/test_d14_level_order.py`。记录：`~/agent-study/repo-qa-agent/notes/d14.md`。

本地统一接口：`solve(root) -> list[list[int]]`。最小输入：`None`；预期：`[]`。

运行：从 `~/agent-study/repo-qa-agent/` 执行 `python -m unittest algorithm_tests.test_d14_level_order -v`。再补2个不同边界；树/链表必须补至少一个非空正常输入，不能只有空输入测试。45分钟后记录真正卡点，不另外开新题。

## 7. 收工前确认

把“是否独立、失败原因、测试输出完整路径、仍未测项、下一次第一步”写入 `~/agent-study/repo-qa-agent/notes/d14.md`。把本日岗位/简历动作写入 `~/agent-study/repo-qa-agent/career/d14_action.md`；只有真实申请才更新 `~/agent-study/repo-qa-agent/career/applications.md`。

**绿灯：** 固定测试与自加边界符合预期，关键逻辑能解释并修改，业务产物真实生成；需要真实模型的学习日另有真实证据。**黄/红灯：** 在当前日卡定位未过函数，不翻页堆欠账。

路径不对先重新运行 `python "$HOME/agent-study/tools/start_day.py" 14` 看打印出的实际地址；它不会覆盖现有文件。模块找不到先确认终端根目录与解释器，不要盲目重装所有依赖。


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
