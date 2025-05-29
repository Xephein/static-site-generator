

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def __eq__(self, target):
        a = self.tag == target.tag
        b = self.value == target.value
        c = self.children == target.children
        d = self.props == target.props
        return a and b and c and d

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props is None:
            return ""
        return "".join(map(lambda key: f' {key}="{self.props[key]}"', self.props))

