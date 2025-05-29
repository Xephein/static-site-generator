import unittest

from leafnode import LeafNode
from textnode import TextNode, TextType
from utils import split_nodes_delimiter


class TestTextConversion(unittest.TestCase):
    def test_bold_text(self):
        old_nodes = [TextNode("This is a **bold** text block", TextType.NORMAL)]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("This is a ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" text block", TextType.NORMAL)
        ])

    def test_italic_text(self):
        old_nodes = [TextNode("This is a _ITALIC_ text block", TextType.NORMAL)]
        new_nodes = split_nodes_delimiter(old_nodes, "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [
            TextNode("This is a ", TextType.NORMAL),
            TextNode("ITALIC", TextType.ITALIC),
            TextNode(" text block", TextType.NORMAL)
        ])

    def test_code_text(self):
        old_nodes = [TextNode("This is a `CODE` text block", TextType.NORMAL)]
        new_nodes = split_nodes_delimiter(old_nodes, "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is a ", TextType.NORMAL),
            TextNode("CODE", TextType.CODE),
            TextNode(" text block", TextType.NORMAL)
        ])

    def test_mult_code_text(self):
        old_nodes = [
            TextNode("`CODE` This is a `CODE` text `CODE` block", TextType.NORMAL)
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("CODE", TextType.CODE),
            TextNode(" This is a ", TextType.NORMAL),
            TextNode("CODE", TextType.CODE),
            TextNode(" text ", TextType.NORMAL),
            TextNode("CODE", TextType.CODE),
            TextNode(" block", TextType.NORMAL)
        ])

    def test_mult_nodes(self):
        old_nodes = [
            TextNode("This is a `CODE` text block", TextType.NORMAL),
            TextNode("This is **bold** and this is `CODE`", TextType.NORMAL)
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is a ", TextType.NORMAL),
            TextNode("CODE", TextType.CODE),
            TextNode(" text block", TextType.NORMAL),
            TextNode("This is **bold** and this is ", TextType.NORMAL),
            TextNode("CODE", TextType.CODE)
        ])

if __name__ == "__main__":
    unittest.main()
