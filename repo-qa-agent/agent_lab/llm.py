from openai import OpenAI


def make_text_model(config: dict) -> object:
    """D04：创建非流式客户端并返回model(messages)->str。"""
    client = OpenAI(api_key=config['api_key'],base_url=config['base_url'],timeout=30,max_retries=0)
    def model(messages)-> str:
        response = client.chat.completions.create(
            model=config['model'],
            stream=False,
            messages=messages
        )
        if not response.choices :
            raise ValueError("choices为空！")
        content = response.choices[0].message.content
        if content :
            return content 
        else:
           raise ValueError("content为空")
    return model


