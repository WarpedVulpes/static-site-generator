from textnode import TextNode, TextType
from web_utils import copy_static_files, generate_pages_recursive

def main():
    node = TextNode('hello world', text_type=TextType.TEXT, url = 'https://www.warpedvulpes.ca')
    print(node)
    copy_static_files('./static', './public')
    generate_pages_recursive('./content', 'template.html', './public')
    



main()