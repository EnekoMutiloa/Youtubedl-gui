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
        self.label = None
        self.entrada_variable = None
        self.download_button = None
        self.top_frame = None
        self.entry_scrollbar = None
        self.button_frame = None

        f_name = 'list.txt'
        self.file = TextFile(f_name)
        self.file.create_text_file()

        self.createWidgets()


    def createWidgets(self):
        '''Metodo que crea todos los widgets necesarios para manejar la interfaz. Botones, cuadros de escritura, etc.'''
        self.top_frame = Frame(relief = 'sunken', bg = 'black')
        self.label = Label(self.master, text="Escribir a continuación las direcciones de las que se quiere descargar la música. Una línea por url (dirección de internet):").pack()#(side=LEFT)
        self.entrada_variable = Text(self.master, relief = 'sunken', insertborderwidth = '2.0').pack(fill = 'x', expand = True)
        #Entry(self.master, relief='sunken').pack()#(side=RIGHT)
        self.top_frame.pack(fill = 'x', expand = True) #fill='x' quiere decir que aprovecha el espacio horizontal disponible

        self.button_frame = Frame(relief = 'raised', bg = 'gray')
        self.download_button = Button(self.master, text="Descargar", command = lambda: self.download_from_text()).pack()
        self.button_frame.pack(fill = 'x', expand = True)

    #def download_button_action(self):
    #    download_from_text()

    def download_from_text(self):
        '''Metodo mediante el cual se realiza la descarga'''
        print(len(self.entrada_variable.get("1.0", END)))
        self.file.write_in_file(self.entrada_variable.get("1.0", END))
        res = subprocess.check_output(["youtube-dl", "--extract-audio", "--audio-format", "mp3", "-a", self.file.get_name])
        #https://www.youtube.com/watch?v=AXvr66tOERo&frags=pl%2Cwn
        self.file.close_and_delete_file()
        messagebox.showinfo("Hecho", "Se ha completado la descarga.")

window = Tk()
window.resizable(0, 0)
window.title("Descargar música")
my_gui = MusicDownloadGUI(window, 500, 500)
window.mainloop()


