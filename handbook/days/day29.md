# D29｜简历与讲解证据

**唯一项目根目录：** `~/agent-study/repo-qa-agent/`。今日任务卡：`~/agent-study/handbook/days/day29.md`。

## 1. 今天具体看哪个文件、读到哪里

|顺序|完整路径与准确范围|只抓住什么|
|---|---|---|
|1|`~/agent-study/materials/notes/29_interview.md`<br>**L1–L20**<br>本包已提供；本次补课讲义，不是教材原文。|D29 补课：每个关键词对应一份证据（本次补课讲义）|

**学到这里停：** 能说出今天目标函数接什么输入、返回什么、至少一个错误分支；接着按下表写代码。源码中的图像不需要下载，未指定内容本日不读。

## 2. 先准备文件，再动手

```bash
cd "$HOME/agent-study/repo-qa-agent"
python "$HOME/agent-study/tools/start_day.py" 29
python "$HOME/agent-study/tools/read_today.py" 29
```

自动生成的阅读页：`~/agent-study/handbook/readings/day29.html`；对应带行号文本：`~/agent-study/handbook/readings/day29.txt`。

## 3. 今天所有文件的完整路径

|动作|完整路径|你在这里做什么|
|---|---|---|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/career/resume_v02.md`|一页真实简历的文字稿|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/career/project_story.md`|五分钟讲解逐段提纲|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/career/evidence_map.md`|每个简历关键词→具体代码与报告路径|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/scripts/d29_change_request.py`|独立改动练习：把工具预算变成参数|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/algorithms/d29_islands_mock.py`|算法独立实现；闭卷日新文件不覆盖旧答案|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/algorithm_tests/test_d29_islands_mock.py`|已给最小样例，你另补2个有效边界|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/notes/d29.md`|今日复盘、算法用时、错误与下一步|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/career/d29_action.md`|今日求职动作与真实证据|
|修改既有文件|`~/agent-study/repo-qa-agent/agent_lab/budget.py`|独立实现本日指定的预算变更|
|修改既有文件|`~/agent-study/repo-qa-agent/agent_lab/qa_agent.py`|接入预算变更，沿用现有Agent而不是复制实现|
|修改既有文件|`~/agent-study/repo-qa-agent/career/applications.md`|核验2个目标岗位的硬条件及简历版本|
|修改既有文件|`~/agent-study/repo-qa-agent/README.md`|删除不能解释或没验证的关键词|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d29/project_story.mp4`|5分钟讲解录屏/录像|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d29/change_request.txt`|独立编码用时、命令、结果和是否看提示|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d29/unittest.txt`|check_day.py自动保存主项目测试输出|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d29/algorithm.txt`|check_day.py自动保存算法测试输出|

**“新建一次”已由准备工具完成时，你只需要打开并填内容；不要删掉重建。报告初始状态NOT_DONE不是成绩。程序生成项没有实际运行结果前不要填写成功。**

## 4. 要写的接口、具体操作和停止标准

```text
修改点必须指向 agent_lab/budget.py 和 agent_lab/qa_agent.py；不再另开业务项目。
```

**步骤：** 写一页简历：教育/毕业年月/到岗条件；实际技能；一项已有CRUD经历；一个Agent主项目。每条项目描述只放“做了什么→为何这样做→证据”。参考模板：

> 基于Hello-Agents学习并实现限定公开语料问答Agent，支持[已完成功能]；保留原文定位并限制[实际调用预算]。
>
> 构建20道开发题及10道留出题，对比[实际运行方案]；在固定语料/模型下记录[实测指标与分母]，分析[真实失败类别]。
>
> 使用FastAPI/SQLite实现[实际能力]，通过[实际测试]，提供[已验证的复现方式]。

不够三条就写两条，不填示范百分比。单工具MCP与LangGraph练习是同一个项目的模块，不包装成两个业务系统。

**面试练习：** 录5分钟：问题与范围45秒、请求链路90秒、个人实现60秒、一次失败与实验90秒、局限15秒。再用20分钟随机选一个核心函数，不看实现重写或完成小改动，如工具次数由固定值改为参数、读不到chunk如何结束。

**验收：** 简历每个关键词能定位代码或报告；能指出教程复用与个人新增边界；讲不出的关键词删除。请自己对照附录C的六个问题录音评分：有代码位置、因果解释、证据/边界各1分，每题至少2分；这只是本课程口述门槛，不是公司面试标准。

**卡住：** 不背新“八股”，回到一个具体请求，用函数名把路径走完。讲“为什么用了某技术”时必须给自己的问题，而不是“大家都用”。

**求职：** 针对2个资格匹配的岗位检查语言、方向、出勤和链接；准备定向版本。岗位数量不作为过关硬指标。

### 本版锁定的固定输入 / 预期

每个关键词至少对应一个代码或实验路径；无法解释即删除。没有证据的指标不填。

## 5. 写完以后，运行哪些命令

**下面业务入口需要先完成本日骨架，首次NotImplementedError不是环境故障。**

```bash
cd "$HOME/agent-study/repo-qa-agent"
python -m scripts.d29_change_request --out "$HOME/agent-study/repo-qa-agent/reports/d29/change_request.txt"
python "$HOME/agent-study/tools/check_day.py" 29
```

固定测试+已创建的过去测试输出：`~/agent-study/repo-qa-agent/reports/d29/unittest.txt`。当前算法测试输出：`~/agent-study/repo-qa-agent/reports/d29/algorithm.txt`。有意未做的集成验收不在此命令中冒充通过。

## 6. 算法也固定文件，不临时找题

本日题目：**模拟：岛屿数量**。网页题目范围：[只看这道题的题面、输入输出和约束](https://leetcode.cn/problems/number-of-islands/description/)；闭卷日不打开题解。

代码：`~/agent-study/repo-qa-agent/algorithms/d29_islands_mock.py`。测试：`~/agent-study/repo-qa-agent/algorithm_tests/test_d29_islands_mock.py`。记录：`~/agent-study/repo-qa-agent/notes/d29.md`。

本地统一接口：`solve(grid: list[list[str]]) -> int`。最小输入：`[["1","1"],["1","1"]]`；预期：`1`。

运行：从 `~/agent-study/repo-qa-agent/` 执行 `python -m unittest algorithm_tests.test_d29_islands_mock -v`。再补2个不同边界；树/链表必须补至少一个非空正常输入，不能只有空输入测试。45分钟后记录真正卡点，不另外开新题。

## 7. 收工前确认

把“是否独立、失败原因、测试输出完整路径、仍未测项、下一次第一步”写入 `~/agent-study/repo-qa-agent/notes/d29.md`。把本日岗位/简历动作写入 `~/agent-study/repo-qa-agent/career/d29_action.md`；只有真实申请才更新 `~/agent-study/repo-qa-agent/career/applications.md`。

**绿灯：** 固定测试与自加边界符合预期，关键逻辑能解释并修改，业务产物真实生成；需要真实模型的学习日另有真实证据。**黄/红灯：** 在当前日卡定位未过函数，不翻页堆欠账。

路径不对先重新运行 `python "$HOME/agent-study/tools/start_day.py" 29` 看打印出的实际地址；它不会覆盖现有文件。模块找不到先确认终端根目录与解释器，不要盲目重装所有依赖。


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
