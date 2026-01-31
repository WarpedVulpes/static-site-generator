import unittest
from htmlnode import HTMLnode, LeafNode

class TestHTMLnode(unittest.TestCase):
    def test_init(self):
        node = HTMLnode(tag="div", value="Hello", children=[], props=("class", "container"))
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, ("class", "container"))

    def test_props_to_html_with_props(self):
        node = HTMLnode(props={"class": "container", "id": "main"})
        expected_html = ' class="container" id="main"'
        self.assertEqual(node.props_to_html(), expected_html)

    def test_props_to_html_without_props(self):
        node = HTMLnode()
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        node = HTMLnode(tag="p", value="Paragraph", children=None, props={"style": "color:red"})
        expected_repr = "HTMLnode(tag=p, value=Paragraph, children=None, props={'style': 'color:red'})"
        self.assertEqual(repr(node), expected_repr)

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_with_props(self):
        node = LeafNode("a", "Click Me!", props={"href": "https://warpedvulpes.ca"})
        self.assertEqual(node.to_html(), '<a href="https://warpedvulpes.ca">Click Me!</a>')
    
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "just text")
        self.assertEqual(node.to_html(), "just text")