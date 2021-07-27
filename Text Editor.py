from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

root = Tk()
root.title('Untitled - Text Editor')

text = Text(root, heigh=30, width=60)
text.pack(side=TOP, fill=X, expand=True)
text.focus_set()
file1 = 0
# ox = root.winfo_screenwidth()
# print(ox)
# root.geometry('1000x600')


def delete():
    text.delete(1.0, 'end')
    # text.window_create(1.0)
    # text.edit_modified()
    # text.edit_undo()


def redo():
    text.edit(redo)


def undo():
    text.edit(undo)


def new_file():
    root.title('Untitled - Text Editor')
    text.delete(1.0, 'end')


def open_folder():
    folder = filedialog.askdirectory(initialdir="/", title='Select Folder')
    # folder.pack()


def open_file():
    global file1
    file1 = filedialog.askopenfilename(initialdir="/", title='Select File',
                                       filetypes=(("text", "*.txt"), ("Any file", "*.*")))
    root.title(file1 + ' - Text Editor')
    file1 = open(file1, 'r+')
    string = file1.read()
    text.insert(1.0, string)


def save_file():
    global file1
    if file1:
        file1.write(text.get(1.0, 'end'))
        file1.close()
    else:
        file = open('untitled.txt', 'w')
        file.write(text.get(1.0, 'end'))
        file.close()


def save_as_file():
    file = filedialog.asksaveasfile(defaultextension='*.txt', mode='w', filetypes=(("text", "*.txt"), ("Any file", "*.*")),
                                    initialfile='untitled', parent=text)
    file.write(text.get(1.0, 'end'))
    file.close()


mainmenu = Menu(root)
root.config(menu=mainmenu)

menu1 = Menu(mainmenu)
mainmenu.add_cascade(label="File", menu=menu1)

menu1.add_command(label="New File", command=new_file)
menu1.add_command(label="Open Folder", command=open_folder)
menu1.add_command(label="Open File", accelerator='Ctrl+O', command=open_file)
menu1.add_separator()
menu1.add_command(label="Save", command=save_file)
menu1.add_command(label="Save as", command=save_as_file)
menu1.add_command(label="Save all")
menu1.add_separator()
menu1.add_command(label="Exit", command=exit)

menu2 = Menu(mainmenu)
mainmenu.add_cascade(label="Edit", menu=menu2)

menu2.add_command(label="Undo Move", command=undo)
menu2.add_command(label="Redo Move", command=redo)
menu2.add_separator()
menu2.add_command(label="Cut")
menu2.add_command(label="Copy")
menu2.add_command(label="Paste")
menu2.add_separator()
menu2.add_command(label="Delete", command=delete)

statusbar = Label(root, text="The text file editor which created by Guri", bg='aqua', bd=6, relief=RIDGE, anchor=N)
statusbar.pack(side=BOTTOM, fill=X)

root.mainloop()
