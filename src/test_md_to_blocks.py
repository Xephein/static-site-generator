import unittest

from textnode import *
from utils import *


class TestTextConversion(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ])

    def test_base(self):
        md = """
paragraph

- List
- whitespaced  

p
"""
        blocks = markdown_to_blocks(md)
        self.assertListEqual([
            "paragraph",
            "- List\n- whitespaced",
            "p"
        ], blocks)

    def test_empty_lines(self):
        md = """
p





other p





"""
        blocks = markdown_to_blocks(md)
        self.assertListEqual([
            "p",
            "other p"
        ], blocks)

            

if __name__ == "__main__":
    unittest.main()
