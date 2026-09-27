"""Construct inputs and assert outputs; contains no exercise solutions."""

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
