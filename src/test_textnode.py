import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_different_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This i a text node", TextType.BOLD)
        self.assertNotEqual(node,node2)
    def test_different_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node,node2)
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.bootdev.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.bootdev.com")
        self.assertEqual(node, node2)
    def test_different_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "www.bootdev.com")
        self.assertNotEqual(node,node2)


    def test_textnode_to_HTML_Normal(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        node2 = LeafNode(None, "This is a text node", None)
        self.assertEqual(node.text_node_to_html_node(), node2)
    def test_textnode_to_HTML_Bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = LeafNode("b", "This is a text node", None)
        self.assertEqual(node.text_node_to_html_node(), node2)
    def test_textnode_to_HTML_Italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = LeafNode("i", "This is a text node", None)
        self.assertEqual(node.text_node_to_html_node(), node2)
    def test_textnode_to_HTML_link(self):
        node = TextNode("This is a text node", TextType.LINKS, "www.bootdev.com")
        node2 = LeafNode("a", "This is a text node", {"href":"www.bootdev.com"})
        self.assertEqual(node.text_node_to_html_node(), node2)

   
if __name__ == "__main__":
    unittest.main()