from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror
filen = NONE

def new():
    global filen
    filen = "Untitled"
    text.delete("1.0", END)
    root.title(filen)

def save():
    data = text.get("1.0",END)
    file = open(filen, 'w')
    file.write(data)
    file.close()
    root.title(filen)

def save_as():
    file = asksaveasfile(mode = 'w',defaultextension="txt")
    root.title(file.name)
    data = text.get("1.0", END)
    try:
        file.write(data.rstrip())
    except:
        showerror(title="Eror", message = "Saving file error")
    
def openf():
    global filen
    op = askopenfile(mode="r")
    root.title(op.name)
    if op is None:
        return
    filen = op.name
    data = op.read()
    text.delete("1.0", END)
    text.insert("1.0", data)
    
def info():
    showerror(title="info", message = "v Betta 0.1")

def exits():
    quit()
def ewp():
    h = text.get("1.0", END)
    eval(h)

root = Tk()
root.title("Untitled")

root.minsize(width = 500, height = 500)
root.maxsize(width = 500, height = 500)

text = Text(root, width = 400, height = 400,wrap="word")
scr = Scrollbar(root, orient=VERTICAL, command=text.yview)
scr.pack(side="right", fill="y")
text.configure(yscrollcommand=scr.set)
text.pack()








menu = Menu(root)
root.configure(menu=menu)

File = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=File)
File.add_command(label="New", command = new)
File.add_command(label="Open", command = openf)
File.add_command(label="Save", command = save)
File.add_command(label="Save as", command = save_as)

Info = Menu(menu, tearoff=0)
menu.add_cascade(label="Info", menu=Info)
Info.add_command(label="Info", command = info)

Edit = Menu(root, tearoff=0)
menu.add_cascade(label="Edit", menu=Edit)
Edit.add_command(label = "With Python", command = ewp)

Exit = Menu(menu, tearoff=0)
menu.add_cascade(label="Exit", menu=Exit)
Exit.add_command(label="Exit", command = exits)

root.mainloop()
