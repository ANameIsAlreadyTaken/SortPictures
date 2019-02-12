#!/usr/bin/env python3

from tkinter import filedialog
from tkinter import *
from os import listdir, rename
from os.path import isfile, join
from PIL import Image

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)

class Win:

    def __init__(self, master):
        self.folder_path = StringVar()
        
        self.master = master
        master.title("A simple GUI")

        self.folder = Label(master, textvariable=folder_path)
        self.folder.pack()
        self.browse = Button(text="Browse", command=browse_button)
        self.browse.pack()

        self.sortpic = Button(text="Sort pictures (PNG/JPEG)", command=self.sort_pictures)
        self.sortpic.pack()


        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def sort_pictures(self):
        folder = folder_path.get()
        if (folder is ""):
            return
        onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))]
        print(onlyfiles)
        for afile in onlyfiles:
            if afile.endswith((".jpg", ".jpeg", ".JPG", ".JPEG")):
                tmp = join(folder, afile)
                print(tmp)
                try:
                    date = Image.open(tmp)._getexif()[36867]
                    rename(tmp, join(folder, date.replace(' ', '_') + '.JPG'))
                except Exception as e:
                    print(e)
                    print("no date for " + afile)
                
            elif afile.endswith((".PNG", ".png")):
                pass
                

root = Tk()
folder_path = StringVar()
win = Win(root)
root.mainloop()
