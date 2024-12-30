from enum import Enum
from htmlnode import HTMLNode, LeafNode, ParentNode
class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "links"
    IMAGES = "images"




class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self, object):
       return (
            self.text == object.text and self.text_type == object.text_type and self.url == object.url
            )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    

#------------converts a textnode into a leafnode--------------

def text_node_to_html_node(text_node):
    match (text_node.text_type):
        case TextType.NORMAL: #convert to leafnode without any tags, text
            return LeafNode(None, text_node.text,)

        case TextType.BOLD: #convert to leafnode with "b" tag, text
            return LeafNode("b", text_node.text,)

        case TextType.ITALIC: #convert to leafnode with "i" tag, text
            return LeafNode("i", text_node.text,)

        case TextType.CODE: #convert to "code" tag. text
            return LeafNode("code", text_node.text,)

        case TextType.LINKS: #convert to "a" tag, anchor text, href prop
            return LeafNode("a", text_node.text, {"href": text_node.url})

        case TextType.IMAGES:  #convert to "img" tag, empty text, URL of images, alt text
            return LeafNode("img", "",{"src": text_node.url, "alt": text_node.text})

        case _:
            raise Exception("type not recognized")

