# D12｜Qdrant本地索引

**唯一项目根目录：** `~/agent-study/repo-qa-agent/`。今日任务卡：`~/agent-study/handbook/days/day12.md`。

## 1. 今天具体看哪个文件、读到哪里

|顺序|完整路径与准确范围|只抓住什么|
|---|---|---|
|1|`~/agent-study/materials/notes/12_vector_store.md`<br>**L1–L25**<br>本包已提供；本次补课讲义，不是教材原文。|D12 补课：本地向量库（本次补课讲义）|

**学到这里停：** 能说出今天目标函数接什么输入、返回什么、至少一个错误分支；接着按下表写代码。源码中的图像不需要下载，未指定内容本日不读。

## 2. 先准备文件，再动手

```bash
cd "$HOME/agent-study/repo-qa-agent"
python "$HOME/agent-study/tools/start_day.py" 12
python "$HOME/agent-study/tools/read_today.py" 12
```

自动生成的阅读页：`~/agent-study/handbook/readings/day12.html`；对应带行号文本：`~/agent-study/handbook/readings/day12.txt`。

## 3. 今天所有文件的完整路径

|动作|完整路径|你在这里做什么|
|---|---|---|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/agent_lab/vector_store.py`|创建集合、upsert、query、close；本地单进程|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/scripts/build_index.py`|导入正式片段并建持久化索引|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/scripts/vector_search.py`|关键词参数接收后编码并查询|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/tests/test_d12_vectors.py`|3维玩具排序、空库、重复ID测试|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/algorithms/d12_subarray_sum.py`|算法独立实现；闭卷日新文件不覆盖旧答案|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/algorithm_tests/test_d12_subarray_sum.py`|已给最小样例，你另补2个有效边界|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/notes/d12.md`|今日复盘、算法用时、错误与下一步|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/career/d12_action.md`|今日求职动作与真实证据|
|修改既有文件|`~/agent-study/repo-qa-agent/requirements.txt`|增加qdrant-client实际直接依赖|
|修改既有文件|`~/agent-study/repo-qa-agent/career/applications.md`|仅记录真实岗位资格、申请和反馈|
|运行或录制后生成|`~/agent-study/repo-qa-agent/workspace/qdrant/`|Qdrant自行创建内部文件，不手工命名|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d12/index.json`|向量数量、维数与重复导入结果|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d12/search.json`|3个真实检索问题及重启后结果|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d12/unittest.txt`|check_day.py自动保存主项目测试输出|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d12/algorithm.txt`|check_day.py自动保存算法测试输出|

**“新建一次”已由准备工具完成时，你只需要打开并填内容；不要删掉重建。报告初始状态NOT_DONE不是成绩。程序生成项没有实际运行结果前不要填写成功。**

## 4. 要写的接口、具体操作和停止标准

```text
class LocalVectorStore:
    __init__(self, path: str, collection: str, dim: int)
    upsert(self, chunks: list[dict], vectors: list[list[float]]) -> None
    query(self, vector: list[float], k: int = 3) -> list[dict]
    count(self) -> int
    close(self) -> None
```

**前置：** D11数学测试通过；真实Embedding未完成可先做玩具向量测试。

**步骤：** 新建`~/agent-study/repo-qa-agent/agent_lab/vector_store.py`。先用`QdrantClient(":memory:")`与3维玩具collection练习：点1=[1,0,0]、点2=[0,1,0]、点3=[0.9,0.1,0]，用Cosine距离；查询[1,0,0]，前两名应为1和3。再用`QdrantClient(path="workspace/qdrant")`持久化真实向量。真实collection维数从Embedding配置读取；点ID用整数或合法UUID，原始chunk_id放payload，不直接把任意长字符串当数据库点ID。

每个payload保存chunk_id、source、version、start_line、end_line、text。真实点ID可由源版本/路径/行范围生成稳定UUID。复用ID进行upsert；小语料版本变更时重建collection，避免新旧数据混用。一次只开一个使用该本地目录的客户端进程，退出时关闭客户端。

