from tkinter import *
from tkinter import ttk

from html.parser import HTMLParser
#import sys
#sys.path.insert(1, '/home/pi/HIP_Project/EbookLib')
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
from page import Page

LINE_LENGTH = 50
LINES_PER_PAGE = 34

# Takes entire chapter as block of text and outputs list of Page objects, 
#  corresponding to all pages of the chapter in order
def break_text_into_pages(chapter_text):
  # Get length of the chapter
  chapter_len = len(chapter_text)
  # Boolean variable to keep track of whether last character of chapter has been read
  end_of_chapter = False
  # Initialize list of pages
  page_list = []
  # While not yet reached end of chapter, add new page to page_list
  while not end_of_chapter:
    line_list = []
    # While not yet reached end of chapter AND there are fewer than 34 lines in this page, 
    #    add new line to page
    while len(line_list) < 34 and not end_of_chapter:
      # Build up new line
      line = ""
      char_ctr = 0
      last_space_index = 0
      # While not yet reached last char of chapter AND not yet hit the 50th character of line
      #    add another char to line
      while char_ctr < LINE_LENGTH+1 and not end_of_chapter:
        # if next char (char_ctr + 1) is greater than size of chapter_text, end of chapter has been
        #    reached
        if len(chapter_text) < char_ctr + 1:
          end_of_chapter = True
          # If current line has at least 1 char in it, add it to line list 
          if len(line) > 0:
            line_list.append(line)
          break
        # Get the next char (now that we know one is available)
        next_char = chapter_text[char_ctr]
        # IF next char is a SPACE, keep track of it (We may have to reset line back to here)
        if next_char == ' ':
          last_space_index = char_ctr
        if next_char == '\n':
          line_list.append(line)
          # Throw away all chapter text now in the line list
          chapter_text = chapter_text[len(line)+1:]
          break
        # if char ctr is less than LINE_LENGTH, add char to line
        if char_ctr < LINE_LENGTH:
          line += next_char
        else: # is the (LINE_LENGTH) character, verify it's a space
          if char_ctr == last_space_index:
            line_list.append(line)
            # Throw away all chapter text now in the line list
            chapter_text = chapter_text[(LINE_LENGTH+1):]
            break
          # If (LINE_LENGTH) character is not a space, reset current line back
          #    to beginning of last space (as to not cut off any word)
          else:
            # Reset line to only contain characters up to last space
            line = line[:(last_space_index)]
            line_list.append(line)
            # Throw away all chapter text now in the line list
            chapter_text = chapter_text[(last_space_index+1):]
            break
        char_ctr += 1
    # Once end of chapter or line list grows to size 34, create page from lines 
    #    and add to page list
    new_page = Page(line_list)
    page_list.append(new_page)
  # Once end of chapter has been reached, return list of all pages
  return page_list

if __name__ == "__main__":
  book = epub.read_epub('/home/pi/HIP_Project/pg28885.epub')
  bookimages = epub.read_epub('/home/pi/HIP_Project/pg28885-images.epub')

  #for image in book.get_items_of_type(ebooklib.ITEM_IMAGE):
    # print(image)
  root = Tk()
  root.title("Buk")

  mainframe = ttk.Frame(root, padding="3 3 3 3")
  mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
  root.columnconfigure(0, weight=1)
  root.rowconfigure(0, weight=1)

  left_page = Text(mainframe, font=('Verdana', 20, 'bold'), width=50, height=34)
  #left_page.insert('1.0',"text")
  left_page.grid(column=1, row=1)

  right_page = Text(mainframe, font=('Verdana', 20, 'bold'), width=50, height=34)
  right_page.grid(column=2, row=1)

  desired_index = 2  # Specific html document we want
  ctr = 0
  for doc in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
    if ctr == desired_index:
      #print(doc.get_body_content())
      chapter_text = BeautifulSoup(doc.get_body_content(),'html.parser') 
      page_list = break_text_into_pages(chapter_text.get_text())
      left_page.insert('1.0', page_list[0].get_text())
      right_page.insert('1.0', page_list[1].get_text())
      #print(soup.get_text())

    ctr += 1

  root.mainloop()
