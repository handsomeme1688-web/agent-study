# D10｜开发与留出题集

**唯一项目根目录：** `~/agent-study/repo-qa-agent/`。今日任务卡：`~/agent-study/handbook/days/day10.md`。

## 1. 今天具体看哪个文件、读到哪里

|顺序|完整路径与准确范围|只抓住什么|
|---|---|---|
|1|`~/agent-study/materials/hello-agents/docs/chapter12/第十二章 智能体性能评估.md`<br>**L11–L52**<br>[打开固定版本相同行范围](https://github.com/datawhalechina/hello-agents/blob/b4aca1af44b7a492b4bfdec5aa100d556c65db54/docs/chapter12/%E7%AC%AC%E5%8D%81%E4%BA%8C%E7%AB%A0%20%E6%99%BA%E8%83%BD%E4%BD%93%E6%80%A7%E8%83%BD%E8%AF%84%E4%BC%B0.md#L11-L52)|为何需要评估及输出不确定性|
|2|`~/agent-study/materials/hello-agents/docs/chapter12/第十二章 智能体性能评估.md`<br>**L81–L109**<br>[打开固定版本相同行范围](https://github.com/datawhalechina/hello-agents/blob/b4aca1af44b7a492b4bfdec5aa100d556c65db54/docs/chapter12/%E7%AC%AC%E5%8D%81%E4%BA%8C%E7%AB%A0%20%E6%99%BA%E8%83%BD%E4%BD%93%E6%80%A7%E8%83%BD%E8%AF%84%E4%BC%B0.md#L81-L109)|指标及评估体系设计|
|3|`~/agent-study/materials/notes/10_evaluation.md`<br>**L1–L31**<br>本包已提供；本次补课讲义，不是教材原文。|评测补课：题目、原始输出与人工分数（本次补课讲义）|

**学到这里停：** 能说出今天目标函数接什么输入、返回什么、至少一个错误分支；接着按下表写代码。源码中的图像不需要下载，未指定内容本日不读。

## 2. 先准备文件，再动手

```bash
cd "$HOME/agent-study/repo-qa-agent"
python "$HOME/agent-study/tools/start_day.py" 10
python "$HOME/agent-study/tools/read_today.py" 10
```

自动生成的阅读页：`~/agent-study/handbook/readings/day10.html`；对应带行号文本：`~/agent-study/handbook/readings/day10.txt`。

## 3. 今天所有文件的完整路径

|动作|完整路径|你在这里做什么|
|---|---|---|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/data/dev.jsonl`|20道开发题，12单片段/4跨片段/4无答案|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/data/holdout.jsonl`|10道留出题，6/2/2；先人工核证，D22再跑模型|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/scripts/check_dataset.py`|检查字段、数量、ID、原文证据范围|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/tests/test_d10_dataset.py`|题集结构与逻辑约束测试|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/reports/d10/dataset_audit.md`|5题人工抽检、划分规则和冻结摘要|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/algorithms/d10_binary_search.py`|算法独立实现；闭卷日新文件不覆盖旧答案|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/algorithm_tests/test_d10_binary_search.py`|已给最小样例，你另补2个有效边界|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/notes/d10.md`|今日复盘、算法用时、错误与下一步|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/career/d10_action.md`|今日求职动作与真实证据|
|修改既有文件|`~/agent-study/repo-qa-agent/data/source_manifest.json`|只核证，不随意扩语料|
|修改既有文件|`~/agent-study/repo-qa-agent/career/applications.md`|仅记录真实岗位资格、申请和反馈|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d10/dataset_check.json`|数量、字段、摘要检查输出|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d10/unittest.txt`|check_day.py自动保存主项目测试输出|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d10/algorithm.txt`|check_day.py自动保存算法测试输出|

**“新建一次”已由准备工具完成时，你只需要打开并填内容；不要删掉重建。报告初始状态NOT_DONE不是成绩。程序生成项没有实际运行结果前不要填写成功。**

## 4. 要写的接口、具体操作和停止标准

```text
validate_dataset(rows: list[dict], split: str) -> list[str]
此函数放在 scripts/check_dataset.py；返回空列表表示没有结构错误，不表示答案事实已人工核对。
```

**前置：** D9来源可定位。

**步骤：** 新建`~/agent-study/repo-qa-agent/data/dev.jsonl`20题与`~/agent-study/repo-qa-agent/data/holdout.jsonl`10题。开发题配比12单片段、4跨片段、4无答案；留出6/2/2。每题包含`qid/question/type/expected_points/gold_evidence/should_abstain`。gold_evidence是源路径、版本、行区间，不是只写某个chunk_id，避免以后改分块让标准答案失效。

先手工核对5题，再补齐。真实题干可从以下开始：ReAct代码何处限制最大步数？一次run开始时怎样处理历史？工具名不存在时的分支在哪？消息类与工具注册分别解决什么问题？不要预设系统已支持教材没有写出的能力。无答案题可以问“这份限定语料有没有给出本项目的生产QPS实测数值”，标准行为是说明当前材料不足，不是断言世界上没有。

**验收：** 新建`~/agent-study/repo-qa-agent/tests/test_d10_dataset.py`验证30个ID唯一、配比正确、可回答题有证据、无答案题不伪造证据。人工抽5题逐一核事实；至少1跨片段题有两处不同证据。保存数据集摘要；从今天起不根据留出题上的模型输出改系统，D22才统一跑留出。

**通过线：** 不是“写了30句问题”，而是30题各有评分规则；任何一题你自己无法根据原文判分，就先改题。自己出的留出集不是外部独立评测，也不代表真实用户分布。

**口述：** 开发集用于选择方案；留出用于冻结后检查。只换同义说法的题不得拆到两边。不要让AI直接批量编标准答案而不核原文。

**求职：** 把简历技能分成“实现过/实验过/只读过”三栏，本日不增加投递数量指标。

### 本版锁定的固定输入 / 预期

30个ID唯一、配比正确；可答题有人工证据；无答案题证据列表为空。禁止写占位行号充当核证。

## 5. 写完以后，运行哪些命令

**下面业务入口需要先完成本日骨架，首次NotImplementedError不是环境故障。**

```bash
cd "$HOME/agent-study/repo-qa-agent"
python -m scripts.check_dataset --dev "$HOME/agent-study/repo-qa-agent/data/dev.jsonl" --holdout "$HOME/agent-study/repo-qa-agent/data/holdout.jsonl" --out "$HOME/agent-study/repo-qa-agent/reports/d10/dataset_check.json"
python "$HOME/agent-study/tools/check_day.py" 10
```

固定测试+已创建的过去测试输出：`~/agent-study/repo-qa-agent/reports/d10/unittest.txt`。当前算法测试输出：`~/agent-study/repo-qa-agent/reports/d10/algorithm.txt`。有意未做的集成验收不在此命令中冒充通过。

## 6. 算法也固定文件，不临时找题

本日题目：**二分查找**。网页题目范围：[只看这道题的题面、输入输出和约束](https://leetcode.cn/problems/binary-search/description/)；闭卷日不打开题解。

代码：`~/agent-study/repo-qa-agent/algorithms/d10_binary_search.py`。测试：`~/agent-study/repo-qa-agent/algorithm_tests/test_d10_binary_search.py`。记录：`~/agent-study/repo-qa-agent/notes/d10.md`。

本地统一接口：`solve(nums: list[int], target: int) -> int`。最小输入：`[-1,0,3,5,9,12], 9`；预期：`4`。

运行：从 `~/agent-study/repo-qa-agent/` 执行 `python -m unittest algorithm_tests.test_d10_binary_search -v`。再补2个不同边界；树/链表必须补至少一个非空正常输入，不能只有空输入测试。45分钟后记录真正卡点，不另外开新题。

## 7. 收工前确认

把“是否独立、失败原因、测试输出完整路径、仍未测项、下一次第一步”写入 `~/agent-study/repo-qa-agent/notes/d10.md`。把本日岗位/简历动作写入 `~/agent-study/repo-qa-agent/career/d10_action.md`；只有真实申请才更新 `~/agent-study/repo-qa-agent/career/applications.md`。

**绿灯：** 固定测试与自加边界符合预期，关键逻辑能解释并修改，业务产物真实生成；需要真实模型的学习日另有真实证据。**黄/红灯：** 在当前日卡定位未过函数，不翻页堆欠账。

路径不对先重新运行 `python "$HOME/agent-study/tools/start_day.py" 10` 看打印出的实际地址；它不会覆盖现有文件。模块找不到先确认终端根目录与解释器，不要盲目重装所有依赖。


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
