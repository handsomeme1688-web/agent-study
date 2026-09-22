# 所有脚本入口与参数契约

脚本路径全部明确；除D1/D2/D3/D6演示已提供，其他入口需在对应日编写。业务代码放agent_lab，参数解析与写出报告放scripts。

## D01

项目根目录：`~/agent-study/repo-qa-agent/`

```bash
python -m scripts.d01_io_demo
```

## D02

项目根目录：`~/agent-study/repo-qa-agent/`

```bash
python -m scripts.d02_chunk_demo
```

## D03

项目根目录：`~/agent-study/repo-qa-agent/`

```bash
python -m scripts.d03_search_demo
```

## D04

项目根目录：`~/agent-study/repo-qa-agent/`

```bash
python -m pip install openai python-dotenv
python -c "import pathlib, subprocess, sys; pathlib.Path.home().joinpath('agent-study/repo-qa-agent/requirements.lock.txt').write_bytes(subprocess.check_output([sys.executable, '-m', 'pip', 'freeze']))"
python -m scripts.ask_once "只回复：连接成功" --out "$HOME/agent-study/repo-qa-agent/reports/d04/live_call.json"
```

## D05

项目根目录：`~/agent-study/repo-qa-agent/`

```bash
python -m scripts.d05_dispatch_demo --out "$HOME/agent-study/repo-qa-agent/reports/d05/dispatch.jsonl"
```

## D06

项目根目录：`~/agent-study/repo-qa-agent/`

```bash
python -m scripts.d06_loop_demo
```

## D07

项目根目录：`~/agent-study/repo-qa-agent/`

```bash
python -m scripts.agent_smoke --question "请先检索资料，再回答谁执行工具" --out "$HOME/agent-study/repo-qa-agent/reports/d07/live_agent.json"
```

## D08

项目根目录：`~/agent-study/repo-qa-agent/`

```bash
python -m scripts.native_tool_call --question "检索工具执行的说明" --out "$HOME/agent-study/repo-qa-agent/reports/d08/messages.json"
```

## D09

项目根目录：`~/agent-study/repo-qa-agent/`

```bash
python -m scripts.ingest --manifest "$HOME/agent-study/repo-qa-agent/data/source_manifest.json" --out "$HOME/agent-study/repo-qa-agent/data/chunks.jsonl" --report "$HOME/agent-study/repo-qa-agent/reports/d09/ingest.json"
```

## D10

项目根目录：`~/agent-study/repo-qa-agent/`

```bash
python -m scripts.check_dataset --dev "$HOME/agent-study/repo-qa-agent/data/dev.jsonl" --holdout "$HOME/agent-study/repo-qa-agent/data/holdout.jsonl" --out "$HOME/agent-study/repo-qa-agent/reports/d10/dataset_check.json"
```

## D11

项目根目录：`~/agent-study/repo-qa-agent/`

```bash
python -m pip install sentence-transformers
python -m scripts.embed_smoke --out "$HOME/agent-study/repo-qa-agent/reports/d11/embedding.json"
```

## D12

项目根目录：`~/agent-study/repo-qa-agent/`

```bash
python -m pip install qdrant-client
python -m scripts.build_index --chunks "$HOME/agent-study/repo-qa-agent/data/chunks.jsonl" --db "$HOME/agent-study/repo-qa-agent/workspace/qdrant" --report "$HOME/agent-study/repo-qa-agent/reports/d12/index.json"
python -m scripts.vector_search --question "工具如何注册" --out "$HOME/agent-study/repo-qa-agent/reports/d12/search.json"
```

## D13

项目根目录：`~/agent-study/repo-qa-agent/`

```bash
python -m scripts.qa --mode vector --question "ReAct循环如何停止" --out "$HOME/agent-study/repo-qa-agent/reports/d13/example.json"
```

## D14

项目根目录：`~/agent-study/repo-qa-agent/`

```bash
python -m scripts.evaluate --dataset "$HOME/agent-study/repo-qa-agent/data/dev.jsonl" --mode keyword --out "$HOME/agent-study/repo-qa-agent/reports/d14/keyword_raw.jsonl"
python -m scripts.evaluate --dataset "$HOME/agent-study/repo-qa-agent/data/dev.jsonl" --mode vector --out "$HOME/agent-study/repo-qa-agent/reports/d14/vector_raw.jsonl"
python -m scripts.score_report --scores "$HOME/agent-study/repo-qa-agent/reports/d14/dev_scores.jsonl" --out "$HOME/agent-study/repo-qa-agent/reports/d14/summary.json"
```

## D15

项目根目录：`~/agent-study/repo-qa-agent/`

```bash
python -m scripts.qa --mode agent --question "ReAct如何查找工具，又如何在未知工具时处理" --out "$HOME/agent-study/repo-qa-agent/reports/d15/fact.json"
```

## D16

项目根目录：`~/agent-study/repo-qa-agent/`

```bash
python -m scripts.followup_demo --out "$HOME/agent-study/repo-qa-agent/reports/d16/followup.json"
```

## D17

项目根目录：`~/agent-study/repo-qa-agent/`

