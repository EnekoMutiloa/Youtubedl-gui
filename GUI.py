from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter.font as tkFont
import tkinter.ttk as ttk
import subprocess


import os


class TextFile:

    def __init__(self, name = 'list.txt'):
        self.file = None
        self.name = name

    def create_text_file(self):
        self.file = open(self.name, 'w')

    def close_and_delete_file(self):
        self.file.close()
        os.remove(self.name)

    def write_in_file(self, url):
        self.file.write(url)

    def get_name(self):
        return self.name

class MusicDownloadGUI:
    def __init__(self, master, height, width):
        '''Metodo constructor de la clase que genera la interfaz'''
        self.master = master
        #master.geometry(str(height)+"x"+str(width))
        self.label = None
        self.entry = None
        self.download_button = None
        self.topFrame = None
        self.entryScrollbar = None
        self.buttonFrame = None

        f_name = 'list.txt'
        f = TextFile(f_name)
        f.create_text_file()

        self.createWidgets(f)
        #T = Text(root, height=2, width=30)
        #T.pack()

        #self.label = Label(master, text="This is our first GUI!")
        #self.label.pack()


    def createWidgets(self, f):
        '''Metodo que crea todos los widgets necesarios para manejar la interfaz. Botones, cuadros de escritura, etc.'''
        self.topFrame = Frame(relief='raised', bg='gray')
        self.label = Label(self.master, text="Direcciones:").pack()#(side=LEFT)
        self.entry = Entry(self.master, relief='sunken').pack()#(side=RIGHT)
        self.entryScrollbar = Scrollbar(self.entry, orient='vertical', relief='raised')
        self.topFrame.pack(fill='x', expand=True) #fill='x' quiere decir que aprovecha el espacio horizontal disponible

        self.buttonFrame = Frame(relief='raised', bg='black')
        self.download_button = Button(self.master, text="Descargar", command = self.download_from_text(f)).pack()
        self.buttonFrame.pack(fill='x', expand=True)

    def download_from_text(self, text_file):
        '''Metodo mediante el cual se realiza la descarga'''
        print(self.entry.get())

        res = subprocess.check_output(["youtube-dl", "--extract-audio", "--audio-format", "mp3", "-a", text_file.get_name])
        text_file.close_and_delete_file()
        messagebox.showinfo("Hecho", "Se ha completado la descarga.")
        return None

window = Tk()
window.resizable(0, 0)
window.title("Descargar música")
my_gui = MusicDownloadGUI(window, 500, 500)
window.mainloop()


