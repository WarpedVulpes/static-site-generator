from node_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType
import unittest

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_bold(self):
        old_nodes = [TextNode("This is **bold** text", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_multiple(self):
        old_nodes = [TextNode("This is `code` and `more code`", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, "`", TextType.CODE)
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" and ", TextType.TEXT),
            TextNode("more code", TextType.CODE)
        ]
        self.assertEqual(new_nodes, expected_nodes)
    def test_unbalanced_delimiter(self):
        old_nodes = [TextNode("This is **bold text", TextType.TEXT)]
        with self.assertRaises(ValueError) as context:
            split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        self.assertIn("Unbalanced delimiter '**'", str(context.exception))

    def test_no_delimiter(self):
        old_nodes = [TextNode("This is normal text", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        expected_nodes = [TextNode("This is normal text", TextType.TEXT)]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_empty_list(self):
        old_nodes = []
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        expected_nodes = []
        self.assertEqual(new_nodes, expected_nodes)
    