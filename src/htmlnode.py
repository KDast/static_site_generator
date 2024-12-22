class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        prop_line = ""
        for prop in self.props:
            prop_line += " " + prop + "=" + f'"{self.props[prop]}"' 
        return prop_line   
    
    def __repr__(self):
        return f"/tag -> {self.tag} \n/value -> {self.value} \n/children-> {self.children} \n/props-> {self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, children = None, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError("value cannot be empty")
        if self.tag == None:
            return str(self.value)
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
