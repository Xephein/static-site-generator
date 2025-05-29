import unittest

from parentnode import ParentNode 
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_w_grandchildren_w_props(self):
        grandchild_a_node = LeafNode("b", "grandchild a", {"family": "one"})
        grandchild_b_node = LeafNode("i", "grandchild b", {"family": "one"})
        grandchild_c_node = LeafNode("yellow", "grandchild c", {"family": "two"})
        child_a_node = ParentNode("p", [grandchild_a_node, grandchild_b_node], {"family": "one"})
        child_b_node = LeafNode("green", "child b", {"family": "three"})
        child_c_node = ParentNode("span", [grandchild_c_node], {"family": "two"})
        parent_node = ParentNode("div", [child_a_node, child_b_node, child_c_node])
        self.assertEqual(
            parent_node.to_html(),
            '<div><p family="one"><b family="one">grandchild a</b><i family="one">grandchild b</i></p><green family="three">child b</green><span family="two"><yellow family="two">grandchild c</yellow></span></div>'
        )

    def test_parent_w_no_child(self):
        with self.assertRaises(ValueError):
            node = ParentNode("p", None).to_html()
        
    def test_parent_w_no_tag(self):
        with self.assertRaises(ValueError):
            node = ParentNode(None, []).to_html()




if __name__ == "__main__":
    unittest.main()
