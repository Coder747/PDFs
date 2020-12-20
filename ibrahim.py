import os
import tkinter as tk

def get_name(str):
    index= str.rfind("\\") # for windows
    return str[index+1:len(str)]

def getdir():
    dict = {}
    for path, dirs, files in os.walk(os.getcwd()+"\\Test"):
        dict[path] = files
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

Folders_Button_list = []
Files_Button_list=[]

#Files
i = 0

for filepath,filelist in myfiles.items():
    for filename in filelist:
        if "pdf" in filename:
            Files_Button_list.append(tk.Button(root,text=filename,command = lambda filepath = filepath, filename = filename: open_pdf(filepath,filename),font=('arial',15,'bold')))
            Files_Button_list[i].pack()
            i+=1


#Folders
# for filepath,filelist in myfiles.items():
#     Button_list.append()
#     for filename in filelist:
#         n_Button = tk.Button(root,text=filename,command = lambda: open_pdf(filepath,filename),font=('arial',15,'bold'))
#         n_Button.pack()


root.mainloop()

'''
import webbrowser as wb
import tkinter as tk
import os

def getdir():
    dict = {}
    for root, dirs, files in os.walk(os.getcwd()): # go through the directory
        dict[root] = files # pathname : filename {}
        # print ("hello")
    return dict

myfiles = getdir() # dictionary of the files
# print(myfiles)

def get_name(str):
    index= str.rfind("\\") # for windows
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
    print(str)
    newButton=tk.Button(root,text=str,command=lambda: open_pdf(name),font=('arial',15,'bold'))
    newButton.pack()

root.mainloop()
'''