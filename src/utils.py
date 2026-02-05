import re

from textnode import TextNode, TextType
from leafnode import LeafNode
from block import BlockType, block_to_block_type
from parentnode import ParentNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue
        split_nodes = node.text.split(delimiter)
        for i in range(0, len(split_nodes)):
            if i % 2 == 0:
                if split_nodes[i] == '':
                    continue
                new_nodes.append(TextNode(split_nodes[i], TextType.NORMAL))
            else:
                new_nodes.append(TextNode(split_nodes[i], text_type))
    return new_nodes


def extract_markdown_images(text):
    extracted = []
    images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    for alt_text, source in images:
        extracted.append((alt_text, source))
    return extracted


def extract_markdown_links(text):
    extracted = []
    images = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    for anchor_text, url in images:
        extracted.append((anchor_text, url))
    return extracted


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue
        node_text = node.text
        images = extract_markdown_images(node_text)
        for image in images:
            image_text = f"![{image[0]}]({image[1]})"
            sections = node_text.split(image_text, maxsplit=1)
            text = sections[0]
            if text:
                new_nodes.append(TextNode(text, TextType.NORMAL))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            node_text = sections[1]
        if node_text:
            new_nodes.append(TextNode(node_text, TextType.NORMAL))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue
        node_text = node.text
        images = extract_markdown_links(node_text)
        for image in images:
            image_text = f"[{image[0]}]({image[1]})"
            sections = node_text.split(image_text, maxsplit=1)
            text = sections[0]
            if text:
                new_nodes.append(TextNode(text, TextType.NORMAL))
            new_nodes.append(TextNode(image[0], TextType.LINK, image[1]))
            node_text = sections[1]
        if node_text:
            new_nodes.append(TextNode(node_text, TextType.NORMAL))

    return new_nodes

def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
        raise Exception(f"{text_node.text_type} is invalid")
    tag = text_node.text_type_to_tag()
    if text_node.text_type.value in ("normal", "bold", "italic", "code"):
        return LeafNode(tag, text_node.text)
    elif text_node.text_type.value == "link":
        return LeafNode(tag, text_node.text, {"href": text_node.url})
    elif text_node.text_type.value == "image":
        return LeafNode(tag, "", {"src": text_node.url, "alt": text_node.text})


def text_to_textnodes(text):
    basenode = [TextNode(text, TextType.NORMAL)]
    textnodes = split_nodes_delimiter(basenode, "**", TextType.BOLD)
    textnodes = split_nodes_delimiter(textnodes, "_", TextType.ITALIC)
    textnodes = split_nodes_delimiter(textnodes, "`", TextType.CODE)
    textnodes = split_nodes_link(textnodes)
    textnodes = split_nodes_image(textnodes)
    return textnodes

def markdown_to_blocks(markdown):
    sections = markdown.split("\n\n")
    sections = list(filter(lambda section: section != '', sections))
    sections = list(map(lambda section: section.strip(), sections))
    return sections

def markdown_to_html_node(markdown):
    content = markdown_to_blocks(markdown)
    body = ParentNode("div", [])
    for block in content:
        block = block_to_html_node(block)
        body.children = body.children + block
    return body

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return text_to_children(block, block_type)
        return ParentNode("div", html_nodes)

    elif block_type == BlockType.UNORDERED_LIST:
        html_nodes = text_to_children(block, block_type)
        return ParentNode("ul", html_nodes)

    elif block_type == BlockType.ORDERED_LIST:
        html_nodes = text_to_children(block, block_type)
        return ParentNode("ol", html_nodes)

    elif block_type == BlockType.HEADING:
        return text_to_children(block, block_type)
        return ParentNode(f"div", html_nodes)

    elif block_type == BlockType.QUOTE:
        return text_to_children(block, block_type)
        return ParentNode("div", html_nodes)

    elif block_type == BlockType.CODE:
        return text_to_children(block, block_type)
        return ParentNode("div", html_nodes)

    raise Exception("No such block type")

    
