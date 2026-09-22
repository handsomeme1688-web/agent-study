# D24｜一个MCP只读工具

**唯一项目根目录：** `~/agent-study/repo-qa-agent/`。今日任务卡：`~/agent-study/handbook/days/day24.md`。

## 1. 今天具体看哪个文件、读到哪里

|顺序|完整路径与准确范围|只抓住什么|
|---|---|---|
|1|`~/agent-study/materials/hello-agents/code/chapter10/14_weather_mcp_server.py`<br>**L1–L12**<br>[打开固定版本相同行范围](https://github.com/datawhalechina/hello-agents/blob/b4aca1af44b7a492b4bfdec5aa100d556c65db54/code/chapter10/14_weather_mcp_server.py#L1-L12)|教程服务器创建方式|
|2|`~/agent-study/materials/hello-agents/code/chapter10/14_weather_mcp_server.py`<br>**L43–L76**<br>[打开固定版本相同行范围](https://github.com/datawhalechina/hello-agents/blob/b4aca1af44b7a492b4bfdec5aa100d556c65db54/code/chapter10/14_weather_mcp_server.py#L43-L76)|业务函数、工具注册与服务器入口|
|3|`~/agent-study/materials/notes/24_mcp.md`<br>**L1–L26**<br>本包已提供；本次补课讲义，不是教材原文。|D24 补课：服务器和真正客户端（本次补课讲义）|

**学到这里停：** 能说出今天目标函数接什么输入、返回什么、至少一个错误分支；接着按下表写代码。源码中的图像不需要下载，未指定内容本日不读。

## 2. 先准备文件，再动手

```bash
cd "$HOME/agent-study/repo-qa-agent"
python "$HOME/agent-study/tools/start_day.py" 24
python "$HOME/agent-study/tools/read_today.py" 24
```

自动生成的阅读页：`~/agent-study/handbook/readings/day24.html`；对应带行号文本：`~/agent-study/handbook/readings/day24.txt`。

## 3. 今天所有文件的完整路径

|动作|完整路径|你在这里做什么|
|---|---|---|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/agent_lab/mcp_server.py`|把已有公开检索工具包装为stdio MCP服务|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/scripts/mcp_smoke.py`|真实客户端启动子进程、发现、调用并关闭|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/integration_tests/test_d24_mcp.py`|真实进程协议测试，与普通单元测试分开|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/reports/d24/mcp.md`|SDK版本、原生调用和MCP的差异|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/algorithms/d24_coin_change.py`|算法独立实现；闭卷日新文件不覆盖旧答案|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/algorithm_tests/test_d24_coin_change.py`|已给最小样例，你另补2个有效边界|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/notes/d24.md`|今日复盘、算法用时、错误与下一步|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/career/d24_action.md`|今日求职动作与真实证据|
|修改既有文件|`~/agent-study/repo-qa-agent/requirements.txt`|记录实际MCP SDK版本；不要混用新旧客户端API|
|修改既有文件|`~/agent-study/repo-qa-agent/career/applications.md`|仅记录真实岗位资格、申请和反馈|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d24/mcp_result.json`|工具列表、正常调用、错误调用和退出状态|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d24/unittest.txt`|check_day.py自动保存主项目测试输出|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d24/algorithm.txt`|check_day.py自动保存算法测试输出|

**“新建一次”已由准备工具完成时，你只需要打开并填内容；不要删掉重建。报告初始状态NOT_DONE不是成绩。程序生成项没有实际运行结果前不要填写成功。**

## 4. 要写的接口、具体操作和停止标准

```text
检索业务仍复用 agent_lab/retrieval.py；MCP仅允许query/k，不接受路径或身份。
脚本必须以 sys.executable 和 -m agent_lab.mcp_server 启动子进程，cwd固定为项目根。
```

**前置：** D23核心通过；否则今天用于修复。

**步骤：** 在独立小脚本`~/agent-study/repo-qa-agent/agent_lab/mcp_server.py`中，使用当天锁定的Python SDK把现有`search_docs`包装为工具。参数只有query与k，内部复用已有检索服务。工具访问固定公开语料，不提供会话查询、任意路径、任意SQL或代码执行。不要另装天气数据源。

创建`~/agent-study/repo-qa-agent/scripts/mcp_smoke.py`作为真正客户端：启动stdio子进程，完成初始化、工具发现、工具调用，关闭连接。按官方示例管理客户端/子进程上下文；标准输出保留给协议数据，调试日志写标准错误。第一次工具调用可以先调用关键词检索，避免把Embedding加载错误误判为协议错误。

**固定用例：** 能在工具列表看到search_docs；query为“工具”获得含id/source的结果；k超界返回可解释的错误；未登记工具不可调用；客户端退出后子进程被正常清理。

**验收：** 保存客户端命令、工具列表、一次正常调用与一次错误结果。可建立`~/agent-study/repo-qa-agent/integration_tests/test_d24_mcp.py`集成测试，但不能只直接调用Python函数就称“完成MCP集成”。

**口述：** Host、Client、Server分别做什么？MCP让外部客户端如何发现并调用你的能力？模型原生Function Calling与MCP为何不是同一层？

**卡住：** 先运行官方最小加法工具，再把函数体替换为D3检索；协议失败与业务失败分开定位。今天不学A2A、ANP、远程鉴权或所有传输方式。此服务仅本机使用，不对互联网开放。

**求职：** 通过后只写“通过stdio客户端验证一个只读检索MCP工具”；不写“搭建生产级MCP平台”。

### 本版锁定的固定输入 / 预期

必须真实走协议发现/调用，直接调用函数不算。官方补充当前2.x示例与教程封装不同；依赖不兼容就标未测，不混装。

**本轮版本说明：** 教材使用HelloAgents封装，补课讲义采用所查官方2.x客户端形式。只借鉴职责，不把教程的MCPServer封装和官方Client强行混成同一个API。服务器/客户端实际协议验收仍需你在本机完成。

## 5. 写完以后，运行哪些命令

**下面业务入口需要先完成本日骨架，首次NotImplementedError不是环境故障。**

```bash
cd "$HOME/agent-study/repo-qa-agent"
python -m pip install "mcp>=2,<3"
python -m scripts.mcp_smoke --out "$HOME/agent-study/repo-qa-agent/reports/d24/mcp_result.json"
python -m unittest integration_tests.test_d24_mcp -v
python "$HOME/agent-study/tools/check_day.py" 24
```

固定测试+已创建的过去测试输出：`~/agent-study/repo-qa-agent/reports/d24/unittest.txt`。当前算法测试输出：`~/agent-study/repo-qa-agent/reports/d24/algorithm.txt`。有意未做的集成验收不在此命令中冒充通过。

## 6. 算法也固定文件，不临时找题

本日题目：**零钱兑换**。网页题目范围：[只看这道题的题面、输入输出和约束](https://leetcode.cn/problems/coin-change/description/)；闭卷日不打开题解。

代码：`~/agent-study/repo-qa-agent/algorithms/d24_coin_change.py`。测试：`~/agent-study/repo-qa-agent/algorithm_tests/test_d24_coin_change.py`。记录：`~/agent-study/repo-qa-agent/notes/d24.md`。

本地统一接口：`solve(coins: list[int], amount: int) -> int`。最小输入：`[1,2,5], 11`；预期：`3`。

运行：从 `~/agent-study/repo-qa-agent/` 执行 `python -m unittest algorithm_tests.test_d24_coin_change -v`。再补2个不同边界；树/链表必须补至少一个非空正常输入，不能只有空输入测试。45分钟后记录真正卡点，不另外开新题。

## 7. 收工前确认

把“是否独立、失败原因、测试输出完整路径、仍未测项、下一次第一步”写入 `~/agent-study/repo-qa-agent/notes/d24.md`。把本日岗位/简历动作写入 `~/agent-study/repo-qa-agent/career/d24_action.md`；只有真实申请才更新 `~/agent-study/repo-qa-agent/career/applications.md`。

**绿灯：** 固定测试与自加边界符合预期，关键逻辑能解释并修改，业务产物真实生成；需要真实模型的学习日另有真实证据。**黄/红灯：** 在当前日卡定位未过函数，不翻页堆欠账。

路径不对先重新运行 `python "$HOME/agent-study/tools/start_day.py" 24` 看打印出的实际地址；它不会覆盖现有文件。模块找不到先确认终端根目录与解释器，不要盲目重装所有依赖。


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
