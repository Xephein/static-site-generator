from enum import Enum

from leafnode import LeafNode
from htmlnode import HTMLNode


class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, target):
        a = self.text == target.text
        b = self.text_type == target.text_type
        c = self.url == target.url
        return a and b and c

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

    def to_html_node(self):
        if self.text_type not in TextType:
            raise Exception(f"{self.text_type} is invalid")
        tag = self.text_type_to_tag()
        if self.text_type.value in ("normal", "bold", "italic", "code"):
            return LeafNode(tag, self.text)
        elif self.text_type.value == "link":
            return LeafNode(tag, self.text, {"href": self.url})
        elif self.text_type.value == "image":
            return LeafNode(tag, "", {"src": self.url, "alt": self.text})
       
    def text_type_to_tag(self):
        match self.text_type:
            case TextType.NORMAL:
                return None 
            case TextType.BOLD:
                return "b"
            case TextType.ITALIC:
                return "i"
            case TextType.CODE:
                return "code"
            case TextType.LINK:
                return "a"
            case TextType.IMAGE:
                return "img"
