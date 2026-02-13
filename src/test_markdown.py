import unittest
from markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_empty(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_markdown_to_blocks_only_newlines(self):
        md = "\n\n\n"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])


    def test_windows_crlf_normalization(self):
        md = "Line one\r\n\r\nLine two"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Line one", "Line two"])

    def test_code_fence_with_internal_blank_line(self):
        md = """
```
line1

line2
```
"""
        blocks = markdown_to_blocks(md)
        # a fenced code block that contains blank lines should remain a single block
        self.assertEqual(blocks, ["```\nline1\n\nline2\n```"])


class TestBlockTypes(unittest.TestCase):
    def test_block_to_blocktype(self):
        from block_types import block_to_blocktype, BlockType

        self.assertEqual(block_to_blocktype("# Heading"), BlockType.HEADING)
        self.assertEqual(block_to_blocktype("## Subheading"), BlockType.HEADING)
        self.assertEqual(block_to_blocktype("### Sub-subheading"), BlockType.HEADING)
        self.assertEqual(block_to_blocktype("```\ncode\n```"), BlockType.CODE)
        self.assertEqual(block_to_blocktype("> Quote"), BlockType.QUOTE)
        self.assertEqual(block_to_blocktype("- Item 1\n- Item 2"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_blocktype("1. Item 1\n2. Item 2"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_blocktype("This is a paragraph."), BlockType.PARAGRAPH)

    