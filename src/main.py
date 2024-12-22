from textnode import *
from htmlnode import HTMLNode, LeafNode

def main():

    props_test = {"href":"https://www.google.com", "target": "_blank"}
    object = TextNode("This is a test", TextType.BOLD, "https://www.boot.dev")
    props1 = LeafNode("h1", "This is value", props_test)
    
    print(props1.to_html())













main()