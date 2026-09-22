# D04｜最小真实模型请求

**唯一项目根目录：** `~/agent-study/repo-qa-agent/`。今日任务卡：`~/agent-study/handbook/days/day04.md`。

## 1. 今天具体看哪个文件、读到哪里

|顺序|完整路径与准确范围|只抓住什么|
|---|---|---|
|1|`~/agent-study/materials/hello-agents/docs/chapter4/第四章 智能体经典范式构建.md`<br>**L29–L45**<br>[打开固定版本相同行范围](https://github.com/datawhalechina/hello-agents/blob/b4aca1af44b7a492b4bfdec5aa100d556c65db54/docs/chapter4/%E7%AC%AC%E5%9B%9B%E7%AB%A0%20%E6%99%BA%E8%83%BD%E4%BD%93%E7%BB%8F%E5%85%B8%E8%8C%83%E5%BC%8F%E6%9E%84%E5%BB%BA.md#L29-L45)|4.1.2：三个环境变量|
|2|`~/agent-study/materials/hello-agents/docs/chapter4/第四章 智能体经典范式构建.md`<br>**L47–L130**<br>[打开固定版本相同行范围](https://github.com/datawhalechina/hello-agents/blob/b4aca1af44b7a492b4bfdec5aa100d556c65db54/docs/chapter4/%E7%AC%AC%E5%9B%9B%E7%AB%A0%20%E6%99%BA%E8%83%BD%E4%BD%93%E7%BB%8F%E5%85%B8%E8%8C%83%E5%BC%8F%E6%9E%84%E5%BB%BA.md#L47-L130)|4.1.3：客户端、messages与请求响应|
|3|`~/agent-study/materials/notes/04_llm_client.md`<br>**L1–L28**<br>本包已提供；本次补课讲义，不是教材原文。|D04 补课：最小模型客户端（本次补课讲义）|
|最后|`~/agent-study/repo-qa-agent/tests/test_d04_config.py`<br>**L1–L20，读完整文件，不修改固定预期。**|先读每个测试名，再读输入和断言；这是当天作业的精确契约。|

**学到这里停：** 能说出今天目标函数接什么输入、返回什么、至少一个错误分支；接着按下表写代码。源码中的图像不需要下载，未指定内容本日不读。

## 2. 先准备文件，再动手

```bash
cd "$HOME/agent-study/repo-qa-agent"
python "$HOME/agent-study/tools/start_day.py" 4
python "$HOME/agent-study/tools/read_today.py" 4
```

自动生成的阅读页：`~/agent-study/handbook/readings/day04.html`；对应带行号文本：`~/agent-study/handbook/readings/day04.txt`。

## 3. 今天所有文件的完整路径

|动作|完整路径|你在这里做什么|
|---|---|---|
|只读：已提供|`~/agent-study/repo-qa-agent/tests/test_d04_config.py`|固定验收用例；不改预期值来刷绿。|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/.env`|由.env.example复制后填写，仅本机使用，永不提交|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/requirements.txt`|当天实际直接依赖|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/requirements.lock.txt`|pip freeze生成的实际安装版本|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/agent_lab/llm.py`|封装非流式模型调用，显式超时，关闭隐含重试|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/scripts/ask_once.py`|命令行接收一个问题，加载配置并调用客户端|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/tests/test_d04_extra.py`|补配置错误不得泄露密钥的测试|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/algorithms/d04_valid_parentheses_rewrite.py`|算法独立实现；闭卷日新文件不覆盖旧答案|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/algorithm_tests/test_d04_valid_parentheses_rewrite.py`|已给最小样例，你另补2个有效边界|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/notes/d04.md`|今日复盘、算法用时、错误与下一步|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/career/d04_action.md`|今日求职动作与真实证据|
|修改既有文件|`~/agent-study/repo-qa-agent/agent_lab/config.py`|已有骨架：完成get_config；不发网络请求|
|修改既有文件|`~/agent-study/repo-qa-agent/career/applications.md`|仅记录真实岗位资格、申请和反馈|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d04/live_call.json`|真实模型ID、日期、脱敏响应与是否成功|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d04/versions.txt`|解释器与SDK实际版本|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d04/unittest.txt`|check_day.py自动保存主项目测试输出|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d04/algorithm.txt`|check_day.py自动保存算法测试输出|

**“新建一次”已由准备工具完成时，你只需要打开并填内容；不要删掉重建。报告初始状态NOT_DONE不是成绩。程序生成项没有实际运行结果前不要填写成功。**

## 4. 要写的接口、具体操作和停止标准

```text
make_text_model(config: dict): 返回 model(messages: list[dict]) -> str
scripts.ask_once 接收位置参数 question 和 --out
```

**前置：** D1–D3过关，或至少离线作业稳定。

**步骤：** 完成`get_config(env)`并跑离线测试。然后新建`~/agent-study/repo-qa-agent/scripts/ask_once.py`和空`~/agent-study/repo-qa-agent/scripts/__init__.py`，按教材客户端写**非流式**请求，要求CLI接收一句问题并输出文本。只安装这个脚本用到的SDK及配置加载库，不安装整本教程。配置使用`~/agent-study/repo-qa-agent/.env.example`中的三个字段；程序显式加载`~/agent-study/repo-qa-agent/.env`或使用终端环境变量，再交给`get_config`，不要假定文件自动生效。

**功能输入：** **见本日运行区的完整命令**。提示词的内容正确与否不是联网成功唯一依据；保留成功响应、模型标识、时间及SDK版本，凭据必须删除。SDK调用设置有限网络超时，暂关闭自动重试以便观察错误；参数名按已安装SDK文档确认。

**验收：** **见本日运行区的完整命令**，3项全过；真实请求至少成功一次；清空模型名时在本地报缺字段，不进入网络调用。交脚本、脱敏输出、`~/agent-study/repo-qa-agent/requirements.txt`中的实际依赖版本。只有配置测试通过时，标“配置通过、真实API未测”，不能标整天绿灯。

**口述：** system/user消息各干什么；token不等于汉字数；温度不是“正确率旋钮”；SDK是调用接口的库，不是模型本身。

**卡住：** 缺配置先不发请求；401/403先核账户权限，404核模型名/服务地址，网络失败核连接与代理；不要循环随机换模型。没有可用账户先用固定响应推进离线作业，保留真实集成待补项。

**求职：** 写旧CRUD项目的一句事实：“我实际负责了__接口/表/功能”；没有的数据不补造。

### 本版锁定的固定输入 / 预期

3个配置固定测试全过+新增边界；至少一次真实HTTP成功。模型名空白应在本地报错，密钥值不得出现在异常或报告。

## 5. 写完以后，运行哪些命令

**下面业务入口需要先完成本日骨架，首次NotImplementedError不是环境故障。**

```bash
cd "$HOME/agent-study/repo-qa-agent"
python -m pip install openai python-dotenv
python -c "import pathlib, subprocess, sys; pathlib.Path.home().joinpath('agent-study/repo-qa-agent/requirements.lock.txt').write_bytes(subprocess.check_output([sys.executable, '-m', 'pip', 'freeze']))"
python -m scripts.ask_once "只回复：连接成功" --out "$HOME/agent-study/repo-qa-agent/reports/d04/live_call.json"
python "$HOME/agent-study/tools/check_day.py" 4
```

固定测试+已创建的过去测试输出：`~/agent-study/repo-qa-agent/reports/d04/unittest.txt`。当前算法测试输出：`~/agent-study/repo-qa-agent/reports/d04/algorithm.txt`。有意未做的集成验收不在此命令中冒充通过。

## 6. 算法也固定文件，不临时找题

本日题目：**有效括号闭卷**。网页题目范围：[只看这道题的题面、输入输出和约束](https://leetcode.cn/problems/valid-parentheses/description/)；闭卷日不打开题解。

代码：`~/agent-study/repo-qa-agent/algorithms/d04_valid_parentheses_rewrite.py`。测试：`~/agent-study/repo-qa-agent/algorithm_tests/test_d04_valid_parentheses_rewrite.py`。记录：`~/agent-study/repo-qa-agent/notes/d04.md`。

本地统一接口：`solve(s: str) -> bool`。最小输入：`"([)]"`；预期：`False`。

运行：从 `~/agent-study/repo-qa-agent/` 执行 `python -m unittest algorithm_tests.test_d04_valid_parentheses_rewrite -v`。再补2个不同边界；树/链表必须补至少一个非空正常输入，不能只有空输入测试。45分钟后记录真正卡点，不另外开新题。

## 7. 收工前确认

把“是否独立、失败原因、测试输出完整路径、仍未测项、下一次第一步”写入 `~/agent-study/repo-qa-agent/notes/d04.md`。把本日岗位/简历动作写入 `~/agent-study/repo-qa-agent/career/d04_action.md`；只有真实申请才更新 `~/agent-study/repo-qa-agent/career/applications.md`。

**绿灯：** 固定测试与自加边界符合预期，关键逻辑能解释并修改，业务产物真实生成；需要真实模型的学习日另有真实证据。**黄/红灯：** 在当前日卡定位未过函数，不翻页堆欠账。

路径不对先重新运行 `python "$HOME/agent-study/tools/start_day.py" 4` 看打印出的实际地址；它不会覆盖现有文件。模块找不到先确认终端根目录与解释器，不要盲目重装所有依赖。


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
