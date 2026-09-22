# D18｜查询API

**唯一项目根目录：** `~/agent-study/repo-qa-agent/`。今日任务卡：`~/agent-study/handbook/days/day18.md`。

## 1. 今天具体看哪个文件、读到哪里

|顺序|完整路径与准确范围|只抓住什么|
|---|---|---|
|1|`~/agent-study/materials/hello-agents/docs/chapter13/第十三章 智能旅行助手.md`<br>**L388–L412**<br>[打开固定版本相同行范围](https://github.com/datawhalechina/hello-agents/blob/b4aca1af44b7a492b4bfdec5aa100d556c65db54/docs/chapter13/%E7%AC%AC%E5%8D%81%E4%B8%89%E7%AB%A0%20%E6%99%BA%E8%83%BD%E6%97%85%E8%A1%8C%E5%8A%A9%E6%89%8B.md#L388-L412)|13.2.5：Pydantic请求/响应与FastAPI示例|
|2|`~/agent-study/materials/notes/18_fastapi.md`<br>**L1–L28**<br>本包已提供；本次补课讲义，不是教材原文。|D18 补课：最小API与错误码（本次补课讲义）|

**学到这里停：** 能说出今天目标函数接什么输入、返回什么、至少一个错误分支；接着按下表写代码。源码中的图像不需要下载，未指定内容本日不读。

## 2. 先准备文件，再动手

```bash
cd "$HOME/agent-study/repo-qa-agent"
python "$HOME/agent-study/tools/start_day.py" 18
python "$HOME/agent-study/tools/read_today.py" 18
```

自动生成的阅读页：`~/agent-study/handbook/readings/day18.html`；对应带行号文本：`~/agent-study/handbook/readings/day18.txt`。

## 3. 今天所有文件的完整路径

|动作|完整路径|你在这里做什么|
|---|---|---|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/agent_lab/api.py`|app、GET /health、POST /query和依赖注入|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/agent_lab/schemas.py`|QueryRequest/QueryResponse，禁额外字段|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/scripts/api_smoke.py`|HTTP访问本机服务并写出响应|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/tests/test_d18_api.py`|通过TestClient和假服务验证路由|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/algorithms/d18_permutations.py`|算法独立实现；闭卷日新文件不覆盖旧答案|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/algorithm_tests/test_d18_permutations.py`|已给最小样例，你另补2个有效边界|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/notes/d18.md`|今日复盘、算法用时、错误与下一步|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/career/d18_action.md`|今日求职动作与真实证据|
|修改既有文件|`~/agent-study/repo-qa-agent/agent_lab/service.py`|API与CLI复用；本地库访问先串行化|
|修改既有文件|`~/agent-study/repo-qa-agent/requirements.txt`|增加fastapi、uvicorn、httpx实际直接依赖|
|修改既有文件|`~/agent-study/repo-qa-agent/career/applications.md`|仅记录真实岗位资格、申请和反馈|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d18/http.json`|健康、正常查询、坏参数和超时结果|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d18/unittest.txt`|check_day.py自动保存主项目测试输出|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d18/algorithm.txt`|check_day.py自动保存算法测试输出|

**“新建一次”已由准备工具完成时，你只需要打开并填内容；不要删掉重建。报告初始状态NOT_DONE不是成绩。程序生成项没有实际运行结果前不要填写成功。**

## 4. 要写的接口、具体操作和停止标准

```text
create_app(query_fn=None) -> FastAPI
QueryRequest: question:str 去首尾空白后1..500字符；mode:keyword/vector/agent；extra=forbid
模块末尾 app=create_app()；导入模块不得直接发模型请求或下载模型。
```

**前置：** CLI业务逻辑稳定。

**步骤：** 新建`~/agent-study/repo-qa-agent/agent_lab/api.py`，定义QueryRequest(question,mode)和QueryResponse(answer,citations,status)。question去掉首尾空白后长度1–500；mode只允许keyword/vector/agent；额外字段禁止，避免以后偷偷从请求读user_id。定义GET /health和POST /query，业务调用复用CLI用的服务函数，不复制一个新Agent。

同步阻塞客户端先放在普通`def`路由中；不要只在函数前加async就认为非阻塞。依赖注入允许测试时替换模型/检索组件。教学演示先把本地存储访问串行化（可在服务层用一把锁），并在同一工作线程内创建、使用、关闭Qdrant本地客户端；不要把CLI里创建的本地存储对象直接跨线程共享。当前语料很小，先接受重新打开的开销，不以此宣传并发性能。[异步说明][FAST_ASYNC]只查与此有关的一段。

**固定接口用例：** `{"question":"工具如何注册？","mode":"vector"}`返回200及约定字段；缺question、全空格、未知mode、超长输入返回请求校验错误；模拟模型超时按本项目约定返回504及脱敏提示。FastAPI默认请求校验通常为422，本作业采用默认行为并实测；教材13.2.5文字中写400，不将其当作本作业的预期值。[官方错误处理][FAST_ERRORS]

**验收：** 新建`~/agent-study/repo-qa-agent/tests/test_d18_api.py`，至少上述5类离线接口测试；运行**见本日运行区的完整命令**。启动约定**见本日运行区的完整命令**，浏览器打开/docs完成一次真实查询。交测试、接口输出和一次CLI/API结果对应记录。

**口述：** 请求模型约束参数，响应模型约束接口输出；HTTP层与业务层职责不同。当前本地服务不公开到互联网。

**卡住：** 先让/health返回ok，再让/query调用固定假回答，最后才接真实业务。端口冲突先换端口，不重装FastAPI。

**求职：** 用一页纸把目标岗位要求映射到CLI、RAG、API、测试四类代码证据。

### 本版锁定的固定输入 / 预期

health为200；好请求200；缺字段/空格/非法mode/超长默认422；模拟模型超时504。教材该处写400，本项目422来自官方补充与实测，不是默改教材。

## 5. 写完以后，运行哪些命令

**下面业务入口需要先完成本日骨架，首次NotImplementedError不是环境故障。**

```bash
cd "$HOME/agent-study/repo-qa-agent"
python -m pip install fastapi uvicorn httpx
python -m uvicorn agent_lab.api:app --host 127.0.0.1 --port 8000
# 上一行保持运行；在第二个已激活同一虚拟环境的终端执行：
python -m scripts.api_smoke --out "$HOME/agent-study/repo-qa-agent/reports/d18/http.json"
python "$HOME/agent-study/tools/check_day.py" 18
```

固定测试+已创建的过去测试输出：`~/agent-study/repo-qa-agent/reports/d18/unittest.txt`。当前算法测试输出：`~/agent-study/repo-qa-agent/reports/d18/algorithm.txt`。有意未做的集成验收不在此命令中冒充通过。

## 6. 算法也固定文件，不临时找题

本日题目：**全排列**。网页题目范围：[只看这道题的题面、输入输出和约束](https://leetcode.cn/problems/permutations/description/)；闭卷日不打开题解。

代码：`~/agent-study/repo-qa-agent/algorithms/d18_permutations.py`。测试：`~/agent-study/repo-qa-agent/algorithm_tests/test_d18_permutations.py`。记录：`~/agent-study/repo-qa-agent/notes/d18.md`。

本地统一接口：`solve(nums: list[int]) -> list[list[int]]`。最小输入：`[1]`；预期：`[[1]]`。

运行：从 `~/agent-study/repo-qa-agent/` 执行 `python -m unittest algorithm_tests.test_d18_permutations -v`。再补2个不同边界；树/链表必须补至少一个非空正常输入，不能只有空输入测试。45分钟后记录真正卡点，不另外开新题。

## 7. 收工前确认

把“是否独立、失败原因、测试输出完整路径、仍未测项、下一次第一步”写入 `~/agent-study/repo-qa-agent/notes/d18.md`。把本日岗位/简历动作写入 `~/agent-study/repo-qa-agent/career/d18_action.md`；只有真实申请才更新 `~/agent-study/repo-qa-agent/career/applications.md`。

**绿灯：** 固定测试与自加边界符合预期，关键逻辑能解释并修改，业务产物真实生成；需要真实模型的学习日另有真实证据。**黄/红灯：** 在当前日卡定位未过函数，不翻页堆欠账。

路径不对先重新运行 `python "$HOME/agent-study/tools/start_day.py" 18` 看打印出的实际地址；它不会覆盖现有文件。模块找不到先确认终端根目录与解释器，不要盲目重装所有依赖。


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
