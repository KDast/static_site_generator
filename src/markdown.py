from textnode import *
import re

#takes a markdown text and exports a list of textnode
old_nodes = [TextNode("This is text with a *code block* word", TextType.NORMAL), TextNode("This is text with a **code block** word", TextType.BOLD)]





def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed") # when properly delimited the length of the list created by split should always be an uneven number
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.NORMAL))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

    
text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"


def extract_markdown_images(text): # a raw text string and returns a list of tuple [(alt text, url)]
    md_img = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text) # the parenthese delimits a group thus why it returns a tuple.
    
 
    return md_img


textlink = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"

def extract_markdown_links(text): # a raw text string and returns a list of tuple [(alt text, url)]
    md_img = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text) # the parenthese delimits a group thus why it returns a tuple. (?<!!) is a negative look behind. 
    
    return md_img


node = [TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.NORMAL)]

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes: # takes all the non TestType.NORMAL nodes and puts them in a list
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue
        delimited_list = re.split(r"(!\[[^\[\]]*\]\([^\(\)]*\))", old_node.text)
        if len(delimited_list) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        list_images = extract_markdown_images(old_node.text)
        
        img_counter = 0
        split_nodes = []
        for i in range(len(delimited_list)):
            if delimited_list[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(delimited_list[i], TextType.NORMAL))
            if i % 2 != 0:
                alt_text, link = list_images[img_counter]
                split_nodes.append(TextNode(alt_text, TextType.IMAGES, link))
                img_counter += 1
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1) # when using text as a delimiter, the delimiter is omitted in the list of string returned
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.NORMAL))
            new_nodes.append(TextNode(link[0], TextType.LINKS, link[1]))
            original_text = sections[1] # updates the stirng to the text after the delimiter
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.NORMAL))
    return new_nodes




input = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.NORMAL)]
    
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


input= ("""# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item""")

def markdown_to_blocks(markdown):
    new_list = []
    string_list = markdown.split("\n\n")
    for string in string_list:
        strings = string.strip()
        if strings == "":
            continue
        
        new_list.append(strings)
    return new_list

block = "#### This is a heading"
def block_to_block(block):
    if block.startswith("# ") or block.startswith("## ") or block.startswith("### ") or block.startswith("#### ") or block.startswith("##### ") or block.startswith("###### "):
        return "heading"
    if block.startswith("```") and block.endswith("```"):
        return "code"
    if block.startswith(">"):
        is_line = True
        for line in block.split("\n"):
            if not line.startswith(">"):
                is_line = False
        if is_line:
            return "line"
        else:
            raise Exception("missing '>' in this block ")
    if block.startswith("* ") or block.startswith("- "):
        is_unordered_list = True
        for line in block.split("\n"):
            if not (line.startswith("* ") or line.startswith("- ")):
                is_unordered_list = False
        if is_unordered_list:
            return "unordered list"
        else:
            raise Exception("missing '- ' or '* ' in this block ")
    if block.startswith("1. "):
        ordered_list = True
        increment = 1
        for line in block.split("\n"):
            if line.startswith(f"{increment}. "):
                increment += 1
            else:
                ordered_list = False
        if ordered_list:
            return "ordered list"
        else:
            raise Exception("missing numbers or not ordered properly")
    else:
        return "normal paragraph"
    
def markdown_to_html_node(markdown):








        
            

                
    
        
        



