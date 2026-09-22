# D20｜两用户会话权限

**唯一项目根目录：** `~/agent-study/repo-qa-agent/`。今日任务卡：`~/agent-study/handbook/days/day20.md`。

## 1. 今天具体看哪个文件、读到哪里

|顺序|完整路径与准确范围|只抓住什么|
|---|---|---|
|1|`~/agent-study/materials/notes/20_auth.md`<br>**L1–L23**<br>本包已提供；本次补课讲义，不是教材原文。|D20 补课：服务端身份与归属（本次补课讲义）|

**学到这里停：** 能说出今天目标函数接什么输入、返回什么、至少一个错误分支；接着按下表写代码。源码中的图像不需要下载，未指定内容本日不读。

## 2. 先准备文件，再动手

```bash
cd "$HOME/agent-study/repo-qa-agent"
python "$HOME/agent-study/tools/start_day.py" 20
python "$HOME/agent-study/tools/read_today.py" 20
```

自动生成的阅读页：`~/agent-study/handbook/readings/day20.html`；对应带行号文本：`~/agent-study/handbook/readings/day20.txt`。

## 3. 今天所有文件的完整路径

|动作|完整路径|你在这里做什么|
|---|---|---|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/agent_lab/auth.py`|Bearer凭据映射身份及会话owner检查|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/scripts/auth_smoke.py`|A/B三条越权与两条合法HTTP请求|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/tests/test_d20_auth.py`|缺凭据、坏凭据、越权读/查/写、额外user_id|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/algorithms/d20_top_k.py`|算法独立实现；闭卷日新文件不覆盖旧答案|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/algorithm_tests/test_d20_top_k.py`|已给最小样例，你另补2个有效边界|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/notes/d20.md`|今日复盘、算法用时、错误与下一步|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/career/d20_action.md`|今日求职动作与真实证据|
|修改既有文件|`~/agent-study/repo-qa-agent/.env`|本机填写DEMO_TOKEN_A、DEMO_TOKEN_B；不写入代码|
|修改既有文件|`~/agent-study/repo-qa-agent/.env.example`|新增上述空变量名，不填值|
|修改既有文件|`~/agent-study/repo-qa-agent/agent_lab/api.py`|创建、读取、带session查询都接入身份及归属校验|
|修改既有文件|`~/agent-study/repo-qa-agent/agent_lab/storage.py`|写前再次检查session归属，避免遗漏入口|
|修改既有文件|`~/agent-study/repo-qa-agent/career/applications.md`|仅记录真实岗位资格、申请和反馈|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d20/isolation.json`|脱敏A/B验收；不含任何token|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d20/unittest.txt`|check_day.py自动保存主项目测试输出|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d20/algorithm.txt`|check_day.py自动保存算法测试输出|

**“新建一次”已由准备工具完成时，你只需要打开并填内容；不要删掉重建。报告初始状态NOT_DONE不是成绩。程序生成项没有实际运行结果前不要填写成功。**

## 4. 要写的接口、具体操作和停止标准

```text
resolve_identity(token: str, token_to_user: dict[str,str]) -> str
require_owner(actual_owner: str | None, requester: str) -> None
invalid token=401；无权或不存在会话统一404；extra user_id=422。
```

**前置：** D19读写稳定。

**步骤：** 在本地环境配置两枚测试token到两个服务端身份A/B的映射，不提交真实token。鉴权依赖从Authorization头解析token并查服务端映射；不能信任请求里的user_id。创建会话自动绑定身份；读会话、带session_id查询、追加消息都先检查owner。对不存在或无权会话统一返回404，避免接口泄露存在性；缺少/非法凭据返回401，行为由你的依赖明确控制。

本项目语料是公开的，同一公开问题允许A/B都检索；这是**会话隔离**测试，不是私有文档多租户测试。read_chunk仍限登记公开片段，不能接受任意路径。未来需要私有资料时，再统一补入库、检索过滤、原文读取与缓存的权限边界。

**固定用例：** A建会话并写入标记`A_ONLY_731`；B用A的session_id读/查询/写入均失败；B正常创建自己的会话成功；请求JSON中加`user_id:'A'`按D18禁止额外字段规则拒绝。错误请求后A原消息不变。

**验收：** 新建`~/agent-study/repo-qa-agent/tests/test_d20_auth.py`，上述越权与正常路径全过。展示A/B两组API请求，而不是只读代码宣称“已隔离”。日志不含token，文档只描述本地演示凭据方案。

**口述：** 鉴权确认是谁，授权确认能访问什么；命名空间不自动等于安全边界。你实现的是演示级会话权限，不是生产身份平台。

**卡住：** 先在纯Python函数测试`require_owner`，再装进三个API入口；漏一个入口就不能过关。今天不把全部文档改为私有来扩大范围。

**求职：** 按简历写一句可验证工程能力：“增加两用户会话归属校验，覆盖读取/写入/查询越权用例”；未通过就不写。

### 本版锁定的固定输入 / 预期

A写A_ONLY_731，B读/查/写A的session都失败；B自己的会话成功；拒绝请求不改变A数据。只证明会话隔离。

## 5. 写完以后，运行哪些命令

**下面业务入口需要先完成本日骨架，首次NotImplementedError不是环境故障。**

```bash
cd "$HOME/agent-study/repo-qa-agent"
python -m scripts.auth_smoke --out "$HOME/agent-study/repo-qa-agent/reports/d20/isolation.json"
python "$HOME/agent-study/tools/check_day.py" 20
```

固定测试+已创建的过去测试输出：`~/agent-study/repo-qa-agent/reports/d20/unittest.txt`。当前算法测试输出：`~/agent-study/repo-qa-agent/reports/d20/algorithm.txt`。有意未做的集成验收不在此命令中冒充通过。

## 6. 算法也固定文件，不临时找题

本日题目：**前K高频元素**。网页题目范围：[只看这道题的题面、输入输出和约束](https://leetcode.cn/problems/top-k-frequent-elements/description/)；闭卷日不打开题解。

代码：`~/agent-study/repo-qa-agent/algorithms/d20_top_k.py`。测试：`~/agent-study/repo-qa-agent/algorithm_tests/test_d20_top_k.py`。记录：`~/agent-study/repo-qa-agent/notes/d20.md`。

本地统一接口：`solve(nums: list[int], k: int) -> list[int]`。最小输入：`[1,1,1,2,2,3], 2`；预期：`[1,2]`。

运行：从 `~/agent-study/repo-qa-agent/` 执行 `python -m unittest algorithm_tests.test_d20_top_k -v`。再补2个不同边界；树/链表必须补至少一个非空正常输入，不能只有空输入测试。45分钟后记录真正卡点，不另外开新题。

## 7. 收工前确认

把“是否独立、失败原因、测试输出完整路径、仍未测项、下一次第一步”写入 `~/agent-study/repo-qa-agent/notes/d20.md`。把本日岗位/简历动作写入 `~/agent-study/repo-qa-agent/career/d20_action.md`；只有真实申请才更新 `~/agent-study/repo-qa-agent/career/applications.md`。

**绿灯：** 固定测试与自加边界符合预期，关键逻辑能解释并修改，业务产物真实生成；需要真实模型的学习日另有真实证据。**黄/红灯：** 在当前日卡定位未过函数，不翻页堆欠账。

路径不对先重新运行 `python "$HOME/agent-study/tools/start_day.py" 20` 看打印出的实际地址；它不会覆盖现有文件。模块找不到先确认终端根目录与解释器，不要盲目重装所有依赖。


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
