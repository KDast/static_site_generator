import unittest

from htmlnode import HTMLNode
children = []
props_test = {"href":"https://www.google.com", "target": "_blank"}


class test_HTMlNode(unittest.TestCase):
    def test_eq(self): #test props_to_html 
        props1 = HTMLNode("h1", "This is value",None, props_test)
        answer = 'href=https://www.google.com target=_blank'
        self.assertEqual(props1.props_to_html(), answer)
    
    def test_not_eq1(self): #test props_to_html w/o space between dict element
        props1 = HTMLNode("h1", "This is value",None, props_test)
        answer = 'href=https://www.google.comtarget=_blank'
        self.assertNotEqual(props1.props_to_html(), answer)

    def test_not_eq2(self): #test props_to_html w/o space between dict element
        props1 = HTMLNode("h1", "This is value",None, props_test)
        answer = 'href https://www.google.com target _blank'
        self.assertNotEqual(props1.props_to_html(), answer)






if __name__ == "__main__":
    unittest.main()