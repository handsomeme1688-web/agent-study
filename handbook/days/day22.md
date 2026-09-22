# D22｜冻结与留出评测

**唯一项目根目录：** `~/agent-study/repo-qa-agent/`。今日任务卡：`~/agent-study/handbook/days/day22.md`。

## 1. 今天具体看哪个文件、读到哪里

|顺序|完整路径与准确范围|只抓住什么|
|---|---|---|
|1|`~/agent-study/materials/hello-agents/docs/chapter12/第十二章 智能体性能评估.md`<br>**L45–L52**<br>[打开固定版本相同行范围](https://github.com/datawhalechina/hello-agents/blob/b4aca1af44b7a492b4bfdec5aa100d556c65db54/docs/chapter12/%E7%AC%AC%E5%8D%81%E4%BA%8C%E7%AB%A0%20%E6%99%BA%E8%83%BD%E4%BD%93%E6%80%A7%E8%83%BD%E8%AF%84%E4%BC%B0.md#L45-L52)|评估挑战|
|2|`~/agent-study/materials/hello-agents/docs/chapter12/第十二章 智能体性能评估.md`<br>**L81–L109**<br>[打开固定版本相同行范围](https://github.com/datawhalechina/hello-agents/blob/b4aca1af44b7a492b4bfdec5aa100d556c65db54/docs/chapter12/%E7%AC%AC%E5%8D%81%E4%BA%8C%E7%AB%A0%20%E6%99%BA%E8%83%BD%E4%BD%93%E6%80%A7%E8%83%BD%E8%AF%84%E4%BC%B0.md#L81-L109)|评分指标与人工验证|
|3|`~/agent-study/materials/notes/22_holdout.md`<br>**L1–L21**<br>本包已提供；本次补课讲义，不是教材原文。|D22 补课：冻结后一次检查（本次补课讲义）|

**学到这里停：** 能说出今天目标函数接什么输入、返回什么、至少一个错误分支；接着按下表写代码。源码中的图像不需要下载，未指定内容本日不读。

## 2. 先准备文件，再动手

```bash
cd "$HOME/agent-study/repo-qa-agent"
python "$HOME/agent-study/tools/start_day.py" 22
python "$HOME/agent-study/tools/read_today.py" 22
```

自动生成的阅读页：`~/agent-study/handbook/readings/day22.html`；对应带行号文本：`~/agent-study/handbook/readings/day22.txt`。

## 3. 今天所有文件的完整路径

|动作|完整路径|你在这里做什么|
|---|---|---|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/data/final_config.json`|最终模型、语料、Embedding、k、提示摘要及预算|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/reports/d22/holdout_scores.jsonl`|10题×3方案的人工评分|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/reports/d22/holdout_report.md`|分母、原始结果路径和局限|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/algorithms/d22_house_robber.py`|算法独立实现；闭卷日新文件不覆盖旧答案|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/algorithm_tests/test_d22_house_robber.py`|已给最小样例，你另补2个有效边界|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/notes/d22.md`|今日复盘、算法用时、错误与下一步|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/career/d22_action.md`|今日求职动作与真实证据|
|修改既有文件|`~/agent-study/repo-qa-agent/scripts/evaluate.py`|只修阻止运行的bug，不根据留出调策略|
|修改既有文件|`~/agent-study/repo-qa-agent/scripts/score_report.py`|统一汇总三个方案|
|修改既有文件|`~/agent-study/repo-qa-agent/career/applications.md`|仅记录真实岗位资格、申请和反馈|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d22/keyword_raw.jsonl`|10题关键词结果|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d22/vector_raw.jsonl`|10题向量结果|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d22/agent_raw.jsonl`|10题Agent结果|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d22/summary.json`|三个方案的真实汇总|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d22/unittest.txt`|check_day.py自动保存主项目测试输出|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d22/algorithm.txt`|check_day.py自动保存算法测试输出|

**“新建一次”已由准备工具完成时，你只需要打开并填内容；不要删掉重建。报告初始状态NOT_DONE不是成绩。程序生成项没有实际运行结果前不要填写成功。**

## 4. 要写的接口、具体操作和停止标准

```text
不新增业务函数。已有evaluate读取 --config 与 --dataset；看到结果后改方案则必须标为已见复测。
```

**前置：** D17改动已有开发集对照，D21上限可验证。

**步骤：** 保存最终Git提交/配置摘要、语料版本、模型ID、Embedding版本与检索配置。用D10冻结的10道留出题，分别跑关键词RAG、向量RAG、最终Agent；三个方案共30条输出。相同问题与评分规则，保存失败和拒答，不能只保留成功输出。若真实调用费用或服务不可用，先保存配置并标“留出评测未完成”，不拿开发集替代。

逐题人工核对结论、证据、无答案处理。统计：8道可回答题的证据Recall@k；全部10题的任务成功；2道无答案题的正确拒答；引用支持与漏引；真实端到端延迟的样本数、中位数、范围。每种方案单独列分母；token缺失记未测。

**验收：** `~/agent-study/repo-qa-agent/reports/d22/agent_raw.jsonl`能逐条追溯到问题、配置与回答；`~/agent-study/repo-qa-agent/reports/d22/holdout_report.md`有三个方案对照、至少三个失败/局限分析。数字必须由保存的逐题记录重新算出。没有提升也过关，造指标或忽略失败不过关。

**重要边界：** 看完留出结果再修功能当然允许，但这10题从此是已见反馈；修后分数须标“看过测试后的复测”。需要新的泛化结论，就另建未用于改进的新题，不继续称其未见测试。

**口述：** 流程测试全过为什么不代表回答正确？小样本结果能说明什么，不能说明什么？

**卡住：** 先人工评完一题并解释每个评分字段，再批量执行；不要先接付费评测平台或用模型给自己打满分。

**求职：** 把简历中的“提升xx%”占位删除；只写你实际报告支持的数字及样本范围。

### 本版锁定的固定输入 / 预期

每方案10条均保存，开发与留出不混。无预算/无网络则写未测，不拿模拟输出当评测。

## 5. 写完以后，运行哪些命令

**下面业务入口需要先完成本日骨架，首次NotImplementedError不是环境故障。**

```bash
cd "$HOME/agent-study/repo-qa-agent"
python -m scripts.evaluate --dataset "$HOME/agent-study/repo-qa-agent/data/holdout.jsonl" --mode keyword --config "$HOME/agent-study/repo-qa-agent/data/final_config.json" --out "$HOME/agent-study/repo-qa-agent/reports/d22/keyword_raw.jsonl"
python -m scripts.evaluate --dataset "$HOME/agent-study/repo-qa-agent/data/holdout.jsonl" --mode vector --config "$HOME/agent-study/repo-qa-agent/data/final_config.json" --out "$HOME/agent-study/repo-qa-agent/reports/d22/vector_raw.jsonl"
python -m scripts.evaluate --dataset "$HOME/agent-study/repo-qa-agent/data/holdout.jsonl" --mode agent --config "$HOME/agent-study/repo-qa-agent/data/final_config.json" --out "$HOME/agent-study/repo-qa-agent/reports/d22/agent_raw.jsonl"
python "$HOME/agent-study/tools/check_day.py" 22
```

固定测试+已创建的过去测试输出：`~/agent-study/repo-qa-agent/reports/d22/unittest.txt`。当前算法测试输出：`~/agent-study/repo-qa-agent/reports/d22/algorithm.txt`。有意未做的集成验收不在此命令中冒充通过。

## 6. 算法也固定文件，不临时找题

本日题目：**打家劫舍**。网页题目范围：[只看这道题的题面、输入输出和约束](https://leetcode.cn/problems/house-robber/description/)；闭卷日不打开题解。

代码：`~/agent-study/repo-qa-agent/algorithms/d22_house_robber.py`。测试：`~/agent-study/repo-qa-agent/algorithm_tests/test_d22_house_robber.py`。记录：`~/agent-study/repo-qa-agent/notes/d22.md`。

本地统一接口：`solve(nums: list[int]) -> int`。最小输入：`[2,7,9,3,1]`；预期：`12`。

运行：从 `~/agent-study/repo-qa-agent/` 执行 `python -m unittest algorithm_tests.test_d22_house_robber -v`。再补2个不同边界；树/链表必须补至少一个非空正常输入，不能只有空输入测试。45分钟后记录真正卡点，不另外开新题。

## 7. 收工前确认

把“是否独立、失败原因、测试输出完整路径、仍未测项、下一次第一步”写入 `~/agent-study/repo-qa-agent/notes/d22.md`。把本日岗位/简历动作写入 `~/agent-study/repo-qa-agent/career/d22_action.md`；只有真实申请才更新 `~/agent-study/repo-qa-agent/career/applications.md`。

**绿灯：** 固定测试与自加边界符合预期，关键逻辑能解释并修改，业务产物真实生成；需要真实模型的学习日另有真实证据。**黄/红灯：** 在当前日卡定位未过函数，不翻页堆欠账。

路径不对先重新运行 `python "$HOME/agent-study/tools/start_day.py" 22` 看打印出的实际地址；它不会覆盖现有文件。模块找不到先确认终端根目录与解释器，不要盲目重装所有依赖。


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
