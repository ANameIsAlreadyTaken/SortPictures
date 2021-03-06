#!/usr/bin/env python3

from tkinter import Tk, filedialog, StringVar, Label, Button
from os import listdir, rename
from os.path import isfile, join
from PIL import Image


def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
#    print(filename)


class Win:

    def __init__(self, master):
        self.folder_path = StringVar()

        self.master = master
        master.title("Pictures sorter")

        self.folder = Label(master, textvariable=folder_path)
        self.browse = Button(text="Browse", command=browse_button)
        self.sortpic = Button(
            text="Sort pictures (JPG ONLY)", command=self.sort_pictures)
        self.status = Label(root, text="Nothing wrong")
        self.nb_err_jpg = Label(root, text="Number of non sorted jpg : 0")
#PNG        self.nb_err_png = Label(root, text="Number of non sorted png : 0")
        self.sorted = Label(root, text="Sorted files : 0")
        self.close_button = Button(master, text="Close", command=master.quit)

        self.folder.pack()
        self.browse.pack()
        self.sortpic.pack()
        self.status.pack()
        self.nb_err_jpg.pack()
#PNG        self.nb_err_png.pack()
        self.sorted.pack()
        self.close_button.pack()

    def sort_pictures(self):
        folder = folder_path.get()
        if (folder is ""):
            return
        onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))]
#        print(onlyfiles)
        sorted_files = 0
        jpg_e = 0
#PNG        png_e = 0
        for afile in onlyfiles:
            if afile.lower().endswith((".jpg", ".jpeg")):
                tmp = join(folder, afile)
#                print(tmp)
                try:
                    date = Image.open(tmp)._getexif()[36867]
                    rename(tmp, join(folder, date.replace(
                        ' ', '_').replace(':', '-') + '.JPG'))
                    sorted_files += 1
                except Exception as e:
                    print(e)
                    print("No date for " + afile)
                    jpg_e += 1
                    self.status["text"] = "No date for " + afile

# Since png are not standard, getexif while rarely, or never work.
# TODO Still trying to find a clean native way to get the creation date from png files
#PNG            elif afile.endswith((".PNG", ".png")):
#PNG                tmp = join(folder, afile)
#PNG                print(tmp)
#PNG                try:
#PNG                    date = Image.open(tmp)._getexif()[36867]
#PNG                    rename(tmp, join(folder, date.replace(' ', '_') + '.PNG'))
#PNG                    sorted_files += 1
#PNG                except Exception as e:
#PNG                    print(e)
#PNG                    print("No date for " + afile)
#PNG                    png_e += 1
#PNG                    self.status["text"] = "No date for " + afile
        self.nb_err_jpg["text"] = "Number of unchanged jpg : %d" % jpg_e
#PNG        self.nb_err_png["text"] = "Number of unchanged png : %d" %  png_e
        self.sorted["text"] = "Sorted files : %d" % sorted_files


root = Tk()
folder_path = StringVar()
win = Win(root)
root.mainloop()
