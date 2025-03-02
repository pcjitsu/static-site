from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    Link = "link"
    IMAGE = "image"

class TextNode(text,text_type,url):
    def __init__(self,text,text_type,url):
        self.text = text
        self.text_type = text_type
        self.url = url
    
           