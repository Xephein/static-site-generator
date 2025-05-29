import unittest

from utils import extract_markdown_images, extract_markdown_links


class TestHTMLNode(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links("link [hello](world)")
        self.assertListEqual([("hello", "world")], matches)

    def test_extr_md_link_w_image(self):
        matches = extract_markdown_links("link [hello](world) ![image](here)")
        self.assertListEqual([("hello", "world")], matches)

    def test_extr_md_mult_link(self):
        matches = extract_markdown_links("[a](b) and [c](d)")
        self.assertListEqual([("a", "b"), ("c", "d")], matches)

    def test_extr_md_mult_image(self):
        matches = extract_markdown_images("![a](b) and ![c](d)")
        self.assertListEqual([("a", "b"), ("c", "d")], matches)

