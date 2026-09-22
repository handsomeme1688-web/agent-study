# D01｜文件读写

**唯一项目根目录：** `~/agent-study/repo-qa-agent/`。今日任务卡：`~/agent-study/handbook/days/day01.md`。

## 1. 今天具体看哪个文件、读到哪里

|顺序|完整路径与准确范围|只抓住什么|
|---|---|---|
|1|`~/agent-study/materials/notes/01_python_io.md`<br>**L1–L39**<br>本包已提供；本次补课讲义，不是教材原文。|D01 补课：文件和JSONL（本次补课讲义）|
|最后|`~/agent-study/repo-qa-agent/tests/test_d01_io.py`<br>**L1–L32，读完整文件，不修改固定预期。**|先读每个测试名，再读输入和断言；这是当天作业的精确契约。|
|样例|`~/agent-study/repo-qa-agent/fixtures/mini.md`<br>**L1–L8**|今天唯一小样例；不要换成整本教程。|

**学到这里停：** 能说出今天目标函数接什么输入、返回什么、至少一个错误分支；接着按下表写代码。源码中的图像不需要下载，未指定内容本日不读。

## 2. 先准备文件，再动手

```bash
cd "$HOME/agent-study/repo-qa-agent"
python "$HOME/agent-study/tools/start_day.py" 1
python "$HOME/agent-study/tools/read_today.py" 1
```

自动生成的阅读页：`~/agent-study/handbook/readings/day01.html`；对应带行号文本：`~/agent-study/handbook/readings/day01.txt`。

## 3. 今天所有文件的完整路径

|动作|完整路径|你在这里做什么|
|---|---|---|
|只读：已提供|`~/agent-study/repo-qa-agent/tests/test_d01_io.py`|固定验收用例；不改预期值来刷绿。|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/scripts/d01_io_demo.py`|练习入口：读取固定样例，写出并读回两条JSONL|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/tests/test_d01_extra.py`|自己写中文路径的边界测试|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/career/profile.md`|填写真实毕业、学历、城市与出勤条件|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/algorithms/d01_two_sum.py`|算法独立实现；闭卷日新文件不覆盖旧答案|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/algorithm_tests/test_d01_two_sum.py`|已给最小样例，你另补2个有效边界|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/notes/d01.md`|今日复盘、算法用时、错误与下一步|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/career/d01_action.md`|今日求职动作与真实证据|
|修改既有文件|`~/agent-study/repo-qa-agent/agent_lab/io.py`|已有骨架：实现 read_text、write_jsonl|
|修改既有文件|`~/agent-study/repo-qa-agent/README.md`|填写当前进度，不写未完成能力|
|修改既有文件|`~/agent-study/repo-qa-agent/career/applications.md`|仅记录真实岗位资格、申请和反馈|
|运行或录制后生成|`~/agent-study/repo-qa-agent/workspace/d01/records.jsonl`|演示脚本生成的两条记录|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d01/demo.txt`|演示终端输出|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d01/unittest.txt`|check_day.py自动保存主项目测试输出|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d01/algorithm.txt`|check_day.py自动保存算法测试输出|

**“新建一次”已由准备工具完成时，你只需要打开并填内容；不要删掉重建。报告初始状态NOT_DONE不是成绩。程序生成项没有实际运行结果前不要填写成功。**

## 4. 要写的接口、具体操作和停止标准

```text
read_text(path: str) -> str
write_jsonl(records: list[dict], path: str) -> None
```

**前置：** 无；能打开终端和编辑Python文件即可。**今天结束时：** 一份中文Markdown可读入，一组字典可存成JSONL。



**动手顺序：** 先按包内README运行D1测试，确认报的是未实现函数；打开`~/agent-study/repo-qa-agent/fixtures/mini.md`观察换行。实现`~/agent-study/repo-qa-agent/agent_lab/io.py`中的`read_text(path)`，先打印返回值的`repr`确认它是字符串。再实现`write_jsonl(records,path)`：创建父目录、覆盖写入、一条记录一行、中文不转义。最后在交互窗口把两个字典写出，再逐行`json.loads`读回比对。

