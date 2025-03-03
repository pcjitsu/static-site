from textnode import TextNode, TextType 

def main():
    newTextnode = TextNode("This is some anchor Text", TextType.LINK, "https://www.google.com")
    print(newTextnode)

if __name__ == "__main__":
    main()  # Call main() when the script is run directly