from tkinter import Tk, Label, Button, Text, messagebox, Frame
import TextFile
import subprocess


class MusicDownloadGUI:
    def __init__(self, master, height, width):
        #f = TextFile()
        #f.create_text_file()

        self.master = master
        master.title("Descargar música")
        master.geometry(str(height)+"x"+str(width))
        master.resizable(0, 0)

        top_frame = Frame(master, width = width, height= height, pady=3).grid(row=0, columnspan=3)
        Label(top_frame, text='Programa para descargar musica').grid(row=0, columnspan=3)

        self.download_button = Button(master, text ="Descargar", command = lambda: self.download_from_text("a.txt")).pack()

        #T = Text(root, height=2, width=30)
        #T.pack()

        #self.label = Label(master, text="This is our first GUI!")
        #self.label.pack()

        self.close_button = Button(master, text = "Close", command = master.quit).pack()


    def download_from_text(self, text_file):

        res = subprocess.check_output(["youtube-dl", "--extract-audio", "--audio-format", "mp3", "https://www.youtube.com/watch?v=AXvr66tOERo&frags=pl%2Cwn"]) #"-a", #text_file.file])
        print("Boton pulsado. Descargando")
        #text_file.close_and_delete_file()
        messagebox.showinfo("Hecho", "Se ha completado la descarga.")
        return None


window = Tk()
my_gui = MusicDownloadGUI(window, 500, 500)
window.mainloop()