**固定输入输出：** `[{'id':1,'text':'工具\n下一行'},{'id':2,'text':'检索'}]`应写成两条物理行，读回后仍完全相等；嵌在字符串中的换行不能把一个JSON对象拆成两条记录。空文件读成`''`；不存在的路径抛`FileNotFoundError`；连续写同一路径第二次应覆盖而非重复追加。

**交什么、怎么验：** 保存`~/agent-study/repo-qa-agent/agent_lab/io.py`与`~/agent-study/repo-qa-agent/notes/d01.md`。运行**见本日运行区的完整命令**，6项测试全过；自己加一项“路径包含中文”的测试。关闭实现，10分钟重写文件读取函数，再把输出文件名改成一个新子目录，仍能运行即停。

**口述自检：** `read_text`返回字符串，JSONL每行代表一个JSON值；`with`负责关闭文件；`w`覆盖、`a`追加。必须结合自己的输出说明，不能只说“懂JSON”。

**卡住先补：** 只试`open→read→print`三步；不要今天学异常继承体系。报`ModuleNotFoundError: agent_lab`先确认终端在项目根目录。今天不配置LLM、不装LangGraph。

**求职15分钟：** 填学历/专业/毕业年月/城市/到岗日/每周出勤天数/可连续实习月份；未知的保持空白。

### 本版锁定的固定输入 / 预期

先跑已提供的6个固定测试；在 test_d01_extra.py 增加中文路径案例，不能修改固定测试预期。演示输出必须包含 records=2、roundtrip=True。

### 从第一行代码开始的顺序

先打开 `~/agent-study/repo-qa-agent/agent_lab/io.py`，只完成read_text。运行第一个测试，看返回值是否是字符串。再完成write_jsonl；最后打开 `~/agent-study/repo-qa-agent/scripts/d01_io_demo.py`，这个入口已提供，读懂它怎样调用你写的两个函数。

在 `~/agent-study/repo-qa-agent/tests/test_d01_extra.py` 写中文目录下读文件的测试。正式函数与测试分开；不要把正式实现写在演示脚本里。

## 5. 写完以后，运行哪些命令

**下面业务入口需要先完成本日骨架，首次NotImplementedError不是环境故障。**

```bash
cd "$HOME/agent-study/repo-qa-agent"
python -m scripts.d01_io_demo
python "$HOME/agent-study/tools/check_day.py" 1
```

固定测试+已创建的过去测试输出：`~/agent-study/repo-qa-agent/reports/d01/unittest.txt`。当前算法测试输出：`~/agent-study/repo-qa-agent/reports/d01/algorithm.txt`。有意未做的集成验收不在此命令中冒充通过。

## 6. 算法也固定文件，不临时找题

本日题目：**两数之和**。网页题目范围：[只看这道题的题面、输入输出和约束](https://leetcode.cn/problems/two-sum/description/)；闭卷日不打开题解。

代码：`~/agent-study/repo-qa-agent/algorithms/d01_two_sum.py`。测试：`~/agent-study/repo-qa-agent/algorithm_tests/test_d01_two_sum.py`。记录：`~/agent-study/repo-qa-agent/notes/d01.md`。

本地统一接口：`solve(nums: list[int], target: int) -> list[int]`。最小输入：`[2, 7, 11, 15], 9`；预期：`[0, 1]`。

运行：从 `~/agent-study/repo-qa-agent/` 执行 `python -m unittest algorithm_tests.test_d01_two_sum -v`。再补2个不同边界；树/链表必须补至少一个非空正常输入，不能只有空输入测试。45分钟后记录真正卡点，不另外开新题。

## 7. 收工前确认

把“是否独立、失败原因、测试输出完整路径、仍未测项、下一次第一步”写入 `~/agent-study/repo-qa-agent/notes/d01.md`。把本日岗位/简历动作写入 `~/agent-study/repo-qa-agent/career/d01_action.md`；只有真实申请才更新 `~/agent-study/repo-qa-agent/career/applications.md`。

**绿灯：** 固定测试与自加边界符合预期，关键逻辑能解释并修改，业务产物真实生成；需要真实模型的学习日另有真实证据。**黄/红灯：** 在当前日卡定位未过函数，不翻页堆欠账。

路径不对先重新运行 `python "$HOME/agent-study/tools/start_day.py" 1` 看打印出的实际地址；它不会覆盖现有文件。模块找不到先确认终端根目录与解释器，不要盲目重装所有依赖。


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
