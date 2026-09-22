# 卡住后才打开：三级提示

先自己尝试20分钟。每次只看一级；根据提示继续写10分钟，不要一次读完。

## D1
一级：先让 read_text 返回全文，再做写出；不要在同一函数里做分块。
二级：阅读 `with open(path, encoding="utf-8")`；写出时对每个字典调用 `json.dumps`。
三级：先 `Path(path).parent.mkdir(parents=True, exist_ok=True)`，以 `w` 模式打开；每个序列化对象后写一个 `\n`，`ensure_ascii=False`。坏路径直接让读操作抛出 FileNotFoundError，不用捕获所有异常。

## D2
一级：先在纸上写出 mini.md 的标题行 1、4、7；每块终点是下一标题行减1。
二级：先收集“块起点”，不要边扫描边写 JSON 文件。行号用 enumerate(..., start=1)。
三级：`lines=text.splitlines()`；得到起点列表后，用下一起点减1或len(lines)做终点；Python切片是`lines[start-1:end]`。不要忘记最后一块；重复标题不能拿标题当唯一ID。当前练习是限定格式，不是完整Markdown解析器。

## D3
一级：第一版只搜一个词，打印每个片段的匹配情况。
二级：把query变成set(query.casefold().split())，每个词只算一次；零分不要返回。
三级：先 `(score, chunk)` 暂存，再按 `(-score, chunk['id'])` 排序；返回 `dict(chunk, score=score)`，不能给原始chunk直接加score。`type(k) is int` 可避免把True当1。

## D4
一级：配置校验与网络调用分开，先通过离线测试。
二级：对三个必填环境变量逐一取值、strip、检查空白。
三级：返回键名是 api_key/base_url/model；值来自LLM_API_KEY/LLM_BASE_URL/LLM_MODEL_ID。报错只说缺哪个字段，绝不能打印api_key。通过这些测试不等于已经接通真实模型。

## D5
一级：先解析type，再分tool/final，不要一个函数同时推理和执行。
二级：JSON语法正确只是第一关；下一关是名称白名单、参数类型、数值范围和允许字段。
三级：把“解析+验证”写成纯函数；dispatch用同一验证逻辑二次检查，然后只在两个固定名称里分支。不要用eval、exec、globals，也不要把read_chunk改为任意路径读取。

## D6
一级：先完成“模型直接给final”的路径，再接一次tool，最后才做边界。
二级：每轮做 调模型→解析→结束或执行工具→保存结果。下一轮模型必须真的收到上一轮工具输出。
三级：用for range(max_steps)避免无限循环；每个run创建独立messages。定义清楚步骤数统计的是模型调用，不是工具调用。SDK的网络超时另设，Python循环步数上限不能打断一个正在阻塞的网络请求。

## 一条求助消息应包括
当天任务ID、系统/Python版本、运行命令、最小相关代码、完整错误末尾、预期输出、已尝试方法。删除密钥和私人数据。请求“先给一个定位提示，不要重写整个项目”。
