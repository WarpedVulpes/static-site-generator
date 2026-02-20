from htmlnode import HTMLnode, LeafNode, ParentNode
from markdown_to_blocks import markdown_to_blocks
from block_types import block_to_blocktype, BlockType
from text_to_textnodes import text_to_textnodes
from text_to_html import text_node_to_html_node
from textnode import TextNode, TextType


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    if not blocks:
        return ParentNode("div", [])
    
    for block in blocks:
        block_type = block_to_blocktype(block)
        html_node = None

        if block_type == BlockType.PARAGRAPH:
            children = text_to_children(block.replace("\n", " "))
            html_node = ParentNode("p", children)
            

        elif block_type == BlockType.UNORDERED_LIST:
            lines = block.split('\n')
            list_items = []
            for line in lines:
                item_text = line.lstrip("- ").strip()
                children = text_to_children(item_text)
                list_items.append(ParentNode("li", children))
            html_node = ParentNode("ul", list_items)

        elif block_type == BlockType.ORDERED_LIST:
            lines = block.split('\n')
            list_items = []
            for line in lines:
                item_text = line.lstrip("0123456789. ").strip()
                children = text_to_children(item_text)
                list_items.append(ParentNode("li", children))
            html_node = ParentNode("ol", list_items)

        elif block_type == BlockType.HEADING:
            level = 0
            for char in block:
                if char == "#":
                    level += 1
                else:
                    break
            heading_text = block[level:].strip()
            children = text_to_children(heading_text)
            html_node = ParentNode(f"h{level}", children)

        elif block_type == BlockType.QUOTE:
            lines = block.split('\n')
            quote_lines = [line.lstrip(">").strip() for line in lines]
            quote_text = " ".join(quote_lines)
            children = text_to_children(quote_text)
            html_node = ParentNode("blockquote", children)

        elif block_type == BlockType.CODE:
            lines = block.splitlines()
            content = "\n".join(lines[1:-1]) + "\n"
            code = TextNode(content, TextType.CODE)
            html_node = ParentNode("pre", [text_node_to_html_node(code)])



        


        if html_node:
            html_nodes.append(html_node)


    parent_div = ParentNode("div", html_nodes)
    return parent_div
        




def text_to_children(text):
    textnodes = text_to_textnodes(text)
    children = []
    for textnode in textnodes:
        children.append(text_node_to_html_node(textnode))
    return children