def text_to_children(block, block_type):
    if block_type == BlockType.CODE:
        content = re.sub("^```", "", block)
        content = re.sub("```$", "", content)
        content = content.strip()
        content = content + "\n"
        content = TextNode(content, TextType.CODE)
        return [ParentNode("pre", [text_node_to_html_node(content)])]

    content = re.sub("\\n", " ", block)
    content = [content.strip("\n ")]
    for idx in range(len(content)):
        if block_type == BlockType.PARAGRAPH:
            text_nodes = text_to_textnodes(content[idx])
            html_nodes = [text_node_to_html_node(x) for x in text_nodes]
            content[idx] = ParentNode("p", html_nodes)

        elif block_type == BlockType.HEADING:
            level = len(re.match("^#*", content[idx])[0])
            text_nodes = text_to_textnodes(content[idx][level + 1:])
            html_nodes = [text_node_to_html_node(x) for x in text_nodes]
            content[idx] = ParentNode(f"h{level}", html_nodes)

        elif block_type == BlockType.UNORDERED_LIST:
            content[idx] = re.sub(r"^-\s", "", content[idx])
            text_nodes = text_to_textnodes(content[idx])
            html_nodes = [text_node_to_html_node(x) for x in text_nodes]
            content[idx] = ParentNode("li", html_nodes)

        elif block_type == BlockType.ORDERED_LIST:
            content[idx] = re.sub(r"^[0-9]\.\s", "", content[idx])
            text_nodes = text_to_textnodes(content[idx])
            html_nodes = [text_node_to_html_node(x) for x in text_nodes]
            content[idx] = ParentNode("li", html_nodes)
            
        elif block_type == BlockType.QUOTE:
            content[idx] = re.sub("^>", "", content[idx]).strip()
            text_nodes = text_to_textnodes(content[idx])
            html_nodes = [text_node_to_html_node(x) for x in text_nodes]
            content[idx] = ParentNode("blockquote", html_nodes)
            
    return content














# def block_to_html_node(block):
#     block_type = block_to_block_type(block)
#     if block_type == BlockType.PARAGRAPH:
#         text_nodes = text_to_textnodes(block)
#         html_nodes = [text_node_to_html_node(x) for x in text_nodes]
#         return ParentNode("p", html_nodes)

#     if block_type == BlockType.UNORDERED_LIST:
#         html_nodes = list_to_html(block, BlockType.UNORDERED_LIST)
#         return ParentNode("ul", html_nodes)
#     if block_type == BlockType.ORDERED_LIST:
#         html_nodes = list_to_html(block, BlockType.ORDERED_LIST)
#         return ParentNode("ol", html_nodes)
#     if block_type == BlockType.HEADING:
#         idx = 0
#         while block[idx] == "#":
#             idx += 1
#         html_nodes = heading_to_html(block)
#         return ParentNode(f"h{idx}", html_nodes)
#     if block_type == BlockType.QUOTE:
#         html_nodes = quote_to_html(block)
#         return ParentNode("blockquote", html_nodes)
#     if block_type == BlockType.CODE:
#         html_nodes = code_to_html(block)
#         return ParentNode("code", [ParentNode("pre", html_nodes)])

        
#     return

# def list_to_html(block, block_type):
#     block_type = block_to_block_type(block)
#     if block_type not in (BlockType.UNORDERED_LIST, BlockType.ORDERED_LIST):
#         return block
    
#     content = block.split("\n")
#     idx = 0
#     if block_type == BlockType.UNORDERED_LIST:
#         for idx in range(len(content)):
#             content[idx] = text_to_textnodes(content[idx].replace("- ", "", 1))
#             content[idx] = ParentNode("li", content[idx])
#     if block_type == BlockType.ORDERED_LIST:
#         for idx in range(len(content)):
#             content[idx] = re.sub("^[0-9]\.\s", "", content[idx], 1)
#             content[idx] = ParentNode("li", content[idx])
#     return content

# def quote_to_html(block):
#     block = re.sub("^>", "", block, flags=re.MULTILINE)
#     block = re.sub("^\s", "", block, flags=re.MULTILINE)
#     return [text_node_to_html_node(x) for x in text_to_textnodes(block)]

# def code_to_html(block):
#     block = re.sub("^```", "", block)
#     block = re.sub("```$", "", block)
#     block = block.strip("\n")
#     return [LeafNode(None, block)]

# def heading_to_html(block):
#     block = re.sub("^#*", "", block)
#     block = block.strip()
#     return [text_node_to_html_node(x) for x in text_to_textnodes(block)]
