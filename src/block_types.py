from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'

def block_to_blocktype(block):
    lines = block.split('\n')

    if re.match(r'^#{1,6} ', block):
        return BlockType.HEADING
    elif block.startswith('```\n') and block.endswith('```'):
        return BlockType.CODE
    elif block.startswith('> ' or '>'):
        return BlockType.QUOTE
    elif all(line.startswith('- ') for line in lines):
        return BlockType.UNORDERED_LIST
    
    is_ordered_list = True
    for i, line in enumerate(lines):
        if not line.startswith(f"{i + 1}. "):
            is_ordered_list = False
            break
    if is_ordered_list:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH