import unittest
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType

class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is a [link](http://example.com) and an ![image](http://example.com/image.png)."
        nodes = text_to_textnodes(text)
        expected_nodes = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "http://example.com"),
            TextNode(" and an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "http://example.com/image.png"),
            TextNode(".", TextType.TEXT)
        ]
        self.assertEqual(nodes, expected_nodes)
    
    def test_text_only(self):
        text = "Just some plain text."
        nodes = text_to_textnodes(text)
        expected_nodes = [TextNode("Just some plain text.", TextType.TEXT)]
        self.assertEqual(nodes, expected_nodes)
    
    def test_image_only(self):
        text = "![alt text](http://example.com/image.png)"
        nodes = text_to_textnodes(text)
        expected_nodes = [TextNode("alt text", TextType.IMAGE, "http://example.com/image.png")]
        self.assertEqual(nodes, expected_nodes)
    
    def test_mixed_content(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        expected_nodes = [
    TextNode("This is ", TextType.TEXT),
    TextNode("text", TextType.BOLD),
    TextNode(" with an ", TextType.TEXT),
    TextNode("italic", TextType.ITALIC),
    TextNode(" word and a ", TextType.TEXT),
    TextNode("code block", TextType.CODE),
    TextNode(" and an ", TextType.TEXT),
    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and a ", TextType.TEXT),
    TextNode("link", TextType.LINK, "https://boot.dev"),
]