```bash
python -m scripts.evaluate --dataset "$HOME/agent-study/repo-qa-agent/data/dev.jsonl" --mode vector --config "$HOME/agent-study/repo-qa-agent/data/experiment_k3.json" --out "$HOME/agent-study/repo-qa-agent/reports/d17/k3_raw.jsonl"
python -m scripts.evaluate --dataset "$HOME/agent-study/repo-qa-agent/data/dev.jsonl" --mode vector --config "$HOME/agent-study/repo-qa-agent/data/experiment_k5.json" --out "$HOME/agent-study/repo-qa-agent/reports/d17/k5_raw.jsonl"
```

## D18

项目根目录：`~/agent-study/repo-qa-agent/`

```bash
python -m pip install fastapi uvicorn httpx
python -m uvicorn agent_lab.api:app --host 127.0.0.1 --port 8000
# 上一行保持运行；在第二个已激活同一虚拟环境的终端执行：
python -m scripts.api_smoke --out "$HOME/agent-study/repo-qa-agent/reports/d18/http.json"
```

## D19

项目根目录：`~/agent-study/repo-qa-agent/`

```bash
python -m scripts.storage_smoke --db "$HOME/agent-study/repo-qa-agent/workspace/sessions.sqlite3" --out "$HOME/agent-study/repo-qa-agent/reports/d19/restart.json"
```

## D20

项目根目录：`~/agent-study/repo-qa-agent/`

```bash
python -m scripts.auth_smoke --out "$HOME/agent-study/repo-qa-agent/reports/d20/isolation.json"
```

## D21

项目根目录：`~/agent-study/repo-qa-agent/`

```bash
python -m scripts.qa --mode agent --question "工具怎样注册" --out "$HOME/agent-study/repo-qa-agent/reports/d21/query.json"
```

## D22

项目根目录：`~/agent-study/repo-qa-agent/`

```bash
python -m scripts.evaluate --dataset "$HOME/agent-study/repo-qa-agent/data/holdout.jsonl" --mode keyword --config "$HOME/agent-study/repo-qa-agent/data/final_config.json" --out "$HOME/agent-study/repo-qa-agent/reports/d22/keyword_raw.jsonl"
python -m scripts.evaluate --dataset "$HOME/agent-study/repo-qa-agent/data/holdout.jsonl" --mode vector --config "$HOME/agent-study/repo-qa-agent/data/final_config.json" --out "$HOME/agent-study/repo-qa-agent/reports/d22/vector_raw.jsonl"
python -m scripts.evaluate --dataset "$HOME/agent-study/repo-qa-agent/data/holdout.jsonl" --mode agent --config "$HOME/agent-study/repo-qa-agent/data/final_config.json" --out "$HOME/agent-study/repo-qa-agent/reports/d22/agent_raw.jsonl"
```

## D23

项目根目录：`~/agent-study/repo-qa-agent/`

```bash
python -m scripts.api_smoke --out "$HOME/agent-study/repo-qa-agent/reports/d23/live_chain.json"
```

## D24

项目根目录：`~/agent-study/repo-qa-agent/`

```bash
python -m pip install "mcp>=2,<3"
python -m scripts.mcp_smoke --out "$HOME/agent-study/repo-qa-agent/reports/d24/mcp_result.json"
python -m unittest integration_tests.test_d24_mcp -v
```

## D25

项目根目录：`~/agent-study/repo-qa-agent/`

```bash
python -m pip install langgraph
python -m unittest tests.test_d25_graph -v
```

## D26

项目根目录：`~/agent-study/repo-qa-agent/`

```bash
docker build -t repo-qa-agent:study "$HOME/agent-study/repo-qa-agent"
docker run --name repo-qa-study --env-file "$HOME/agent-study/repo-qa-agent/.env" -p 127.0.0.1:8000:8000 --mount "type=bind,source=$HOME/agent-study/repo-qa-agent/workspace/container-data,target=/app/workspace" repo-qa-agent:study
# 第二个终端：
python -m scripts.container_smoke --out "$HOME/agent-study/repo-qa-agent/reports/d26/http.json"
```

## D27

项目根目录：`~/agent-study/repo-qa-agent/`

```bash
python -m unittest discover -s tests -v
```

## D28

项目根目录：`~/agent-study/repo-qa-agent/`

```bash
python "$HOME/agent-study/tools/reproduce.py" prepare
# 阅读它打印的目标清单：不会复制旧环境、旧索引、旧密钥或历史报告
python "$HOME/agent-study/tools/reproduce.py" check
# check会新建独立虚拟环境、按锁文件安装并执行离线测试；结果据实保存
# 完成后返回主项目，继续下面的日常检查
cd "$HOME/agent-study/repo-qa-agent"
```

## D29

项目根目录：`~/agent-study/repo-qa-agent/`

```bash
python -m scripts.d29_change_request --out "$HOME/agent-study/repo-qa-agent/reports/d29/change_request.txt"
```

## D30

项目根目录：`~/agent-study/repo-qa-agent/`

```bash
python -m unittest discover -s tests -v
```