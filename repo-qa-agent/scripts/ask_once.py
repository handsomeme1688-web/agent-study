"""
D04：命令行接收一个问题，加载配置并调用客户端。
"""
from datetime import datetime
import json
import argparse
import openai
from pathlib import Path


from dotenv import dotenv_values

from agent_lab.config import get_config
from agent_lab.llm import make_text_model

PROJECT_ROOT = Path(__file__).resolve().parents[1]

def main():
    env = dotenv_values(PROJECT_ROOT/".env")
    parser = argparse.ArgumentParser(description="输入问题：")
    parser.add_argument("question")          # 位置参数
    parser.add_argument("--out")  # 可选参数

    args = parser.parse_args()

    config = None
    content = ""
    model_id = env.get("LLM_MODEL_ID","")
    

    try:
        config = get_config(env=env) # type: ignore
        model = make_text_model(config=config)
        messages=[]
        messages.append({"role":"user","content":args.question})
        content = model(messages) # type: ignore
        print(content)
        status = "success"
    except ValueError :
        status = "响应格式错误" if config else "配置问题"
    except openai.APITimeoutError:
        status = "超时"
    except openai.OpenAIError :
        status = "接口错误"


    path = Path(args.out)
    path.parent.mkdir(parents=True,exist_ok=True)
    with open(path,"w",encoding='utf-8') as f:
        json.dump(
            {
                "time":datetime.now().astimezone().isoformat(timespec="seconds"),
                "model":model_id,
                "status":status,
                "content":content,
                "sdk_version": openai.__version__
            },
            f,
            ensure_ascii=False,
            indent=2)
        f.write("\n")
    print(f"path:{path}")

if __name__ == "__main__":
    main()
