from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        html_string = ""
        closer = ""
        if self.tag:
            closer = f"</{self.tag}>"
            html_string += f"<{self.tag}{self.props_to_html()}>"
        html_string += self.value + closer
        return html_string
