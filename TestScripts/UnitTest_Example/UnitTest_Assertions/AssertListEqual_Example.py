import unittest


class TestListElements(unittest.TestCase):
    def setUp(self):
        self.expected = ['foo', 'bar', 'baz']
        self.result = ['foo', 'bar', 'baz']

    def test_count_eq(self):
        """Will succeed"""
        self.assertCountEqual(self.result, self.expected)

    def test_list_eq(self):
        """Will fail"""
        self.assertListEqual(self.result, self.expected)

if __name__ == "__main__":
    unittest.main()