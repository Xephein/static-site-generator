import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "hello, world", [], {})
        node2 = HTMLNode("p", "hello, world", [], {})
        self.assertEqual(node, node2)

    def test_repr(self):
        node = HTMLNode("p", "a")
        string = 'HTMLNode(p, a, None, None)'
        self.assertEqual(node.__repr__(), string)

    def test_children_not_eq(self):
        node = HTMLNode("p", "hello", ["b"])
        node2 = HTMLNode("p", "hello")
        self.assertNotEqual(node, node2)

    def test_props_eq(self):
        node = HTMLNode("a", "hello", None, {"a": "b"})
        node2 = HTMLNode("a", "hello", None, {"a": "b"})
        self.assertEqual(node, node2)

    def test_p_a_not_eq(self):
        node = HTMLNode("p", "a")
        node2 = HTMLNode("a", "a")
        self.assertNotEqual(node, node2)

    def test_props_to_html_eq(self):
        node = HTMLNode("p", "a", None, {1: 2, 2: 3})
        string = ' 1="2" 2="3"'
        self.assertEqual(node.props_to_html(), string)


if __name__ == "__main__":
    unittest.main()
