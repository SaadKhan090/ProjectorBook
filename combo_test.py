from html.parser import HTMLParser
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import RPi.GPIO as GPIO

index = -1  # Specific html document we want

def button_callback(channel):
    global index
    print("Button was pushed!")
    index = index+1
    
    
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(15,GPIO.IN) #use gpio 15 which is pin 10, not pin 15
#normally open switch, falling=when pushed down, rising=when released
GPIO.add_event_detect(15,GPIO.FALLING,callback=button_callback)


book = epub.read_epub('pg28885.epub')
#bookimages = epub.read_epub('pg28885-images.epub')

prev_index = -1

ctr = 0

while (index < 15):
    if index != prev_index:
        ctr = 0
        for doc in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
            if ctr == index:
                #print(doc.get_body_content())
                soup = BeautifulSoup(doc.get_body_content(),'html.parser')
                print(soup.get_text())
                print("LENGTH OF CHAPTER -> {}".format(len(soup.get_text())))
            ctr += 1
            
        prev_index = index
            
        

        
        






message = input("Press enter to quit\n\n")