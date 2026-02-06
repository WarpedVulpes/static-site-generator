import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtraction(unittest.TestCase):

    def test_extract_markdown_images(self):
            matches = extract_markdown_images(
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
            )
            self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_markdown_links(self):
          matches = extract_markdown_links(
                "This is a link with [anchor text](https://www.warpedvulpes.ca)"
          )
          self.assertListEqual([("anchor text", "https://www.warpedvulpes.ca")], matches)

    def test_neq_alt_markdown_images(self):
          matches = extract_markdown_images(
                "this is text with an ![incorrect](https://i.imgur.com/zjjcJKZ.png)"
          )
          self.assertNotEqual([("correct", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_neq_url_markdown_images(self):
          matches = extract_markdown_images(
                "this is text with an ![correct](https://i.imgur.com/zjjcJKZ.jpg)"
          )
          self.assertNotEqual([("correct", "https://i.imgur.com/zjjcJKZ.png")], matches)