import unittest

from textnode import *
from utils import *


class TestTextConversion(unittest.TestCase):
    def test_normal(self):
        text = "This is completely normal text"
        nodes = text_to_textnodes(text)
        self.assertListEqual([
            TextNode("This is completely normal text", TextType.NORMAL)
        ], nodes)

    def test_bold(self):
        text = "**bold** normal"
        nodes = text_to_textnodes(text)
        self.assertListEqual([
            TextNode("bold", TextType.BOLD),
            TextNode(" normal", TextType.NORMAL)
        ], nodes)

    def test_italic(self):
        text = "_i_ n"
        nodes = text_to_textnodes(text)
        self.assertListEqual([
            TextNode("i", TextType.ITALIC),
            TextNode(" n", TextType.NORMAL)
        ], nodes)

    def test_code(self):
        text = "`c` n"
        nodes = text_to_textnodes(text)
        self.assertListEqual([
            TextNode("c", TextType.CODE),
            TextNode(" n", TextType.NORMAL)
        ], nodes)

    def test_image(self):
        text = "n ![i](i)"
        nodes = text_to_textnodes(text)
        self.assertListEqual([
            TextNode("n ", TextType.NORMAL),
            TextNode("i", TextType.IMAGE, "i")
        ], nodes)

    def test_link(self):
        text = "[l](l) n"
        nodes = text_to_textnodes(text)
        self.assertListEqual([
            TextNode("l", TextType.LINK, "l"),
            TextNode(" n", TextType.NORMAL)
        ], nodes)

    def test_mixed(self):
        text = "**b** _i_, `c` and [l](l) ![img](img) (hello) **b t** **more** _i have `code` here_ end"
        nodes = text_to_textnodes(text)
        self.assertListEqual([
            TextNode("b", TextType.BOLD),
            TextNode(" ", TextType.NORMAL),
            TextNode("i", TextType.ITALIC),
            TextNode(", ", TextType.NORMAL),
            TextNode("c", TextType.CODE),
            TextNode(" and ", TextType.NORMAL),
            TextNode("l", TextType.LINK, "l"),
            TextNode(" ", TextType.NORMAL),
            TextNode("img", TextType.IMAGE, "img"),
            TextNode(" (hello) ", TextType.NORMAL),
            TextNode("b t", TextType.BOLD),
            TextNode(" ", TextType.NORMAL),
            TextNode("more", TextType.BOLD),
            TextNode(" ", TextType.NORMAL),
            TextNode("i have `code` here", TextType.ITALIC),
            TextNode(" end", TextType.NORMAL)
        ], nodes)

            

if __name__ == "__main__":
    unittest.main()
