from tkinter import Tk, Label, Button, Text
import TextFile
import subprocess

class MusicDownloadGUI:
    def __init__(self, window):
        f = TextFile()
        f.create_text_file()

        self.master = window
        window.title("Descargar música")

        self.download_button = Button("Descargar", self.download)
        self.download_button.pack()

        T = Text(root, height=2, width=30)
        T.pack()

        #self.label = Label(master, text="This is our first GUI!")
        #self.label.pack()

    def download(self, text_file):
        subprocess.check_output(["youtube-dl", "--extract-audio", "--audio-format", "mp3", "-a", text_file.file])
        text_file.close_and_delete_file()


root = Tk()
my_gui = MusicDownloadGUI(root)
root.mainloop()