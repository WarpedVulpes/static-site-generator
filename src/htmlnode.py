class HTMLnode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Subclasses must implement to_html method")
    
    def props_to_html(self):
        if not self.props:
            return ""
        props_str = ""
        for key, value in self.props.items():
            props_str += f' {key}="{value}"'
        return props_str
    
    def __repr__(self):
        return f"HTMLnode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

class LeafNode(HTMLnode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)
    
    def to_html(self):
        if not self.value:
            raise ValueError("LeafNode must have a value")
        if not self.tag:
            return self.value
        props_str = self.props_to_html()
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"

class ParentNode(HTMLnode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag")
        if not self.children:
            raise ValueError("ParentNode must have children")
        props_str = self.props_to_html()
        children_html = ''.join(child.to_html() for child in self.children)
        return f"<{self.tag}{props_str}>{children_html}</{self.tag}>"

        
        