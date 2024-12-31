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






def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.NORMAL)]
    
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


def markdown_to_blocks(markdown):
    new_list = []
    string_list = markdown.split("\n\n")
    for string in string_list:
        strings = string.strip()
        if strings == "":
            continue
        
        new_list.append(strings)
    return new_list


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
    if block.startswith("* "): 
        for line in block.split("\n"):
            if not line.startswith("* "):
                return "paragraph"
        return "unordered list"
    if block.startswith("- "):
        for line in block.split("\n"):
            if not line.startswith("- "):
                return "paragraph"
        return "unordered list"

    if block.startswith("1. "):
        ordered_list = True
        increment = 1
        for line in block.split("\n"):
            if line.startswith(f"{increment}. "):
                increment += 1
            else:
                return "paragraph"
        if ordered_list:
            return "ordered list"
        else:
            raise Exception("missing numbers or not ordered properly")
    else:
        return "paragraph"


def markdown_node_heading(block):
    count = 0
    for letters in block[0:6]:
        if letters == "#":
            count += 1
        if letters == " ":
            break
    value = block[count+1:]
    tag = f"h{count}"
    return (tag, value)


def value_to_node(value): #takes a text (value) and returns it as a list of leafnode. the elements can be converted to html with to_html method
    text_node_value = text_to_textnodes(value) 
    leaf_list = []
    for text in text_node_value:
        leafnode = text_node_to_html_node(text)
        leaf_list.append(leafnode)
    return leaf_list # leaf_list is the children in the parent node

            
def markdown_to_html_node(markdown): #Parent HTMLNODE -> childrens = block_list, tag <div>, no props, each block should be a leafnode
# every block_type needs its associated tag and value.
    block_list = markdown_to_blocks(markdown)
    children_block_list = []
    #make one function that returns the node for each type

    for blocks in block_list:
        block_type = block_to_block(blocks)
        if block_type == "heading": #n is the number of #
            tag, value = markdown_node_heading(blocks)[0], markdown_node_heading(blocks)[1]
            children = value_to_node(value)
            block_node = ParentNode(tag, children,)
            children_block_list.append(block_node) 
        
        if block_type == "code": # should be nested inside <pre>
            tag = "code"
            value = blocks[3:-3]
            children = value_to_node(value)
            pre_nested = ParentNode(tag, children,)
            list_prenested = []
            list_prenested.append(pre_nested)
            block_node = ParentNode("pre", list_prenested) #Pre nested must be converted into a list otherwise to_html cannot iterate in block_node.to_html()
            children_block_list.append(block_node)

        if block_type == "line":
            tag = "blockquote"
            value = blocks[1:]
            children = value_to_node(value)
            block_node = ParentNode(tag, children,)
            children_block_list.append(block_node)


        if block_type == "unordered list": #will have children every line of the list should be considred as a children of the block
            list_element = blocks.split("\n")
            list_children = []
            for ele in list_element:
                value = ele[2:]
                tag = "li"
                children = value_to_node(value)
                list_children.append(ParentNode(tag, children,))
            block_node = ParentNode("ul", list_children,)
            children_block_list.append(block_node)
            

        if block_type == "ordered list": # will have children
            list_element = blocks.split("\n")
            list_children = []
            for ele in list_element:
                value = ele[3:]
                tag = "li"
                children = value_to_node(value)
                list_children.append(ParentNode(tag, children,))
            block_node = ParentNode("ol", list_children,)
            children_block_list.append(block_node)

        if block_type == "paragraph":
            tag = "p"
            value = blocks
            children = value_to_node(value)
            block_node = ParentNode(tag, children,)
            children_block_list.append(block_node)
    return ParentNode("div", children_block_list,)  
    
        

markdown = """# This is a heading

    This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
print(markdown_to_html_node(markdown).to_html())       



