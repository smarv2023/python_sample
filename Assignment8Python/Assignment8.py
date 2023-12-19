import os.path
from tkinter import *
from tkinter import filedialog, Tk, messagebox
from tkinter.messagebox import showinfo

# Global variable to see if file name is active useful for save function to overwrite old file
global active_file_Name
active_file_Name = False


# New File will also ask if you want to save your file before clearing the pad (messagebox.askyesno)
# If the user click new file on empty pad nothing will happen because of If textfile > 1:
# If the user click SAVE on empty pad Save_as() function will pop up, because the boolean active_file_Name = False
def new_file():
    global active_file_Name
    textfile = len(textBox.get('1.0', END))
    if textfile > 1:
        if messagebox.askyesno('Basic Notepad', 'Do you want to save changes?'):
            save_file()
            active_file_Name = False
            window.title("Untitled")
            textBox.delete(1.0, END)
            active_file_Name = False
        else:
            textBox.delete(1.0, END)
        window.title("Untitled")


# This open file will also give value to (**active_file_Name = text_open**) for the location of file
# If there is a file existing in location or directory (Save function) is functional
# Filedialog will appear if you click open
def open_file():
    text_open = filedialog.askopenfilename(title='Open File', defaultextension=".txt",
                                           filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')])

    if text_open:
        global active_file_Name
        active_file_Name = text_open
        textBox.delete('1.0', END)
        window.title(os.path.basename(text_open))
        text_open = open(text_open, 'r')
        file = text_open.read()
        textBox.insert(END, file)


# This is save file function it will overwrite the old file if it is existing
# if global variable (**active_file_Name is False**) and you click save it will trigger the (Save As Function)
def save_file():
    global active_file_Name
    if active_file_Name:
        text_file = open(active_file_Name, 'w')
        text_file.write(textBox.get(1.0, END))
        text_file.close()
    else:
        save_as_file()


# A filedialog that will ask where to save the user's file
# This will always pop up everytime the user click save if the file does not exit.
def save_as_file():
    text_save_as = filedialog.asksaveasfilename(title="Save As File", defaultextension='.txt',
                                                filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')])
    if text_save_as:
        global active_file_Name
        active_file_Name = text_save_as
        window.title(os.path.basename(text_save_as))
        text_save_as = open(text_save_as, 'w')
        text_save_as.write(textBox.get('1.0', END))
        text_save_as.close()


# function for CUT,COPY, PASTE, ABOUT and QUIT
def cut_text():
    textBox.event_generate('<<Cut>>')


def copy_text():
    textBox.event_generate('<<Copy>>')


def paste_text():
    textBox.event_generate('<<Paste>>')


def about():
    showinfo('About this basic Notepad', 'Created by: Marvin Soro')


def quit():
    window.destroy()


# Window
window = Tk()
window.geometry('800x600')
window.title('Basic Notepad')
window.config()

# Menu holder
menu_base = Menu(window)
window.config(menu=menu_base)

# File menu
file_menu = Menu(menu_base, tearoff=0)
menu_base.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New File", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save as", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

# Edit menu
edit_menu = Menu(menu_base, tearoff=0)
menu_base.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)

# About
about_menu = Menu(menu_base, tearoff=0)
menu_base.add_cascade(label="About", menu=about_menu)
about_menu.add_command(label="About", command=about)

# Text area
textBox = Text(undo=True)
textBox.pack(expand=True, fill=BOTH)

# Code for the right-side scroll bar
scroll_bar = Scrollbar(textBox)
scroll_bar.pack(side=RIGHT, fill=Y)
textBox.config(yscrollcommand=scroll_bar.set)

window.mainloop()
