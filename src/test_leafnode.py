import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode




props_test1 = {"href":"https://www.google.com"}
children1 = [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ]

class test_LeafNode(unittest.TestCase):
    def test_eq(self): #value, tag, props= None
        leafnode1 = LeafNode("h1", "This is value", None)
        answer = '<h1>This is value</h1>'
        self.assertEqual(leafnode1.to_html(), answer)
    
    def test_eq1(self): #value, tag, props
        leafnode1 = LeafNode("h1", "This is value", props_test1)
        answer = '<h1 href="https://www.google.com">This is value</h1>'
        self.assertEqual(leafnode1.to_html(), answer)

    def test_eq2(self): # no tags
        leafnode1 = LeafNode("", "This is value", props_test1)
        answer = 'This is value'
        self.assertEqual(leafnode1.to_html(), answer)

    def test_not_eq2(self): #test props_to_html w/o space between dict element
        leafnode1 = LeafNode("h1", "This is value", props_test1)
        answer = '<h1 href : "https://www.google.com">This is value</h1>'
        self.assertNotEqual(leafnode1.to_html(), answer)

    def test_empty_value(self): #test value error with empty value input
        leafnode1 = LeafNode("h1", "", props_test1)
        with self.assertRaises(ValueError):
            leafnode1.to_html()




#Parent Node test------
props_test1 = {"href":"https://www.google.com"}
children1 = [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ]
children2 = [
        LeafNode("b", "Bold text"),
        LeafNode(None, ""),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ]

children3 = [
        LeafNode("b", "Bold text"),
        ParentNode("p", children1, props_test1),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ]
children4 = [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ]
children0 = []


class test_ParentNode(unittest.TestCase):
    def test_normal_case(self): #normal case
        parentnode1 = ParentNode("p",children1,)
        answer = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(parentnode1.to_html(), answer)

    def test_empty_value1_in_children(self): #test value error with empty value input inside children
            parentnode2 = ParentNode("h1", children2,)
            with self.assertRaises(ValueError):
                parentnode2.to_html()

    def test_nested_parent_node(self): #nested parent node
        parentnode3 = ParentNode("p",children3,)
        answer = (
                "<p>"\
                "<b>Bold text</b>"\
                '<p href="https://www.google.com">'\
                    "<b>Bold text</b>"\
                        "Normal text"\
                    "<i>italic text</i>"\
                        "Normal text</p>"\
                    "<i>italic text</i>"\
                        "Normal text"\
                "</p>"
            )
        self.assertEqual(parentnode3.to_html(), answer)

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

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

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",)



if __name__ == "__main__":
    unittest.main()