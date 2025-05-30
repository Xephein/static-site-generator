import unittest

from block import *

class TestHTMLNode(unittest.TestCase):
    def test_base(self):
        md = "jdsnauidhsai"
        converted = block_to_block_type(md)
        self.assertEqual(converted, BlockType.PARAGRAPH)

    def test_heading(self):
        md = "## Heading"
        converted = block_to_block_type(md)
        self.assertEqual(converted, BlockType.HEADING)

    def test_not_heading(self):
        md = "##nonheading"
        converted = block_to_block_type(md)
        self.assertEqual(converted, BlockType.PARAGRAPH)

    def test_not_heading_2(self):
        md = "####### something"
        converted = block_to_block_type(md)
        self.assertEqual(converted, BlockType.PARAGRAPH)

    def test_code(self):
        md = "```something hsauidohusaids audsahu idhau```"
        converted = block_to_block_type(md)
        self.assertEqual(converted, BlockType.CODE)

    def test_not_code(self):
        md = "```sadsa\ndsada\nsadsa\n"
        converted = block_to_block_type(md)
        self.assertEqual(converted, BlockType.PARAGRAPH)

    def test_quote(self):
        md = ">dsadsi\n>saidsa\n>saodjsia"
        converted = block_to_block_type(md)
        self.assertEqual(converted, BlockType.QUOTE)

    def test_not_quote(self):
        md = ">dsadosao\ndsadads"
        converted = block_to_block_type(md)
        self.assertEqual(converted, BlockType.PARAGRAPH)

    def test_ul(self):
        md = "- sddad\n- sdasda\n- sad"
        converted = block_to_block_type(md)
        self.assertEqual(converted, BlockType.UNORDERED_LIST)

    def test_not_ul(self):
        md = "- sddad\n- sdasda\n-sad"
        converted = block_to_block_type(md)
        self.assertEqual(converted, BlockType.PARAGRAPH)

    def test_ol(self):
        md = "1. sdad\n2. asd"
        converted = block_to_block_type(md)
        self.assertEqual(converted, BlockType.ORDERED_LIST)

    def test_not_ol(self):
        md = "1. sdad\n2. asd\n4. sads"
        converted = block_to_block_type(md)
        self.assertEqual(converted, BlockType.PARAGRAPH)


    def test_not_ol2(self):
        md = "1. sdad\n2.asd"
        converted = block_to_block_type(md)
        self.assertEqual(converted, BlockType.PARAGRAPH)


