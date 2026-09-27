"""Shared scaffolding for the 30-day interview algorithm practice.

Generated student modules contain signatures and TODOs only. The generated test
support is self-contained, so the practice project does not import these tools.
"""

import json
import re
import sys
from pathlib import Path


STRUCTURES = '''"""LeetCode-compatible linked-list, binary-tree and random-list nodes."""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random
'''


TEST_SUPPORT = '''"""Construct inputs and assert outputs; contains no exercise solutions."""

from collections import deque
from algorithms.interview._structures import ListNode, TreeNode, Node


def linked(values):
    nodes = [ListNode(value) for value in values]
    for left, right in zip(nodes, nodes[1:]):
        left.next = right
    return (nodes[0] if nodes else None), nodes


def tree(values):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    index = 1
    while queue and index < len(values):
        parent = queue.popleft()
        for side in ("left", "right"):
            if index >= len(values):
                break
            value = values[index]
            index += 1
            if value is not None:
                child = TreeNode(value)
                setattr(parent, side, child)
                queue.append(child)
    return root


def decode(value):
    if isinstance(value, dict) and "$tree" in value:
        return tree(value["$tree"])
    if isinstance(value, dict) and "$list" in value:
        return linked(value["$list"])[0]
    if isinstance(value, list):
        return [decode(item) for item in value]
    if isinstance(value, dict):
        return {key: decode(item) for key, item in value.items()}
    return value


def list_nodes(head):
    nodes, seen = [], set()
    while head is not None:
        if id(head) in seen:
            raise AssertionError("返回链表有环，无法序列化")
        seen.add(id(head))
        nodes.append(head)
        head = head.next
    return nodes


def tree_nodes(root):
    queue = deque([root] if root is not None else [])
    result, seen = [], set()
    while queue:
        node = queue.popleft()
        if id(node) in seen:
            raise AssertionError("树中存在环或重复节点引用")
        seen.add(id(node))
        result.append(node)
        queue.extend(child for child in (node.left, node.right) if child is not None)
    return result


def encode(value):
    if isinstance(value, ListNode):
        return [node.val for node in list_nodes(value)]
    if isinstance(value, TreeNode):
        tree_nodes(value)
        queue, result = deque([value]), []
        while queue:
            node = queue.popleft()
            result.append(None if node is None else node.val)
            if node is not None:
                queue.extend((node.left, node.right))
        while result and result[-1] is None:
            result.pop()
        return result
    if isinstance(value, (tuple, list)):
        return [encode(item) for item in value]
    if isinstance(value, dict):
        return {key: encode(item) for key, item in value.items()}
    return value


def compare(test, actual, case):
    actual, expected = encode(actual), case["expected"]
    comparator = case.get("comparator", "equal")
    if comparator == "unordered":
        test.assertCountEqual(actual, expected)
    elif comparator == "unordered_nested":
        test.assertCountEqual([sorted(row) for row in actual], [sorted(row) for row in expected])
    elif comparator == "any_of":
        test.assertIn(actual, expected)
    elif comparator == "approx":
        test.assertAlmostEqual(actual, expected, delta=max(abs(expected) * 1e-5, 1e-8))
    elif comparator == "equal":
        test.assertEqual(actual, expected)
    else:
        raise AssertionError(f"未知比较器：{comparator}")


def random_serial(head):
    nodes = list_nodes(head)
    index = {id(node): i for i, node in enumerate(nodes)}
    result = []
    for node in nodes:
        if node.random is not None and id(node.random) not in index:
            raise AssertionError("random 指针指向返回链表以外的节点")
        result.append([node.val, None if node.random is None else index[id(node.random)]])
    return result


def run_case(test, module, spec, case):
    kind = spec.get("kind", "function")
    if kind == "design":
        operations = case["operations"]
        arguments = case["arguments"]
        test.assertEqual(len(operations), len(arguments))
        test.assertEqual(len(operations), len(case["expected"]))
        instance = getattr(module, spec["class_name"])(*decode(arguments[0]))
        result = [None]
        for operation, args in zip(operations[1:], arguments[1:]):
            result.append(getattr(instance, operation)(*decode(args)))
        compare(test, result, case)
        return

    method = getattr(module.Solution(), spec["method"])
    if kind in ("cycle_node", "cycle_bool"):
        values, position = case["args"]
        head, nodes = linked(values)
        if position != -1:
            if not 0 <= position < len(nodes):
                raise AssertionError("非法环入口索引")
            nodes[-1].next = nodes[position]
        actual = method(head)
        if kind == "cycle_bool":
            test.assertIs(actual, case["expected"])
        else:
            expected_index = case["expected_index"]
            test.assertIs(actual, nodes[expected_index] if expected_index != -1 else None)
        return
    if kind == "intersection":
        shared, _ = linked(case["shared"])
        a, a_nodes = linked(case["a_prefix"])
        b, b_nodes = linked(case["b_prefix"])
        if a_nodes:
            a_nodes[-1].next = shared
        if b_nodes:
            b_nodes[-1].next = shared
        test.assertIs(method(a if a_nodes else shared, b if b_nodes else shared), shared)
        return
    if kind == "lca":
        values, p_value, q_value = case["args"]
        root = tree(values)
        by_value = {node.val: node for node in tree_nodes(root)}
        test.assertIs(method(root, by_value[p_value], by_value[q_value]), by_value[case["expected"]])
        return
    if kind == "random_list":
        values = case["args"][0]
        nodes = [Node(item[0]) for item in values]
        for index, (node, (_, random_index)) in enumerate(zip(nodes, values)):
            node.next = nodes[index + 1] if index + 1 < len(nodes) else None
            node.random = nodes[random_index] if random_index is not None else None
        head = nodes[0] if nodes else None
        actual = method(head)
        test.assertEqual(random_serial(actual), case["expected"])
        test.assertTrue({id(node) for node in nodes}.isdisjoint(id(node) for node in list_nodes(actual)), "必须深拷贝，不能返回原节点")
        test.assertEqual(random_serial(head), values, "拷贝完成后须恢复原链表")
        return
    if kind == "balanced_bst":
        root = method(*decode(case["args"]))
        tree_nodes(root)
        values = []
        def visit(node):
            if node is None:
                return 0
            left = visit(node.left)
            values.append(node.val)
            right = visit(node.right)
            test.assertLessEqual(abs(left - right), 1, "每个节点的左右高度差须 <= 1")
            return max(left, right) + 1
        visit(root)
        test.assertEqual(values, case["expected"])
        return
    if kind == "flatten":
        root = tree(case["args"][0])
        original = tree_nodes(root)
        method(root)
        nodes = []
        seen, cursor = set(), root
        while cursor is not None:
            test.assertNotIn(id(cursor), seen, "展开的右链存在环")
            seen.add(id(cursor))
            test.assertIsNone(cursor.left, "展开后 left 必须为 None")
            nodes.append(cursor)
            cursor = cursor.right
        test.assertEqual([node.val for node in nodes], case["expected"])
        test.assertEqual(seen, {id(node) for node in original}, "必须原地重连所有原节点")
        return
    if kind != "function":
        raise AssertionError(f"未知题目类型：{kind}")
    args = decode(case["args"])
    result = method(*args)
    if "in_place_arg" in case:
        result = args[case["in_place_arg"]]
    elif result is None and case["expected"] == [] and spec.get("returns") in {
        "Optional[ListNode]", "Optional[TreeNode]", "ListNode", "TreeNode",
        "ListNode | None", "TreeNode | None",
    }:
        # Only an empty node structure uses None; an array must really be [].
        result = []
    compare(test, result, case)
'''


