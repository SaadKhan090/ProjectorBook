from html.parser import HTMLParser
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

book = epub.read_epub('pg28885.epub')
bookimages = epub.read_epub('pg28885-images.epub')

#for image in book.get_items_of_type(ebooklib.ITEM_IMAGE):
   # print(image)

desired_index = 2  # Specific html document we want
ctr = 0  # 
for doc in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
    #if ctr == desired_index:
        #print(doc.get_body_content())
        soup = BeautifulSoup(doc.get_body_content(),'html.parser')
        print(soup.get_text())
        #print(soup.prettify()) #parses the html tags and visually shows all paragrahps and italics
    #ctr += 1
    
#desired_index = 1
for img in bookimages.get_items_of_type(ebooklib.ITEM_IMAGE):
    #if ctr == desired_index:
        image_raw = img.get_content()
        print(img)
    #ctr += 1
        
        
        