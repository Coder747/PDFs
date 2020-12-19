import directory as dir
import webbrowser as wb
import tkinter as tk
import os

def getdir():
    dict = {}
    for root, dirs, files in os.walk(os.getcwd()+"\\Test"):
        dict[root] = files
    return dict

myfiles = dir.getdir()

def get_name(str):
    index= str.rfind("\\")
    return str[index+1:len(str)]

def open_pdf(s):
    wb.open_new(s)
#-----------------------------------------------------#
root=tk.Tk()
frame=tk.Frame(root)
frame.pack()
#   root.title("program")
root.geometry("350x250+700+400")

for name in myfiles:
    str = get_name(name)
    newButton=tk.Button(root,text=str,command=lambda: open_pdf(name),font=('arial',15,'bold'))
    newButton.pack()

root.mainloop()