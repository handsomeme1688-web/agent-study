# D26｜Docker交付

**唯一项目根目录：** `~/agent-study/repo-qa-agent/`。今日任务卡：`~/agent-study/handbook/days/day26.md`。

## 1. 今天具体看哪个文件、读到哪里

|顺序|完整路径与准确范围|只抓住什么|
|---|---|---|
|1|`~/agent-study/materials/notes/26_docker.md`<br>**L1–L26**<br>本包已提供；本次补课讲义，不是教材原文。|D26 补课：容器的路径不同于宿主（本次补课讲义）|

**学到这里停：** 能说出今天目标函数接什么输入、返回什么、至少一个错误分支；接着按下表写代码。源码中的图像不需要下载，未指定内容本日不读。

## 2. 先准备文件，再动手

```bash
cd "$HOME/agent-study/repo-qa-agent"
python "$HOME/agent-study/tools/start_day.py" 26
python "$HOME/agent-study/tools/read_today.py" 26
```

自动生成的阅读页：`~/agent-study/handbook/readings/day26.html`；对应带行号文本：`~/agent-study/handbook/readings/day26.txt`。

## 3. 今天所有文件的完整路径

|动作|完整路径|你在这里做什么|
|---|---|---|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/Dockerfile`|单进程本机容器运行，WORKDIR=/app|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/.dockerignore`|排除真实.env、venv、workspace等|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/scripts/container_smoke.py`|通过HTTP验证容器健康和持久化|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/reports/d26/container.md`|完整构建/运行/停止/重启证据|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/algorithms/d26_coin_change_review.py`|算法独立实现；闭卷日新文件不覆盖旧答案|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/algorithm_tests/test_d26_coin_change_review.py`|已给最小样例，你另补2个有效边界|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/notes/d26.md`|今日复盘、算法用时、错误与下一步|
|新建一次 / 填骨架|`~/agent-study/repo-qa-agent/career/d26_action.md`|今日求职动作与真实证据|
|修改既有文件|`~/agent-study/repo-qa-agent/requirements.lock.txt`|在可复现环境重新冻结并验证|
|修改既有文件|`~/agent-study/repo-qa-agent/README.md`|容器内/app/workspace与宿主目录的对应|
|修改既有文件|`~/agent-study/repo-qa-agent/career/applications.md`|仅记录真实岗位资格、申请和反馈|
|运行或录制后生成|`~/agent-study/repo-qa-agent/workspace/container-data/`|Docker数据卷挂载源目录|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d26/http.json`|容器启动与重启后的HTTP结果|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d26/unittest.txt`|check_day.py自动保存主项目测试输出|
|运行或录制后生成|`~/agent-study/repo-qa-agent/reports/d26/algorithm.txt`|check_day.py自动保存算法测试输出|

**“新建一次”已由准备工具完成时，你只需要打开并填内容；不要删掉重建。报告初始状态NOT_DONE不是成绩。程序生成项没有实际运行结果前不要填写成功。**

## 4. 要写的接口、具体操作和停止标准

```text
容器中的 SQLite/Qdrant 路径均取 /app/workspace；必须由环境或配置控制，不能写死宿主~/路径。
```

**前置：** 本机README已有可执行启动命令。

**步骤：** 从一个干净虚拟环境整理你实际用到的直接依赖，安装验证后记录Python与完整锁定版本。编写Dockerfile和.dockerignore；排除.env、私人会话、venv、Git目录等。镜像不写真实密钥，运行时通过环境注入。服务使用一个worker；SQLite与Qdrant本地存储写workspace，通过挂载持久化。

模型文件由下载步骤或本地缓存显式提供，写清首次下载需要网络。离线mock演示和真实模型演示采用明确开关，不允许“API不可用自动返回预制答案但界面显示正常”。

**验收：** 约定**见本日运行区的完整命令**成功；运行后/health通过；执行一次查询；创建会话后停掉并重新启动容器，挂载正确时记录仍在。测试时使用专门的演示数据，不装入个人真实资料。

**交什么：** Dockerfile、.dockerignore、完整运行命令、环境变量表、数据目录说明、一次重启前后证据。模型/API未接通时，记录健康检查与离线模式通过、真实问答未测。

**口述：** 镜像与容器差别；删除容器后哪些数据会丢；为什么本地嵌入式数据库不直接启动多个worker共享访问？

**卡住：** Docker在当前机器无法安装时，今天用第二个干净venv验证安装并把容器项标未完成，不购买云资源。D28优先保证别人能按文档在本地启动。

**求职：** 修正“已部署”表述：本地容器验证不等于公网生产部署。

### 本版锁定的固定输入 / 预期

构建和health通过不等于真实RAG通过。检索索引与模型缓存首次准备方式必须写进README。只用一个worker。

**首次容器索引必须另做：** 镜像复制公开 `/app/data/chunks.jsonl` 后，挂载的 `/app/workspace` 初次为空；在容器内执行已有 `scripts.build_index`，`--chunks /app/data/chunks.jsonl --db /app/workspace/qdrant --report /app/workspace/container_index.json`。客户端加载Embedding所需的下载/缓存与同一向量维数都要实测。不完成索引准备不能将health通过称为问答通过。

保留一次完整启动窗口；停掉旧的本机uvicorn后再用8000端口。容器里启动必须绑定0.0.0.0，宿主映射仍限制127.0.0.1。

## 5. 写完以后，运行哪些命令

**下面业务入口需要先完成本日骨架，首次NotImplementedError不是环境故障。**

```bash
cd "$HOME/agent-study/repo-qa-agent"
docker build -t repo-qa-agent:study "$HOME/agent-study/repo-qa-agent"
docker run --name repo-qa-study --env-file "$HOME/agent-study/repo-qa-agent/.env" -p 127.0.0.1:8000:8000 --mount "type=bind,source=$HOME/agent-study/repo-qa-agent/workspace/container-data,target=/app/workspace" repo-qa-agent:study
# 第二个终端：
python -m scripts.container_smoke --out "$HOME/agent-study/repo-qa-agent/reports/d26/http.json"
python "$HOME/agent-study/tools/check_day.py" 26
```

固定测试+已创建的过去测试输出：`~/agent-study/repo-qa-agent/reports/d26/unittest.txt`。当前算法测试输出：`~/agent-study/repo-qa-agent/reports/d26/algorithm.txt`。有意未做的集成验收不在此命令中冒充通过。

## 6. 算法也固定文件，不临时找题

本日题目：**默认复习零钱兑换**。网页题目范围：[只看这道题的题面、输入输出和约束](https://leetcode.cn/problems/coin-change/description/)；闭卷日不打开题解。

代码：`~/agent-study/repo-qa-agent/algorithms/d26_coin_change_review.py`。测试：`~/agent-study/repo-qa-agent/algorithm_tests/test_d26_coin_change_review.py`。记录：`~/agent-study/repo-qa-agent/notes/d26.md`。

本地统一接口：`solve(coins: list[int], amount: int) -> int`。最小输入：`[1], 0`；预期：`0`。

运行：从 `~/agent-study/repo-qa-agent/` 执行 `python -m unittest algorithm_tests.test_d26_coin_change_review -v`。再补2个不同边界；树/链表必须补至少一个非空正常输入，不能只有空输入测试。45分钟后记录真正卡点，不另外开新题。

## 7. 收工前确认

把“是否独立、失败原因、测试输出完整路径、仍未测项、下一次第一步”写入 `~/agent-study/repo-qa-agent/notes/d26.md`。把本日岗位/简历动作写入 `~/agent-study/repo-qa-agent/career/d26_action.md`；只有真实申请才更新 `~/agent-study/repo-qa-agent/career/applications.md`。

**绿灯：** 固定测试与自加边界符合预期，关键逻辑能解释并修改，业务产物真实生成；需要真实模型的学习日另有真实证据。**黄/红灯：** 在当前日卡定位未过函数，不翻页堆欠账。

路径不对先重新运行 `python "$HOME/agent-study/tools/start_day.py" 26` 看打印出的实际地址；它不会覆盖现有文件。模块找不到先确认终端根目录与解释器，不要盲目重装所有依赖。


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
