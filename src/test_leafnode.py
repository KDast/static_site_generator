import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode




props_test1 = {"href":"https://www.google.com"}
children1 = [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],

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
class test_ParentNode(unittest.TestCase):
    def test_eq(self): #normal case
        parentnode1 = ParentNode("p",children1,)
        answer = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(parentnode1.to_html(), answer)




if __name__ == "__main__":
    unittest.main()