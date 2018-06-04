from tkinter import *

def search(event):
    print('I just tried to search', entSearch.get())

root = Tk()

# Main container
searchFrame = Frame(root)
searchFrame.pack()

fileNameFrame = Frame(root)
fileNameFrame.pack()

# Search Field
lblKeyWord = Label(searchFrame, text='Search for a keyword')
lblKeyWord.pack()
entSearch = Entry(searchFrame)
entSearch.pack(side=LEFT)

# JSON file to search in
lblFileName = Label(fileNameFrame, text='JSON file path')
lblFileName.pack()
entFileName = Entry(fileNameFrame)
entFileName.pack()

btnSearch = Button(root, text='Search', fg ='red')
btnSearch.bind('<Button-1>', search)
btnSearch.pack(side=BOTTOM)

root.mainloop()

