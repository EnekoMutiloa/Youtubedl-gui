from tkinter import *
from tkinter import messagebox
from TextFile import TextFile
import subprocess


class MusicDownloadGUI:
    def __init__(self, master, height, width):
        f = TextFile()
        f_name = 'list.txt'
        f.create_text_file(f_name)

        self.master = master
        master.title("Descargar música")
        master.geometry(str(height)+"x"+str(width))
        master.resizable(0, 0)

        #Label(master, text="Programa para decsargar musica").grid(row=0)
        #e1 = Entry(master)
        #e1.grid(row=0, column=1)

        self.download_button = Button(master, text ="Descargar", command = lambda: self.download_from_text(f)).pack()

        #T = Text(root, height=2, width=30)
        #T.pack()

        #self.label = Label(master, text="This is our first GUI!")
        #self.label.pack()

        self.close_button = Button(master, text = "Close", command = self.exit_button(f)).pack()


    def download_from_text(self, text_file):

        print("Boton pulsado. Descargando")
        res = subprocess.check_output(["youtube-dl", "--extract-audio", "--audio-format", "mp3", "-a", text_file.get_name])
        text_file.close_and_delete_file()
        messagebox.showinfo("Hecho", "Se ha completado la descarga.")
        return None

    def exit_button(self, text_file):
        text_file.close_and_delete_file()
        self.master.quit
        return None


window = Tk()
my_gui = MusicDownloadGUI(window, 500, 500)
window.mainloop()