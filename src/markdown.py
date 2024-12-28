from textnode import *
import re

#takes a markdown text and exports a list of textnode
old_nodes = [TextNode("This is text with a *code block* word", TextType.NORMAL), TextNode("This is text with a **code block** word", TextType.BOLD)]





def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes: # takes all the non TestType.NORMAL nodes and puts them in a list
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
    md_img = re.findall(r"\!\[.*?\]\(.*?\)", text)
    list_imgs = []
    for img in md_img:
        alt_text = re.findall(r"\!\[([^]]+)\]", img)
        url = re.findall(r"\(([^]]+)\)", img)
        list_imgs.append((alt_text[0], url[0]))
    return list_imgs
print(extract_markdown_images(text))

textlink = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"

def extract_markdown_links(text): # a raw text string and returns a list of tuple [(alt text, url)]
    md_img = re.findall(r"\[.*?\]\(.*?\)", text)
    list_links = []
    for img in md_img:
        anchor_text = re.findall(r"\!\[([^]]+)\]", img)
        url = re.findall(r"\(([^]]+)\)", img)
        list_links.append((anchor_text[0], url[0]))
    return list_links