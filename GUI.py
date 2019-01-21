try: # para ejecutar en python3.X
	from tkinter import *
	from tkinter import filedialog
	from tkinter import messagebox
	import tkinter.font as tkFont
	import tkinter.ttk as ttk
	import subprocess
	import os

except ImportError:  # para jecutar en python 2.7
	from Tkinter import *
	import tkFileDialog as filedialog
	import tkMessageBox as messagebox
	import tkFont
	import ttk
	import subprocess
	import os


class MusicDownloadGUI:
	def __init__(self, master, height, width):
		'''Metodo constructor de la clase que genera la interfaz'''
		self.master = master
		self.label = None
		self.text_area = None
		self.download_button = None
		self.text_frame = None
		self.entry_scrollbar = None
		self.button_frame = None
		self.text_scrollbar = None
		self.exit_button = None

		self.f_name = 'list.txt'
		self.file = open(self.f_name, "w+")

		self.initGui(height, width)


	def initGui(self, width, height):
		'''Metodo que crea todos los widgets necesarios para manejar la interfaz. Botones, cuadros de escritura, scrollbars, etc.'''

		self.label = Label(self.master, text="Escribir a continuacion las direcciones de las que se quiere descargar la musica. Una linea por url (direccion de internet):")
		self.label.pack()
		'''Create a Frame for the Text and Scrollbar'''
		self.text_frame = Frame(relief ='sunken', width = width, height = height)
		self.text_frame.pack(fill ='both', expand = True) #fill='x' quiere decir que aprovecha el espacio horizontal disponible

		'''create a Text widget'''
		self.text_area = Text(self.text_frame, relief='sunken', borderwidth=3)
		#self.text_area = Text(self.master, relief = 'sunken', insertborderwidth = '2.0', yscrollcommand = self.text_scrollbar.set)
		self.text_area.pack(fill = 'x', expand = True)

		'''create a Scrollbar and associate it with txt'''
		self.text_scrollbar = Scrollbar(self.text_frame, command = self.text_area.yview, orient='vertical', relief='raised')
		self.text_scrollbar.pack(side = 'right', fill = 'y', ipady = 0)  # cambiando ipady cambia la 'altura' del cuadro donde se escriben las tablas que contienen cierta variable
		#self.text_area['yscrollcommand'] = self.text_scrollbar.set()

		'''Create a Frame for the buttons'''
		self.button_frame = Frame(relief = 'raised', bg = 'gray')
		self.button_frame.pack(fill = 'x', expand = True)
		self.download_button = Button(self.master, relief = "raised", text="Descargar", command = lambda: self.download_from_text())
		self.download_button.pack(fill = 'x', expand = True)
		self.exit_button = Button(self.master, relief = "raised", text = "Salir", command = self.master.quit)
		self.exit_button.pack(fill = 'x', expand = True)


	def download_from_text(self):
		'''Metodo mediante el cual se realiza la descarga'''
		self.write_in_text()
		os.system("youtube-dl --extract-audio --audio-format mp3 -a " + self.f_name)
		#subprocess.run(["youtube-dl --extract-audio --audio-format mp3 -a", self.f_name])
		#https://www.youtube.com/watch?v=AXvr66tOERo&frags=pl%2Cwn
		#https://www.youtube.com/watch?v=8t4O5RnLSKI&frags=pl%2Cwn
		self.delete_file()
		messagebox.showinfo("Hecho", "Se ha completado la descarga.")

	def write_in_text(self):
		input_lines = self.text_area.get("1.0", END).splitlines()
		try:
			input_lines = [u.encode("utf-8") for u in input_lines]
			input_lines = list(filter(str.strip, input_lines))
		except TypeError:
			input_lines = [b.decode("utf-8") for b in input_lines]
			input_lines = list(filter(str.strip, input_lines))
		for l in input_lines:
			self.file.write(l+'\n')
		self.file.close()

	def delete_file(self):
		os.remove(self.f_name)

window = Tk()
window.resizable(0, 0)
window.title("Descargar musica")
my_gui = MusicDownloadGUI(window, 50, 100)
window.mainloop()