

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
        return prop_line.rstrip()
    

    def __repr__(self):
        return f"/tag -> {self.tag} \n/value -> {self.value} \n/children-> {self.children} \n/props-> {self.props}"

