import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_no_props(self):
        node = HTMLNode(tag="div", props={})
        self.assertEqual(node.props_to_html(), "")
    
    def test_props_to_html_with_props(self):
        node = HTMLNode(tag="a", props={"href": "https://example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com" target="_blank"')
    
    def test_props_to_html_none_props(self):
        node = HTMLNode(tag="p", props=None)
        self.assertEqual(node.props_to_html(), "")

if __name__ == "__main__":
    unittest.main()
