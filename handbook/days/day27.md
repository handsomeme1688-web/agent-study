# D27｜无密钥CI

**唯一项目根目录：** `~/agent-study/repo-qa-agent/`。今日任务卡：`~/agent-study/handbook/days/day27.md`。

## 1. 今天具体看哪个文件、读到哪里

|顺序|完整路径与准确范围|只抓住什么|
|---|---|---|
|1|`~/agent-study/materials/notes/27_ci.md`<br>**L1–L21**<br>本包已提供；本次补课讲义，不是教材原文。|D27 补课：CI只运行它能验证的事（本次补课讲义）|

**学到这里停：** 能说出今天目标函数接什么输入、返回什么、至少一个错误分支；接着按下表写代码。源码中的图像不需要下载，未指定内容本日不读。

## 2. 先准备文件，再动手

```bash
cd "$HOME/agent-study/repo-qa-agent"
python "$HOME/agent-study/tools/start_day.py" 27
python "$HOME/agent-study/tools/read_today.py" 27
```

自动生成的阅读页：`~/agent-study/handbook/readings/day27.html`；对应带行号文本：`~/agent-study/handbook/readings/day27.txt`。

## 3. 今天所有文件的完整路径

|动作|完整路径|你在这里做什么|
|---|---|---|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/.github/workflows/tests.yml`|push/PR时安装测试依赖并运行离线测试|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/requirements-test.txt`|离线工程测试实际最小依赖|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/reports/d27/ci.md`|本机离线与远端Actions分栏|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/algorithms/d27_binary_search_review.py`|算法独立实现；闭卷日新文件不覆盖旧答案|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/algorithm_tests/test_d27_binary_search_review.py`|已给最小样例，你另补2个有效边界|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/notes/d27.md`|今日复盘、算法用时、错误与下一步|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/career/d27_action.md`|今日求职动作与真实证据|
|修改既有文件|`~/agent-study/repo-qa-agent/tests/test_d25_graph.py`|未做选修时不要伪造通过；CI显式说明覆盖范围|
|修改既有文件|`~/agent-study/repo-qa-agent/README.md`|离线/集成测试各自运行命令|
|修改既有文件|`~/agent-study/repo-qa-agent/career/applications.md`|仅记录真实岗位资格、申请和反馈|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d27/ci_url.txt`|自己实际远端run链接；未执行写NOT_RUN|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d27/unittest.txt`|check_day.py自动保存主项目测试输出|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d27/algorithm.txt`|check_day.py自动保存算法测试输出|

**“新建一次”已由准备工具完成时，你只需要打开并填内容；不要删掉重建。报告初始状态NOT_DONE不是成绩。程序生成项没有实际运行结果前不要填写成功。**

## 4. 要写的接口、具体操作和停止标准

```text
普通tests目录不得要求真实API密钥或自动下载Embedding。真实MCP协议测试保持在integration_tests。
```

**前置：** 本地关键测试可运行。

**步骤：** 明确测试分层：普通unittest只用fake模型、临时文件/数据库，不下载Embedding、不访问外部API；需要真实模型、MCP进程或Docker的测试列入集成范围。给需要外部条件的测试用标准库`unittest.skipUnless`显式标记，仅在`RUN_INTEGRATION=1`且对应条件齐备时运行，或移到单独integration_tests目录。

新建`~/agent-study/repo-qa-agent/.github/workflows/tests.yml`，在push/pull_request后使用你锁定的Python版本、安装最小测试依赖，执行**见本日运行区的完整命令**。服务层依赖用注入而不是导入模块时立即连接模型/创建大型索引。可另加格式检查，但不为格式工具迁移而改坏代码。

**验收：** 无API密钥的新环境能跑离线测试；故意破坏一个断言能让本地检查失败，恢复后通过；实际推送后查看一次CI运行结果。未推送就只能写“本地检查已通过，远端CI未验证”。报告区分passed与skipped，不能将跳过集成测试计作集成通过。

**交什么：** 工作流、测试依赖说明、一次真实CI结果链接/截图或明确未测状态；不要在工作流、测试日志或仓库Secrets操作截图中暴露密钥。

**口述：** 单元、集成、端到端各验证什么？CI不接真实模型还剩哪些价值、又不能证明什么？

**卡住：** 先让仅D1–D6测试在CI通过，再逐步加工程测试；不要为CI引入所有教程依赖。

**求职：** 简历只引用已经可访问的仓库/报告链接，检查公开仓库没有隐私资料。

### 本版锁定的固定输入 / 预期

人为破坏一个断言应使CI失败，恢复后再过；无远端运行链接时只能写本地通过。

## 5. 写完以后，运行哪些命令

**下面业务入口需要先完成本日骨架，首次NotImplementedError不是环境故障。**

```bash
cd "$HOME/agent-study/repo-qa-agent"
python -m unittest discover -s tests -v
python "$HOME/agent-study/tools/check_day.py" 27
```

固定测试+已创建的过去测试输出：`~/agent-study/repo-qa-agent/reports/d27/unittest.txt`。当前算法测试输出：`~/agent-study/repo-qa-agent/reports/d27/algorithm.txt`。有意未做的集成验收不在此命令中冒充通过。

## 6. 算法也固定文件，不临时找题

本日题目：**默认限时二分查找**。网页题目范围：[只看这道题的题面、输入输出和约束](https://leetcode.cn/problems/binary-search/description/)；闭卷日不打开题解。

代码：`~/agent-study/repo-qa-agent/algorithms/d27_binary_search_review.py`。测试：`~/agent-study/repo-qa-agent/algorithm_tests/test_d27_binary_search_review.py`。记录：`~/agent-study/repo-qa-agent/notes/d27.md`。

本地统一接口：`solve(nums: list[int], target: int) -> int`。最小输入：`[1,3,5], 5`；预期：`2`。

运行：从 `~/agent-study/repo-qa-agent/` 执行 `python -m unittest algorithm_tests.test_d27_binary_search_review -v`。再补2个不同边界；树/链表必须补至少一个非空正常输入，不能只有空输入测试。45分钟后记录真正卡点，不另外开新题。

## 7. 收工前确认

把“是否独立、失败原因、测试输出完整路径、仍未测项、下一次第一步”写入 `~/agent-study/repo-qa-agent/notes/d27.md`。把本日岗位/简历动作写入 `~/agent-study/repo-qa-agent/career/d27_action.md`；只有真实申请才更新 `~/agent-study/repo-qa-agent/career/applications.md`。

**绿灯：** 固定测试与自加边界符合预期，关键逻辑能解释并修改，业务产物真实生成；需要真实模型的学习日另有真实证据。**黄/红灯：** 在当前日卡定位未过函数，不翻页堆欠账。

路径不对先重新运行 `python "$HOME/agent-study/tools/start_day.py" 27` 看打印出的实际地址；它不会覆盖现有文件。模块找不到先确认终端根目录与解释器，不要盲目重装所有依赖。


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
