# D11｜余弦与真实Embedding

**唯一项目根目录：** `~/agent-study/repo-qa-agent/`。今日任务卡：`~/agent-study/handbook/days/day11.md`。

## 1. 今天具体看哪个文件、读到哪里

|顺序|完整路径与准确范围|只抓住什么|
|---|---|---|
|1|`~/agent-study/materials/hello-agents/docs/chapter8/第八章 记忆与检索.md`<br>**L1085–L1100**<br>[打开固定版本相同行范围](https://github.com/datawhalechina/hello-agents/blob/b4aca1af44b7a492b4bfdec5aa100d556c65db54/docs/chapter8/%E7%AC%AC%E5%85%AB%E7%AB%A0%20%E8%AE%B0%E5%BF%86%E4%B8%8E%E6%A3%80%E7%B4%A2.md#L1085-L1100)|数据向量化在完整流程中的位置|
|2|`~/agent-study/materials/notes/11_embeddings.md`<br>**L1–L24**<br>本包已提供；本次补课讲义，不是教材原文。|D11 补课：真实文本向量化（本次补课讲义）|

**学到这里停：** 能说出今天目标函数接什么输入、返回什么、至少一个错误分支；接着按下表写代码。源码中的图像不需要下载，未指定内容本日不读。

## 2. 先准备文件，再动手

```bash
cd "$HOME/agent-study/repo-qa-agent"
python "$HOME/agent-study/tools/start_day.py" 11
python "$HOME/agent-study/tools/read_today.py" 11
```

自动生成的阅读页：`~/agent-study/handbook/readings/day11.html`；对应带行号文本：`~/agent-study/handbook/readings/day11.txt`。

## 3. 今天所有文件的完整路径

|动作|完整路径|你在这里做什么|
|---|---|---|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/agent_lab/embeddings.py`|余弦、模型加载、文本向量化与长度检查|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/scripts/embed_smoke.py`|先3条中文文本，再报告真实shape|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/data/embedding_config.json`|模型ID、实际revision、维数、归一化与查询前缀|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/tests/test_d11_embeddings.py`|纯数学/假编码器测试；不下载模型|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/algorithms/d11_binary_search_rewrite.py`|算法独立实现；闭卷日新文件不覆盖旧答案|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/algorithm_tests/test_d11_binary_search_rewrite.py`|已给最小样例，你另补2个有效边界|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/notes/d11.md`|今日复盘、算法用时、错误与下一步|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/career/d11_action.md`|今日求职动作与真实证据|
|修改既有文件|`~/agent-study/repo-qa-agent/requirements.txt`|增加sentence-transformers实际直接依赖|
|修改既有文件|`~/agent-study/repo-qa-agent/requirements.lock.txt`|重新记录环境版本|
|修改既有文件|`~/agent-study/repo-qa-agent/career/applications.md`|仅记录真实岗位资格、申请和反馈|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d11/embedding.json`|真实3条文本的shape、范数、长度和配置|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d11/unittest.txt`|check_day.py自动保存主项目测试输出|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d11/algorithm.txt`|check_day.py自动保存算法测试输出|

**“新建一次”已由准备工具完成时，你只需要打开并填内容；不要删掉重建。报告初始状态NOT_DONE不是成绩。程序生成项没有实际运行结果前不要填写成功。**

## 4. 要写的接口、具体操作和停止标准

```text
cosine(a: list[float], b: list[float]) -> float
embed_texts(texts: list[str], model, is_query: bool = False) -> list[list[float]]
```

**前置：** D9语料稳定。

**步骤：** 先写`cosine(a,b)`小函数，手算`[1,0]`与`[1,0]`相似度1、与`[0,1]`为0；零向量和维数不同应明确报错。再新建`~/agent-study/repo-qa-agent/agent_lab/embeddings.py`，默认实验使用`BAAI/bge-small-zh-v1.5`，按模型卡安装Sentence-Transformers，先用CPU编码3条中文短文本；查询前缀按模型卡配置并记录。示例初始化为`SentenceTransformer("BAAI/bge-small-zh-v1.5", device="cpu")`，不要求GPU。

把你使用的模型名/版本、是否归一化、查询前缀写入`~/agent-study/repo-qa-agent/data/embedding_config.json`。用模型tokenizer检查源片段输入长度，超过模型限制的片段先缩短并保留原文定位，不把被静默截断的尾部当已索引。向量维数与最大输入token数是两个不同概念。

**验收：** 新建`~/agent-study/repo-qa-agent/tests/test_d11_embeddings.py`，确定性用例验证余弦计算与错误分支；真实实验3条文本应生成3个有限数值向量。所选BGE-small-zh-v1.5的模型卡列出的向量维数为512，打印实际shape核对，不把其他模型维数硬套过来。保存一次真实运行记录；能拿相同文本查询自身，并解释不同文本的分数不保证答案正确。

**交什么：** 代码、实际配置、3条向量的维数/范数记录；无需把大模型权重提交Git。

**口述：** Embedding是数值表示，不是答案；相似度不是正确率或概率。文本不相关也可能返回某个“最相近”的向量。

**卡住：** 下载/依赖失败先保留三个人造向量继续D12的数据库机械测试，但将真实语义检索标“未测”；不能用随机向量包装RAG成果。确需改用已有Embedding API时记录替代模型与维数，后续全部索引一致重建，不同时试多套。

**求职：** 挑1个目标JD，删去自己尚未做过却写成“熟悉”的简历词。

### 本版锁定的固定输入 / 预期

同向=1、正交=0；零向量/维数不符拒绝。真实文本输出真实向量，不能用随机向量记语义检索完成。

## 5. 写完以后，运行哪些命令

**下面业务入口需要先完成本日骨架，首次NotImplementedError不是环境故障。**

```bash
cd "$HOME/agent-study/repo-qa-agent"
python -m pip install sentence-transformers
python -m scripts.embed_smoke --out "$HOME/agent-study/repo-qa-agent/reports/d11/embedding.json"
python "$HOME/agent-study/tools/check_day.py" 11
```

固定测试+已创建的过去测试输出：`~/agent-study/repo-qa-agent/reports/d11/unittest.txt`。当前算法测试输出：`~/agent-study/repo-qa-agent/reports/d11/algorithm.txt`。有意未做的集成验收不在此命令中冒充通过。

## 6. 算法也固定文件，不临时找题

本日题目：**二分闭卷**。网页题目范围：[只看这道题的题面、输入输出和约束](https://leetcode.cn/problems/binary-search/description/)；闭卷日不打开题解。

代码：`~/agent-study/repo-qa-agent/algorithms/d11_binary_search_rewrite.py`。测试：`~/agent-study/repo-qa-agent/algorithm_tests/test_d11_binary_search_rewrite.py`。记录：`~/agent-study/repo-qa-agent/notes/d11.md`。

本地统一接口：`solve(nums: list[int], target: int) -> int`。最小输入：`[1], 0`；预期：`-1`。

运行：从 `~/agent-study/repo-qa-agent/` 执行 `python -m unittest algorithm_tests.test_d11_binary_search_rewrite -v`。再补2个不同边界；树/链表必须补至少一个非空正常输入，不能只有空输入测试。45分钟后记录真正卡点，不另外开新题。

## 7. 收工前确认

把“是否独立、失败原因、测试输出完整路径、仍未测项、下一次第一步”写入 `~/agent-study/repo-qa-agent/notes/d11.md`。把本日岗位/简历动作写入 `~/agent-study/repo-qa-agent/career/d11_action.md`；只有真实申请才更新 `~/agent-study/repo-qa-agent/career/applications.md`。

**绿灯：** 固定测试与自加边界符合预期，关键逻辑能解释并修改，业务产物真实生成；需要真实模型的学习日另有真实证据。**黄/红灯：** 在当前日卡定位未过函数，不翻页堆欠账。

路径不对先重新运行 `python "$HOME/agent-study/tools/start_day.py" 11` 看打印出的实际地址；它不会覆盖现有文件。模块找不到先确认终端根目录与解释器，不要盲目重装所有依赖。


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
