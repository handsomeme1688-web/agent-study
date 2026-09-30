"""D05 学生测试：多余顶层字段必须拒绝，坏参数不得抵达工具。契约见当天任务卡。"""
import json
import unittest
from unittest.mock import patch

from agent_lab.tools import dispatch, parse_decision


class TestD05Student(unittest.TestCase):
    def test_unexpected_top_level_field(self):
        """合法 search 的输入加一个顶层多余字段 → 拒绝。"""
        obj = {'type': 'tool', 'name': 'search_docs',
               'arguments': {'query': '工具 执行'}, 'debug': 1}
        with self.assertRaises(ValueError):
            parse_decision(json.dumps(obj, ensure_ascii=False))

    def test_dispatch_bad_k_not_executed(self):
        """k 是字符串（非 int）→ 报错，且底层搜索一次都不能被调用。"""
        with patch('agent_lab.tools.search_docs') as fn:
            with self.assertRaises(ValueError):
                dispatch([], 'search_docs', {'query': 'q', 'k': '3'})
            fn.assert_not_called()

    def test_dispatch_read_chunk(self):
        """dispatch 的 read_chunk 分支：参数按位置传给 D3 的 read_chunk。"""
        with patch('agent_lab.tools.read_chunk', return_value={'id': 'a'}) as fn:
            self.assertEqual(dispatch([], 'read_chunk', {'chunk_id': 'a'}), {'id': 'a'})
            fn.assert_called_once_with([], 'a')


if __name__ == "__main__":
    unittest.main()
