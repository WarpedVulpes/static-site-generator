from textnode import TextNode, TextType
from copy_static import copy_static_files

def main():
    node = TextNode('hello world', text_type=TextType.TEXT, url = 'https://www.warpedvulpes.ca')
    print(node)
    copy_static_files('./static', './public')


main()