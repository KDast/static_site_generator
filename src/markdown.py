from textnode import *

#takes a markdown text and exports a list of textnode
old_nodes = TextNode("This is text with a *code block* word", TextType.NORMAL)
#new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
# takes a node which has a text and a delimiter inside as well as an assigned textype. 
# Our functions analyse this node and identifies a new delimiter with a textype associated with



def split_nodes_delimiter(old_nodes, delimiter, text_type):
    
    text_node = old_nodes.text
    node_type = old_nodes.text_type
    node_url = old_nodes.url
    i = 0
    list_node = []
    if delimiter not in text_node:
        raise Exception("Invalid Markdown syntax or syntax not found")
    
    for node in text_node.split(delimiter):
        if i == 0 or i % 2 == 0:
            
            list_node.append(TextNode(node, node_type))
            
        if i % 2 != 0:
            
            list_node.append(TextNode(node, text_type))
        i += 1
    return list_node

    



print(split_nodes_delimiter(old_nodes, "*", TextType.CODE))
