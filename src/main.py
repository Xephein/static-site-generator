from os import mkdir, listdir, path
from shutil import copy, rmtree

from textnode import TextNode, TextType
from utils import markdown_to_html_node

def static_to_public(directory=""):
    static_path = path.join("./static", directory)
    public_path = path.join("./public", directory)

    if path.exists(public_path):
        rmtree(public_path)
    mkdir(public_path)
    for item in listdir(static_path):
        src = path.join(static_path, item)
        dest = path.join(public_path, item)
        if path.isfile(src):
            print("filing", path.join(static_path, item))
            copy(src, dest)
        else:
            print("dirring")
            static_to_public(item)

def main():
    static_to_public()

if __name__ == "__main__":
    main()