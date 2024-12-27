from textnode import *
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():

    props_test = {"href":"https://www.google.com", "target": "_blank"}
    object = TextNode("This is a test", TextType.BOLD, "https://www.boot.dev")
    props1 = LeafNode("h1", "This is value", props_test)
    props_test1 = {"href":"https://www.google.com"}
    children1 = [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ]
    parentnode1 = ParentNode("p", children1, props_test1)
   
    text_node_to_convert = TextNode("HEllo",TextType.BOLD, None)
    print(text_node_to_convert.text_node_to_html_node())












main()