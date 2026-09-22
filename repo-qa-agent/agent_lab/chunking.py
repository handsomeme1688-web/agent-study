import re

def split_markdown(text: str, source: str) -> list[dict]:
    """D2：仅支持行首 # 到 ###### + 空格的标题；每个标题另起一块。
    行号从 1 起、两端包含；块正文含标题及所属空行。
    标题前的非空前言用 title='未分节'；全空白输入返回 []。
    字段：id, source, title, start_line, end_line, text。
    id 规则：f'{source}#L{start_line}-L{end_line}'。
    D2 不支持围栏代码块；D9 再扩展，README 必须说明边界。
    """
    raise NotImplementedError("D2: 实现 split_markdown")