def metadata_path(root):
    return Path(root) / "handbook/algorithms_110.json"


def load_catalog(root):
    return json.loads(metadata_path(root).read_text(encoding="utf-8"))


def parse_day(value):
    match = re.fullmatch(r"[Aa]?(\d{1,2})", str(value))
    if not match or not 1 <= int(match[1]) <= 30:
        raise ValueError("算法日请输入 A01–A30（也接受 1–30）")
    return int(match[1])


def select_problems(catalog, number, problem=None):
    day = catalog["days"][str(number)]
    ids = [int(value) for value in day["problem_ids"]]
    if problem is not None:
        if problem not in ids:
            raise ValueError(f"LC {problem} 不属于 A{number:02d}；当天题号：{', '.join(map(str, ids))}")
        ids = [problem]
    return day, [catalog["problems"][str(value)] for value in ids]


def problem_paths(spec):
    slug = spec["slug"].replace("-", "_")
    if not re.fullmatch(r"[a-z0-9_]+", slug):
        raise ValueError(f"非法题目 slug：{spec['slug']}")
    name = f"lc{int(spec['id']):04d}_{slug}"
    return f"algorithms/interview/{name}.py", f"algorithm_tests/interview/test_{name}.py"


def safe_path(project, relative):
    target = (Path(project) / relative).resolve()
    if not target.is_relative_to(Path(project).resolve()):
        raise ValueError(f"非法输出路径：{relative}")
    return target


def write_new(project, relative, content):
    target = safe_path(project, relative)
    if target.exists():
        print(f"KEEP   {target}")
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    print(f"CREATE {target}")


