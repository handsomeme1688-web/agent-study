# D07｜第一关：真实工具闭环

**唯一项目根目录：** `~/agent-study/repo-qa-agent/`。今日任务卡：`~/agent-study/handbook/days/day07.md`。

## 1. 今天具体看哪个文件、读到哪里

|顺序|完整路径与准确范围|只抓住什么|
|---|---|---|
|1|`~/agent-study/materials/hello-agents/code/chapter4/ReAct.py`<br>**L32–L74**<br>[打开固定版本相同行范围](https://github.com/datawhalechina/hello-agents/blob/b4aca1af44b7a492b4bfdec5aa100d556c65db54/code/chapter4/ReAct.py#L32-L74)|复看主循环，定位与自己实现的差别|
|2|`~/agent-study/materials/notes/07_gate1.md`<br>**L1–L21**<br>本包已提供；本次补课讲义，不是教材原文。|D07 验收：两栏证据（本次补课讲义）|

**学到这里停：** 能说出今天目标函数接什么输入、返回什么、至少一个错误分支；接着按下表写代码。源码中的图像不需要下载，未指定内容本日不读。

## 2. 先准备文件，再动手

```bash
cd "$HOME/agent-study/repo-qa-agent"
python "$HOME/agent-study/tools/start_day.py" 7
python "$HOME/agent-study/tools/read_today.py" 7
```

自动生成的阅读页：`~/agent-study/handbook/readings/day07.html`；对应带行号文本：`~/agent-study/handbook/readings/day07.txt`。

## 3. 今天所有文件的完整路径

|动作|完整路径|你在这里做什么|
|---|---|---|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/prompts/agent_json.txt`|教学JSON协议系统提示，不冒充供应商原生协议|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/scripts/agent_smoke.py`|把真实模型、tools与loop连接|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/reports/d07/gate1.md`|逐项写离线/真实集成/未测结论|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/algorithms/d07_two_sum_review.py`|算法独立实现；闭卷日新文件不覆盖旧答案|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/algorithm_tests/test_d07_two_sum_review.py`|已给最小样例，你另补2个有效边界|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/notes/d07.md`|今日复盘、算法用时、错误与下一步|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/career/d07_action.md`|今日求职动作与真实证据|
|修改既有文件|`~/agent-study/repo-qa-agent/agent_lab/llm.py`|补转换为model(messages)->str的适配|
|修改既有文件|`~/agent-study/repo-qa-agent/agent_lab/loop.py`|只修回归失败，不增加新框架|
|修改既有文件|`~/agent-study/repo-qa-agent/README.md`|只列已完成能力|
|修改既有文件|`~/agent-study/repo-qa-agent/career/applications.md`|仅记录真实岗位资格、申请和反馈|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d07/live_agent.json`|真实模型发起工具、宿主执行和最终结束的轨迹|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d07/mock_demo.mp4`|录屏：明确标为离线假模型演示|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d07/unittest.txt`|check_day.py自动保存主项目测试输出|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d07/algorithm.txt`|check_day.py自动保存算法测试输出|

**“新建一次”已由准备工具完成时，你只需要打开并填内容；不要删掉重建。报告初始状态NOT_DONE不是成绩。程序生成项没有实际运行结果前不要填写成功。**

## 4. 要写的接口、具体操作和停止标准

```text
scripts.agent_smoke 接收 --question 与 --out；默认样例语料取workspace/d02/chunks.jsonl
```

**今天不增加新框架。学习：** 重看[第1章][H1]1.3.3及你前6天最弱的一个函数。

**步骤：** 运行**见本日运行区的完整命令**。把D4客户端包成`model(messages)->str`交给D6；通过system提示约束输出D5教学JSON。执行器复用D5，不在提示词里“模拟工具已经执行”。在mini.md上做三件事：问谁执行工具；明确要求读一个合法片段ID；问这份样例未包含的信息。

**验收分两栏：** ①38项固定离线测试全过，再加你自己写的边界测试；②至少留下一条真实模型发起工具、宿主确实执行、返回结果再结束的脱敏轨迹。若模型坏格式，应受控报错，不靠手工修输出冒充成功。空问题、未知工具、无穷调用脚本都按规则退出。

**独立考试：** 20分钟从空白重写“一个tool后final”的循环或D3检索函数，不能打开完整答案；可以查函数签名。口述模型和宿主分别承担什么；能说明当前只有关键词检索。

**交什么：** `~/agent-study/repo-qa-agent/reports/d07/gate1.md`写通过/失败/未测，附命令、输出和复现录屏。真实模型未通就保持“集成未通过”；下周不因账户阻塞而停掉离线数据准备，但D15必须补过。

**未过怎么排：** IO/分块不过回D1/2，检索不过回D3，参数不过回D5，循环不过回D6；不要重新从第一章通读。今天不计新技术量。

**求职：** 检查项目README只写已经完成的能力，放出可访问代码链接，排除.env和无关私人文件。

### 本版锁定的固定输入 / 预期

38个原固定测试与D1–D6自加测试通过；真实工具闭环另验，不能用离线通过替代。

## 5. 写完以后，运行哪些命令

**下面业务入口需要先完成本日骨架，首次NotImplementedError不是环境故障。**

```bash
cd "$HOME/agent-study/repo-qa-agent"
python -m scripts.agent_smoke --question "请先检索资料，再回答谁执行工具" --out "$HOME/agent-study/repo-qa-agent/reports/d07/live_agent.json"
python "$HOME/agent-study/tools/check_day.py" 7
```

固定测试+已创建的过去测试输出：`~/agent-study/repo-qa-agent/reports/d07/unittest.txt`。当前算法测试输出：`~/agent-study/repo-qa-agent/reports/d07/algorithm.txt`。有意未做的集成验收不在此命令中冒充通过。

## 6. 算法也固定文件，不临时找题

本日题目：**两数之和验收**。网页题目范围：[只看这道题的题面、输入输出和约束](https://leetcode.cn/problems/two-sum/description/)；闭卷日不打开题解。

代码：`~/agent-study/repo-qa-agent/algorithms/d07_two_sum_review.py`。测试：`~/agent-study/repo-qa-agent/algorithm_tests/test_d07_two_sum_review.py`。记录：`~/agent-study/repo-qa-agent/notes/d07.md`。

本地统一接口：`solve(nums: list[int], target: int) -> list[int]`。最小输入：`[2, 7, 11, 15], 9`；预期：`[0, 1]`。

运行：从 `~/agent-study/repo-qa-agent/` 执行 `python -m unittest algorithm_tests.test_d07_two_sum_review -v`。再补2个不同边界；树/链表必须补至少一个非空正常输入，不能只有空输入测试。45分钟后记录真正卡点，不另外开新题。

## 7. 收工前确认

把“是否独立、失败原因、测试输出完整路径、仍未测项、下一次第一步”写入 `~/agent-study/repo-qa-agent/notes/d07.md`。把本日岗位/简历动作写入 `~/agent-study/repo-qa-agent/career/d07_action.md`；只有真实申请才更新 `~/agent-study/repo-qa-agent/career/applications.md`。

**绿灯：** 固定测试与自加边界符合预期，关键逻辑能解释并修改，业务产物真实生成；需要真实模型的学习日另有真实证据。**黄/红灯：** 在当前日卡定位未过函数，不翻页堆欠账。

路径不对先重新运行 `python "$HOME/agent-study/tools/start_day.py" 7` 看打印出的实际地址；它不会覆盖现有文件。模块找不到先确认终端根目录与解释器，不要盲目重装所有依赖。


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
