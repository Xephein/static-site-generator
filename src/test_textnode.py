import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_bold_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_italic_eq(self):
        node = TextNode("a", TextType.ITALIC)
        node2 = TextNode("a", TextType.ITALIC)
        self.assertEqual(node, node2)

    def test_link_eq(self):
        node = TextNode("b", TextType.LINK, "url")
        node2 = TextNode("b", TextType.LINK, "url")
        self.assertEqual(node, node2)

    def test_image_not_eq(self):
        node = TextNode("c", TextType.IMAGE, "image")
        node2 = TextNode("c", TextType.IMAGE, "image2")
        self.assertNotEqual(node, node2)

    def test_normal_bold_not_eq(self):
        node = TextNode("d", TextType.NORMAL)
        node2 = TextNode("d", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_non_vs_url_not_eq(self):
        node = TextNode("e", TextType.LINK)
        node2 = TextNode("e", TextType.LINK, "url")

    def test_not_eq(self):
        node = TextNode("This is a link node", TextType.LINK, "This is a url")
        node2 = TextNode("This is an italic node", TextType.ITALIC, "This is a url")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
