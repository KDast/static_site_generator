from textnode import *
from htmlnode import HTMLNode

def main():

    props_test = {"href":"https://www.google.com", "target": "_blank"}
    object = TextNode("This is a test", TextType.BOLD, "https://www.boot.dev")
    props1 = HTMLNode("h1", "This is value",None, props_test)
    
    print(props1.props_to_html())













main()