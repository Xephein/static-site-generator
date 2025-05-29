import unittest

from textnode import TextNode, TextType
from utils import split_nodes_image, split_nodes_link


class TestHTMLNode(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual([
            TextNode("This is text with an ", TextType.NORMAL),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.NORMAL),
            TextNode(
                 "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            ),
        ], new_nodes)

    def test_split_links(self):
        node = TextNode("a [b](c) d ![e](f) g [h](i) k", TextType.NORMAL)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([
            TextNode("a ", TextType.NORMAL),
            TextNode("b", TextType.LINK, "c"),
            TextNode(" d ![e](f) g ", TextType.NORMAL),
            TextNode("h", TextType.LINK, "i"),
            TextNode(" k", TextType.NORMAL),
        ], new_nodes)

    def test_split_images_same(self):
        node = TextNode("a ![b](c) and ![b](c) and [y](y)", TextType.NORMAL)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([
            TextNode("a ", TextType.NORMAL),
            TextNode("b", TextType.IMAGE, "c"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("b", TextType.IMAGE, "c"),
            TextNode(" and [y](y)", TextType.NORMAL)
        ], new_nodes)

    def test_split_links_mult_nodes(self):
        nodes = [
            TextNode("[a](a) b [b](b)", TextType.NORMAL),
            TextNode("![yo](ho)", TextType.NORMAL),
            TextNode("c [c](c), d", TextType.NORMAL)
        ]
        new_nodes = split_nodes_link(nodes)
        self.assertListEqual([
            TextNode("a", TextType.LINK, "a"),
            TextNode(" b ", TextType.NORMAL),
            TextNode("b", TextType.LINK, "b"),
            TextNode("![yo](ho)", TextType.NORMAL),
            TextNode("c ", TextType.NORMAL),
            TextNode("c", TextType.LINK, "c"),
            TextNode(", d", TextType.NORMAL),
        ], new_nodes)

    def test_links_adj(self):
        node = TextNode("[a](b)[c](d)", TextType.NORMAL)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([
            TextNode("a", TextType.LINK, "b"),
            TextNode("c", TextType.LINK, "d"),
        ], new_nodes)


