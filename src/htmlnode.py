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
        super().__init__(tag, value=value, children = None, props=props)
    

    def to_html(self):
        if not self.value:
            raise ValueError("value cannot be empty")
        if not self.tag:
            return str(self.value)
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children = children, props=props)
    

    def to_html(self):
        if not self.children or self.children == []:
            raise ValueError("children must exist")
        if not self.tag:
            raise ValueError("tag cannot be empty")
        else:
            
            a = ""
            for child in self.children:
                    if not isinstance(child, (LeafNode, ParentNode)): #checks for supported class in to_html method
                        raise TypeError("Unsupported node type in children")
                    a += child.to_html()
            return (f"<{self.tag}{self.props_to_html()}>{a}</{self.tag}>")
