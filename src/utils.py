import re

from textnode import TextNode, TextType

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

