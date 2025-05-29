from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("All parent nodes must have tags")
        if self.children is None:
            raise ValueError("All parent nodes must have children")
        html_string = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            html_string += child.to_html()
        return html_string + f"</{self.tag}>"


