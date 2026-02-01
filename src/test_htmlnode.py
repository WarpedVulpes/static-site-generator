import unittest
from htmlnode import HTMLnode, LeafNode, ParentNode

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


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
        
    def test_to_html_with_props(self):
        child_node = LeafNode("i", "italic")
        parent_node = ParentNode("p", [child_node], props={"class": "test"})
        self.assertEqual(parent_node.to_html(), '<p class="test"><i>italic</i></p>')