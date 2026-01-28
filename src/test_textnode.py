import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_neq_different_text(self):
        node = TextNode("this is a text node", TextType.PLAIN)
        node2 = TextNode("this is another text node", TextType.PLAIN)
        self.assertNotEqual(node, node2)
    def test_neq_different_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.PLAIN)
        self.assertNotEqual(node, node2)
    def test_eq_with_url(self):
        node = TextNode("Click here", TextType.LINKS, url="https://example.com")
        node2 = TextNode("Click here", TextType.LINKS, url="https://example.com")
        self.assertEqual(node, node2)
if __name__ == '__main__':
    unittest.main()