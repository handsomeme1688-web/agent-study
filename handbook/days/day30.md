# D30｜最终验收与下一轮

**唯一项目根目录：** `~/agent-study/repo-qa-agent/`。今日任务卡：`~/agent-study/handbook/days/day30.md`。

## 1. 今天具体看哪个文件、读到哪里

|顺序|完整路径与准确范围|只抓住什么|
|---|---|---|
|1|`~/agent-study/materials/notes/30_final.md`<br>**L1–L21**<br>本包已提供；本次补课讲义，不是教材原文。|D30 验收：四类证据一致（本次补课讲义）|

**学到这里停：** 能说出今天目标函数接什么输入、返回什么、至少一个错误分支；接着按下表写代码。源码中的图像不需要下载，未指定内容本日不读。

## 2. 先准备文件，再动手

```bash
cd "$HOME/agent-study/repo-qa-agent"
python "$HOME/agent-study/tools/start_day.py" 30
python "$HOME/agent-study/tools/read_today.py" 30
```

自动生成的阅读页：`~/agent-study/handbook/readings/day30.html`；对应带行号文本：`~/agent-study/handbook/readings/day30.txt`。

## 3. 今天所有文件的完整路径

|动作|完整路径|你在这里做什么|
|---|---|---|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/reports/d30/final_check.md`|代码/质量/交付/求职四类证据|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/career/resume_final.md`|提交用文字稿，保留版本号与日期|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/career/next_cycle.md`|只选下一轮最大短板|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/reports/d30/mock_interview.md`|完整模拟记录，不伪填通过|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/algorithms/d30_subarray_sum_mock.py`|算法独立实现；闭卷日新文件不覆盖旧答案|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/algorithm_tests/test_d30_subarray_sum_mock.py`|已给最小样例，你另补2个有效边界|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/notes/d30.md`|今日复盘、算法用时、错误与下一步|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/career/d30_action.md`|今日求职动作与真实证据|
|修改既有文件|`~/agent-study/repo-qa-agent/career/applications.md`|填真实申请状态，暂无反馈不等于拒绝|
|修改既有文件|`~/agent-study/repo-qa-agent/README.md`|最终功能与局限一致|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d30/demo_final.mp4`|最终演示文件或明确未录制|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d30/mock_interview.mp4`|完整模拟录像；不宜分享时本机保存|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d30/unittest.txt`|check_day.py自动保存主项目测试输出|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d30/algorithm.txt`|check_day.py自动保存算法测试输出|

**“新建一次”已由准备工具完成时，你只需要打开并填内容；不要删掉重建。报告初始状态NOT_DONE不是成绩。程序生成项没有实际运行结果前不要填写成功。**

## 4. 要写的接口、具体操作和停止标准

```text
不新增业务模块；终测仍使用实际现有模块和测试。
```

**今天不追新章节。** 按D28说明再走一遍；检查项目、报告、简历内容一致。做一次完整模拟：5分钟项目介绍、15分钟项目追问、30分钟算法/编码、10分钟复盘。卡住时记录事实，不临时宣称掌握未实践技术。

**毕业门槛分四张票：**

- 代码票：核心读写、检索、工具调用、上限、API、持久化与会话权限可解释，关键回归通过。
- 质量票：20开发题、10留出题有原文依据、原始结果与诚实评分；真实集成和mock分开记录。
- 交付票：干净环境复现、README、演示、来源标注和已知局限可访问；缺少Docker/MCP时如实注明。
- 求职票：一页真实简历，个人资格与出勤明确，至少对符合条件的岗位启动投递或记录为何当前暂无合适岗位。

这些票不能用“看完全书”代替，也不保证实习录取。LangGraph不是必需票；未完成的真实集成、核心权限或质量评测不能由框架数量抵消。

**交什么：** `~/agent-study/repo-qa-agent/reports/d30/final_check.md`，逐项证据链接；简历版本号；投递记录；下一轮唯一重点。

**下一轮选择：** 算法笔试薄弱就用接下来10个学习单元补哈希/树图/动态规划与限时输入输出；项目追问答不深就重做一个失败实验和一次独立实现；目标Python后端岗位要求更完整数据库能力时，再补关系库/索引/事务和并发。只有明确投模型算法方向，才另开ML/PyTorch/训练主线。不因一次拒绝重头读教程，也不同时开启三条补课路线。

**最后口述：** 用90秒回答“你现在能独立做什么，不能做什么，下一个最重要的改进是什么？”能把边界说清楚，就是本轮学习的真实产出。


---

### 本版锁定的固定输入 / 预期

代码、评测、演示、简历内容一致；真实模型与离线测试分栏；没有完成的MCP/Docker等如实写未测。

## 5. 写完以后，运行哪些命令

**下面业务入口需要先完成本日骨架，首次NotImplementedError不是环境故障。**

```bash
cd "$HOME/agent-study/repo-qa-agent"
python -m unittest discover -s tests -v
python "$HOME/agent-study/tools/check_day.py" 30
```

固定测试+已创建的过去测试输出：`~/agent-study/repo-qa-agent/reports/d30/unittest.txt`。当前算法测试输出：`~/agent-study/repo-qa-agent/reports/d30/algorithm.txt`。有意未做的集成验收不在此命令中冒充通过。

## 6. 算法也固定文件，不临时找题

本日题目：**模拟：前缀和**。网页题目范围：[只看这道题的题面、输入输出和约束](https://leetcode.cn/problems/subarray-sum-equals-k/description/)；闭卷日不打开题解。

代码：`~/agent-study/repo-qa-agent/algorithms/d30_subarray_sum_mock.py`。测试：`~/agent-study/repo-qa-agent/algorithm_tests/test_d30_subarray_sum_mock.py`。记录：`~/agent-study/repo-qa-agent/notes/d30.md`。

本地统一接口：`solve(nums: list[int], k: int) -> int`。最小输入：`[1,2,3], 3`；预期：`2`。

运行：从 `~/agent-study/repo-qa-agent/` 执行 `python -m unittest algorithm_tests.test_d30_subarray_sum_mock -v`。再补2个不同边界；树/链表必须补至少一个非空正常输入，不能只有空输入测试。45分钟后记录真正卡点，不另外开新题。

## 7. 收工前确认

把“是否独立、失败原因、测试输出完整路径、仍未测项、下一次第一步”写入 `~/agent-study/repo-qa-agent/notes/d30.md`。把本日岗位/简历动作写入 `~/agent-study/repo-qa-agent/career/d30_action.md`；只有真实申请才更新 `~/agent-study/repo-qa-agent/career/applications.md`。

**绿灯：** 固定测试与自加边界符合预期，关键逻辑能解释并修改，业务产物真实生成；需要真实模型的学习日另有真实证据。**黄/红灯：** 在当前日卡定位未过函数，不翻页堆欠账。

路径不对先重新运行 `python "$HOME/agent-study/tools/start_day.py" 30` 看打印出的实际地址；它不会覆盖现有文件。模块找不到先确认终端根目录与解释器，不要盲目重装所有依赖。


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
