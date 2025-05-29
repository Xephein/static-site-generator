import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_node_with_props(self):
        node = LeafNode("p", "Hello, world", {1: 2})
        self.assertEqual(node.to_html(), '<p 1="2">Hello, world</p>')

    def test_leaf_to_html_table(self):
        node = LeafNode("table", "hello", {"apples": "pears"})
        self.assertEqual(node.to_html(), '<table apples="pears">hello</table>')



if __name__ == "__main__":
    unittest.main()
