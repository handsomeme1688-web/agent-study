# D01 补课：文件和JSONL

本次编写的补课讲义，不是 Hello-Agents 原文。例子与通过线属于课程设计。

## 官方补充资料
- Python 3.12 中文教程，7.2、7.2.1、7.2.2：https://docs.python.org/zh-cn/3.12/tutorial/inputoutput.html#reading-and-writing-files
- 不会定义函数时只补4.8：https://docs.python.org/zh-cn/3.12/tutorial/controlflow.html#defining-functions

## 今日只学以下内容
### 1. 先读一段文本
文件路径是字符串；文件内容也是字符串，它们不是同一个东西。
先写一个五行以内的实验，读取当天样例，再观察 repr(text)。
```python
from pathlib import Path
p = Path.home() / "agent-study/repo-qa-agent/fixtures/mini.md"
with p.open("r", encoding="utf-8") as handle:
    text = handle.read()
print(type(text), repr(text))
```
上面是读文件的演示，不是两个正式作业函数的完整答案。
读不存在的路径时，不要返回空字符串掩盖错误；D1契约要求FileNotFoundError。
### 2. JSON与JSONL
json.dumps把一个Python对象编码为JSON字符串；json.loads做相反过程。
JSONL在本课程中约定每条记录一个物理行。字典中字符串本身的换行由JSON编码器转义。
请观察下面这条结果的repr，而不是直接猜文件会有几行。
```python
import json
encoded = json.dumps({"text": "工具\n下一行"}, ensure_ascii=False)
print(repr(encoded))
```
write_jsonl用w覆盖；循环处理records；每次写一条编码结果后再写一个换行。
父目录不一定存在，写文件前创建父目录，exist_ok=True允许目录已经存在。
### 3. 如何写边界测试
只在 tests/test_d01_extra.py（完整路径见日卡）补自己的测试，不修改给定测试。
使用TemporaryDirectory，在其中建中文目录；写入中文文件；调用自己的read_text；用assertEqual比较。
不要把预期写成“程序不报错”就算通过；预期必须是准确的文本或异常类型。

## 停止条件
能说明输入、返回值、一个失败分支；回到当天作业实现，不继续拓展新框架。