def student_source(spec):
    lines = [f'"""LC {spec["id"]} {spec["title"]}', f"题目：https://leetcode.cn/problems/{spec['slug']}/", f"重点：{spec.get('focus', '先分析输入、输出和边界。')}", f"复杂度目标：{spec.get('complexity', '写完后自行分析。')}", "只实现下面的 TODO；先在纸上写思路、边界和复杂度。", '"""', "", "from typing import Any, Optional, List, Dict, Tuple", "from algorithms.interview._structures import ListNode, TreeNode, Node", "", ""]
    design = spec.get("kind") == "design"
    lines.append(f"class {spec['class_name'] if design else 'Solution'}:")
    methods = spec["methods"] if design else [{"name": spec["method"], "params": spec.get("params", ""), "returns": spec.get("returns", "Any")}]
    for method in methods:
        params = method.get("params", "")
        returns = method.get("returns", "None") or "None"
        signature = f"self, {params}" if params else "self"
        lines.extend([f"    def {method['name']}({signature}) -> {returns}:", f"        raise NotImplementedError(\"TODO: 独立完成 LC {spec['id']} 的 {method['name']}\")", ""])
    return "\n".join(lines)


def test_source(spec):
    code, _ = problem_paths(spec)
    module = code[:-3].replace("/", ".")
    # JSON is copied into the test file so the exercise remains standalone.
    payload = {key: spec[key] for key in ("id", "kind", "method", "class_name", "returns", "cases") if key in spec}
    lines = [f'"""Fixed local cases for LC {spec["id"]}; run LeetCode after these pass."""', "", "import importlib", "import json", "import unittest", "from algorithm_tests.interview._support import run_case", "", f"SPEC = json.loads({json.dumps(payload, ensure_ascii=False)!r})", f"MODULE = importlib.import_module({module!r})", "", "", f"class LC{int(spec['id']):04d}Tests(unittest.TestCase):"]
    for index in range(len(spec["cases"])):
        lines.extend([f"    def test_case_{index + 1:02d}(self):", f"        run_case(self, MODULE, SPEC, SPEC['cases'][{index}])", ""])
    lines.extend(["", 'if __name__ == "__main__":', "    unittest.main()", ""])
    return "\n".join(lines)


def scaffold(root, project, number):
    catalog = load_catalog(root)
    day, problems = select_problems(catalog, number)
    print(f"\nA{number:02d}：{day['topic']}（{len(problems)} 题）")
    for package in ("algorithms", "algorithms/interview", "algorithm_tests", "algorithm_tests/interview"):
        write_new(project, f"{package}/__init__.py", "")
    write_new(project, "algorithms/interview/_structures.py", STRUCTURES)
    write_new(project, "algorithm_tests/interview/_support.py", TEST_SUPPORT)
    for spec in problems:
        code, test = problem_paths(spec)
        write_new(project, code, student_source(spec))
        write_new(project, test, test_source(spec))
    record = [f"# A{number:02d} 算法练习记录", "", f"主题：{day['topic']}", "", "| 题号 | 本地测试 | 力扣提交 | 独立或提示后完成 | 下次闭卷日期 |", "| --- | --- | --- | --- | --- |"]
    record.extend(f"| LC {spec['id']} {spec['title']} |  |  |  |  |" for spec in problems)
    record.extend(["", "每日仅复盘 1 道旧题，限时 10–15 分钟；复盘不重复计入 110 道独立题。", "", "今日复盘题：", "卡住的知识点：", ""])
    write_new(project, f"notes/algorithms/a{number:02d}.md", "\n".join(record))
    print("\n业务测试通过后，按下面顺序练习：")
    for index, spec in enumerate(problems, 1):
        code, _ = problem_paths(spec)
        print(f"{index}. LC {spec['id']} {spec['title']}：{safe_path(project, code)}")
        print(f"   写完单题测试：{sys.executable} {Path(root) / 'tools/check_algorithms.py'} A{number:02d} --problem {spec['id']}")
    print(f"全部完成后测试：{sys.executable} {Path(root) / 'tools/check_algorithms.py'} A{number:02d}")
    print("预期：每题 Ran N tests、OK，最终 EXIT_CODE=0；未实现的 TODO 报 NotImplementedError 是正常起点。")
    print("本地样例通过后，仍须提交力扣，并口述思路、复杂度和边界；通过样例不代表已经掌握。")
    print(f"练习记录：{safe_path(project, f'notes/algorithms/a{number:02d}.md')}")
    print(f"现在下一步（算法环节）：打开 {safe_path(project, problem_paths(problems[0])[0])}")
    return problems
