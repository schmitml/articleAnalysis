from tkinter import *
from tkinter.filedialog import askopenfilename

class SearchGui():
    
    def onselect(self, evt):
        # Note here that Tkinter passes an event object to onselect()
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        print ('You selected item %d: "%s"' % (index, value))

    # Take a string and add it as an entry to a Listbox
    def btnAddSite(self, event, lb):
        filename = askopenfilename()
        fileNameSplit = filename.split('/')
        lb.insert(END,fileNameSplit[len(fileNameSplit)-1])

    def btnSearch(self, event, ent):
        print('I searched for ' + ent.get())

    def createSiteList(self, frame, col):
        # Create file list
        lbFileList = Listbox(frame, name='fileList')
        lbFileList.bind('<<ListboxSelect>>', self.onselect)
        lbFileList.grid(column=col,row=0,rowspan=3)

        # Create add site button
        btnAddSite = Button(frame, text='Add Site', fg='red')
        btnAddSite.grid(column=col,row=3)
        btnAddSite.bind('<ButtonPress-1>', lambda event, arg=lbFileList: self.btnAddSite(event,arg))

    def createSearchBox(self, frame, col):
        # Search Field
        lblKeyWord = Label(frame, text='Search for a keyword')
        lblKeyWord.grid(column=col, row=0,columnspan=2)
        entSearch = Entry(frame)
        entSearch.grid(column=col+1, row=1,sticky=E)
        
        btnSearch = Button(frame, text='Search', fg='red')
        btnSearch.bind('<ButtonPress-1>', lambda event, arg=entSearch: self.btnSearch(event, arg))
        btnSearch.grid(column=col,row=1,sticky=W)

    def __init__(self):
        root = Tk()
        self.createSiteList(root, 0)
        self.createSearchBox(root,1)
        root.mainloop()

def main(*args):
    mSearchGui = SearchGui()

if __name__ == '__main__':
    main(*sys.argv[1:])

