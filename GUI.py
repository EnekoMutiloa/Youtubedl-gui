#try: # para ejecutar en python3.X
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter.font as tkFont
import tkinter.ttk as ttk
import subprocess
from TextFile import TextFile

#except ImportError:  # para jecutar en python 2.7
#	from Tkinter import *
#	import tkFileDialog as filedialog
#	import tkMessageBox as messagebox
#	import tkFont
#	import ttk
#	import os
#    import subprocess


class MusicDownloadGUI:
    def __init__(self, master, height, width):

        self.master = master
        self.topFrame = Frame(relief='raised', bg='gray')
        master.title("Descargar música")
        master.geometry(str(height)+"x"+str(width))
        master.resizable(0, 0)
        self.label = None
        self.entry = None
        self.download_button = None
        self.createWidgets()

        f_name = 'list.txt'
        f = TextFile(f_name)
        f.create_text_file()

        #T = Text(root, height=2, width=30)
        #T.pack()

        #self.label = Label(master, text="This is our first GUI!")
        #self.label.pack()

    def createWidgets(self):
        self.topFrame = Frame(relief='raised', bg='gray')
        self.label = Label(self.master, text="Direcciones:").pack(side=LEFT)
        self.entry = Entry(self.master, relief='sunken').pack(side=RIGHT)
        self.entryScrollbar = Scrollbar(self.entry, orient='vertical', relief='raised')
        self.topFrame.pack(fill='x')
        self.download_button = Button(self.master, text="Descargar", command=lambda: self.download_from_text(f)).pack()

    def get_value(self):
        return self.entry.get

    def download_from_text(self, text_file):

        res = subprocess.check_output(["youtube-dl", "--extract-audio", "--audio-format", "mp3", "-a", text_file.get_name])
        text_file.close_and_delete_file()
        messagebox.showinfo("Hecho", "Se ha completado la descarga.")
        return None

window = Tk()
my_gui = MusicDownloadGUI(window, 500, 500)
window.mainloop()