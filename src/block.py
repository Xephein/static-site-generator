from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code" 
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(md_block):
    line_num = len(md_block.split("\n"))
    if re.findall(r"^#{1,6} ", md_block):
        return BlockType.HEADING
    elif re.findall(r"^```", md_block) and re.findall(r"```$", md_block):
        return BlockType.CODE
    elif line_num == len(re.findall(r"(?m)^>", md_block)):
        return BlockType.QUOTE
    elif line_num == len(re.findall(r"(?m)^- ", md_block)):
        return BlockType.UNORDERED_LIST
    else:
        digit = 1
        for line in md_block.split("\n"):
            match = re.findall(r"^[0-9]+\.\s", line)
            if match:
                digit_current = int(match[0][:-2])
                if digit_current == digit:
                    digit += 1
                else:
                    return BlockType.PARAGRAPH
            else:
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
    

