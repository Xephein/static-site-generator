import unittest

from leafnode import LeafNode
from textnode import TextNode, TextType


class TestTextConversion(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        html_node = node.to_html_node()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = node.to_html_node()
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_italic(self):
        node = TextNode("Italic", TextType.ITALIC)
        html_node = node.to_html_node()
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic") 
    
    def test_CODE(self):
        node = TextNode("CODE", TextType.CODE)
        html_node = node.to_html_node()
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "CODE")
    
    def test_LINK(self):
        node = TextNode("LINK", TextType.LINK, "url")
        html_node = node.to_html_node()
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "LINK")
        self.assertEqual(html_node.props, {"href": "url"})
    
    def test_IMAGE(self):
        node = TextNode("IMAGE", TextType.IMAGE, "url")
        html_node = node.to_html_node()
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "url", "alt": "IMAGE"})


if __name__ == "__main__":
    unittest.main()
