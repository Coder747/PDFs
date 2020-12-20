import os
import tkinter as tk


def getdir():
    dict = {}
    for root, dirs, files in os.walk(os.getcwd()+"\\Test"):
        dict[root] = files
    return dict

def open_pdf(filepath,filename):
    filepath += f"\\{filename}"
    os.startfile(filepath)

myfiles = getdir()

########################################################
#GUI
########################################################

root=tk.Tk()
root.geometry("350x250+700+400")

for filepath,filelist in myfiles.items():
    for filename in filelist:
        n_Button= tk.Button(root,text=filename,command = lambda: open_pdf(filepath,filename),font=('arial',15,'bold'))
        n_Button.pack()


root.mainloop()