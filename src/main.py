import sys

from textnode import TextNode, TextType
from web_utils import copy_static_files, generate_pages_recursive

def main():
    if len(sys.argv) < 2:
        basepath = '/'
    else:
        basepath = sys.argv[1]
    
    node = TextNode('hello world', text_type=TextType.TEXT, url = 'https://www.warpedvulpes.ca')
    print(node)
    copy_static_files('./static', './docs')
    generate_pages_recursive('./content', 'template.html', './docs', basepath)
    



main()