**验收：** 新建`~/agent-study/repo-qa-agent/tests/test_d12_vectors.py`，验证玩具排序、空库、同ID重复写入不增加点数。真实库导入20–40片段，再关掉进程重启查询，能找回来源和正文；抽5条payload与原文核对。执行**见本日运行区的完整命令**，保存真实检索3题的结果。

**口述：** collection维数必须与向量一致；向量库返回相似片段不是最终回答。本地开发模式不证明生产并发能力。

**卡住：** 先用3维玩具collection隔离数据库问题；512维模型向量只能进入对应维数的新collection。不要通过删校验或随机填零“修复”维数错误。

**求职：** 更新README技术栈，只加实际跑通的Embedding/向量库，不写“精通RAG”。

### 本版锁定的固定输入 / 预期

查询[1,0,0]对玩具点[1,0,0]、[0,1,0]、[.9,.1,0]前两名为1、3。正式库关闭再打开可查。

## 5. 写完以后，运行哪些命令

**下面业务入口需要先完成本日骨架，首次NotImplementedError不是环境故障。**

```bash
cd "$HOME/agent-study/repo-qa-agent"
python -m pip install qdrant-client
python -m scripts.build_index --chunks "$HOME/agent-study/repo-qa-agent/data/chunks.jsonl" --db "$HOME/agent-study/repo-qa-agent/workspace/qdrant" --report "$HOME/agent-study/repo-qa-agent/reports/d12/index.json"
python -m scripts.vector_search --question "工具如何注册" --out "$HOME/agent-study/repo-qa-agent/reports/d12/search.json"
python "$HOME/agent-study/tools/check_day.py" 12
```

固定测试+已创建的过去测试输出：`~/agent-study/repo-qa-agent/reports/d12/unittest.txt`。当前算法测试输出：`~/agent-study/repo-qa-agent/reports/d12/algorithm.txt`。有意未做的集成验收不在此命令中冒充通过。

## 6. 算法也固定文件，不临时找题

本日题目：**和为K的子数组**。网页题目范围：[只看这道题的题面、输入输出和约束](https://leetcode.cn/problems/subarray-sum-equals-k/description/)；闭卷日不打开题解。

代码：`~/agent-study/repo-qa-agent/algorithms/d12_subarray_sum.py`。测试：`~/agent-study/repo-qa-agent/algorithm_tests/test_d12_subarray_sum.py`。记录：`~/agent-study/repo-qa-agent/notes/d12.md`。

本地统一接口：`solve(nums: list[int], k: int) -> int`。最小输入：`[1,1,1], 2`；预期：`2`。

运行：从 `~/agent-study/repo-qa-agent/` 执行 `python -m unittest algorithm_tests.test_d12_subarray_sum -v`。再补2个不同边界；树/链表必须补至少一个非空正常输入，不能只有空输入测试。45分钟后记录真正卡点，不另外开新题。

## 7. 收工前确认

把“是否独立、失败原因、测试输出完整路径、仍未测项、下一次第一步”写入 `~/agent-study/repo-qa-agent/notes/d12.md`。把本日岗位/简历动作写入 `~/agent-study/repo-qa-agent/career/d12_action.md`；只有真实申请才更新 `~/agent-study/repo-qa-agent/career/applications.md`。

**绿灯：** 固定测试与自加边界符合预期，关键逻辑能解释并修改，业务产物真实生成；需要真实模型的学习日另有真实证据。**黄/红灯：** 在当前日卡定位未过函数，不翻页堆欠账。

路径不对先重新运行 `python "$HOME/agent-study/tools/start_day.py" 12` 看打印出的实际地址；它不会覆盖现有文件。模块找不到先确认终端根目录与解释器，不要盲目重装所有依赖。


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
