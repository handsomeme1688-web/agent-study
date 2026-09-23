import re

def split_markdown(text: str, source: str) -> list[dict]:
    """D2：仅支持行首 # 到 ###### + 空格的标题；每个标题另起一块。
    行号从 1 起、两端包含；块正文含标题及所属空行。
    标题前的非空前言用 title='未分节'；全空白输入返回 []。
    字段：id, source, title, start_line, end_line, text。
    id 规则：f'{source}#L{start_line}-L{end_line}'。
    D2 不支持围栏代码块；D9 再扩展，README 必须说明边界。
    """

    chunks = []
    start_lines=[]
    texts = text.splitlines()
    # 1. 遍历收集标题起点
    for i, line in enumerate(texts):
        # 判断是否是一个标题
        if line.lstrip().startswith("#"):
            count = 0
            count_space = 0
            for char in line:

                if char == "#":
                    count += 1
                    count_space += 1
                elif char == " ":
                    count_space += 1
                else:
                    break
            if count_space > count  and 0 < count < 7:
                # 这是一个标题
                # 记录起点（行号）
                start_line = i+1
                # 取标题
                title = line.lstrip().lstrip("#").lstrip()
                start_lines.append([title,start_line])
                # 标题也要累加进 text
                # chunk_text += line
        else:
            continue
            # chunk_text += line

    # --- 未分节：这段是这次改动最大的地方 -------------------------------
    # ✗ if len(text.strip()) and start_lines == [] or start_lines[1][1]!=1:
    # ✗     start_lines.append(["未分节",1])
    #
    # 原写法三个问题：
    #   1) 解析成 (A and B) or C，C 在"左边为假"时求值——text 全空白时
    #      start_lines 可能是空的，start_lines[1] 当场 IndexError
    #   2) 想问"第一个标题不在第 1 行"，应该看 start_lines[0]，不是 [1]
    #   3) append 把块加到了最后，未分节必须在最前面 → insert(0,...)
    #      而且它的行号 1 比后面的标题行号还小，会让块的终点算出 0 或负数
    #   4) 契约要的是"标题之前有【非空文字】"，不是"第一个标题不在第 1 行"
    #
    # ✓ 拆成两种情况，都插到最前面：
    if start_lines == []:
        # 一个标题都没有：有非空正文才成块；全空白直接返回 []
        if text.strip():
            start_lines.append(["未分节", 1])
        else:
            return []
    elif "\n".join(texts[:start_lines[0][1]-1]).strip():
        # 有标题，但第一个标题【之前】还有非空文字 → 最前面插一个未分节块
        start_lines.insert(0, ["未分节", 1])

    # 防溢出
    start_lines.append(["end",len(texts)+1])
    # ✗ if len(start_lines) == 1:      # 上面的分支已经提前 return [] 了，这里不再需要
    # ✗     return []

    # ✗ for j,item in enumerate(start_lines):   # 会把末尾的哨兵 ["end", N+1] 也当成一块
    # ✓ 只遍历到哨兵之前，哨兵只用来提供"下一块的起点"
    for j in range(len(start_lines) - 1):
        item = start_lines[j]
        chunk_text=""
        title = item[0]
        start_line = item[1]
        end_line = start_lines[j+1][1]-1
        # ✗ item.append(end_line)   # 用不上：end_line 已经是局部变量了
        # ✗ for k in range(start_line-1,end_line):
        # ✗     chunk_text += texts[k]      # 逐行 += 会在结尾多出一个 "\n"
        # ✗     chunk_text += "\n"
        # ✓ 要第 start 到第 end 行，就是 texts[start-1:end] 这个切片，一次 join
        #   这一行同时修好了：越界、标题行丢失（切片第一项正是原文 "# 工具"）、结尾多换行
        chunk_text = "\n".join(texts[start_line-1:end_line])
        chunk = {"id":f'{source}#L{start_line}-L{end_line}', "source":source, "title":title, "start_line":start_line, "end_line":end_line, "text":chunk_text}
        chunks.append(chunk)
    return chunks
