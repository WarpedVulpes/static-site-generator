from textnode import TextNode, TextType

def main():
    node = TextNode('hello world', text_type=TextType.PLAIN, url = 'https://www.warpedvulpes.ca')
    print(node)

main()