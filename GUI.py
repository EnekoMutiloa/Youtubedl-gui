#-*- coding: utf-8 -*-

try: # para ejecutar en python3.X
	from tkinter import *
	from tkinter import filedialog
	from tkinter import messagebox
	import tkinter.font as tkFont
	import tkinter.ttk as ttk
	import os

except ImportError:  # para jecutar en python 2.7
	from Tkinter import *
	import tkFileDialog as filedialog
	import tkMessageBox as messagebox
	import tkFont
	import ttk
	import os


class MusicDownloadGUI:
	def __init__(self, master, height, width):
		'''
		Constructor method of the MusicDownloadGUI class
		'''
		self.master = master
		self.master.resizable(0, 0)
		self.master.title('Descargar música')
		self.label = None
		self.text_area = None
		self.download_button = None
		self.text_frame = None
		self.entry_scrollbar = None
		self.button_frame = None
		self.text_scrollbar = None
		self.exit_button = None

		self.f_name = 'list.txt'
		self.file = None

		self.initGui(height, width)

	def initGui(self, width, height):
		'''
		Method that initializes all the necessary widgets for the gui. Buttons, text areas, scrollbars etc.
		:param width: width of the window
		:param height: height of the window
		'''

		self.label = Label(self.master, text='Escribir a continuación las direcciones de las que se quiere descargar la música. Una línea por url (dirección de internet):')
		self.label.pack()

		'''Create a Frame for the Text and Scrollbar'''
		self.text_frame = Frame(relief = 'sunken', width = width, height = height)
		self.text_frame.pack(fill = 'both', expand = True)  # fill = 'x' quiere decir que aprovecha el espacio horizontal disponible

		'''create a Scrollbar and associate it with txt'''
		self.text_scrollbar = Scrollbar(self.text_frame, orient = 'vertical')
		self.text_scrollbar.pack(side = 'right', fill = 'y')

		'''create a Text widget'''
		self.text_area = Text(self.text_frame, relief = 'sunken', borderwidth = 2, yscrollcommand = self.text_scrollbar.set)
		# self.text_area = Text(self.master, relief = 'sunken', insertborderwidth = '2.0', yscrollcommand = self.text_scrollbar.set)
		self.text_area.pack(fill = 'x', expand = True)
		self.text_scrollbar.config(command = self.text_area.yview)

		'''Create a Frame for the buttons'''
		self.button_frame = Frame(relief = 'raised', bg = 'gray')
		self.button_frame.pack(fill = 'x', expand = True)
		self.download_button = Button(self.master, relief = 'raised', text = 'Descargar', command = lambda: self.download_from_text())
		self.download_button.pack(fill = 'x', expand = True)
		self.exit_button = Button(self.master, relief = 'raised', text = 'Salir', command = self.master.quit)
		self.exit_button.pack(fill = 'x', expand = True)

	def download_from_text(self):
		'''
				Method that downloads everything in the text file. It shows a message when the process finishes.
				This method deletes the text file also.
				'''
		self.write_in_text()
		#https://www.youtube.com/watch?v=AXvr66tOERo&frags=pl%2Cwn
		#https://www.youtube.com/watch?v=DMkDwIM3piA&list=PL0_Zm4Wcsi0K_KT9jkrwPYhCr-oK1vU-r

		## Esta manera de ejecutar el comando sirve para capturar la salida pero no los errores
		os.system('youtube-dl --extract-audio --audio-format mp3 -a ' + self.f_name + ' > tmp')
		out = open('tmp', 'r').readlines()

		n_songs = 0
		for line in out:
			if '[ffmpeg] Destination' in line:
				n_songs += 1
		#(\[ffmpeg\]\sDestination\:)\s(.*)\.(.*)$
		# ERROR QUE NECESITA UPDATE: Make sure you are using the latest version; type  youtube-dl -U  to update.
		# NUMERO DE CANCIONES DESCARGADAS: Concatenacion [download] Destination: + [ffmpeg] Destination:

		messagebox.showinfo('Hecho', 'Se ha completado la descarga de ' + str(n_songs) + ' canciones')
		#try:
		#	subprocess.call(['youtube-dl --extract-audio --audio-format mp3 -a', self.f_name])
		#	messagebox.showinfo('Hecho', 'Se ha completado la descarga de ' + str(n_songs) + ' canciones')
		#self.delete_file()
		#except NameError as err: #NameError as err or
		#	messagebox.showerror('Error', 'La dirección ' +' no es válida.' + str(err))
		#	self.delete_file()
		#except OSError as err:
		#	messagebox.showerror('Error', 'Ha ocurrido un error en la ejecución \n OS error:'+ str(err) + '.')
		#	self.delete_file()

		self.delete_file()
		os.remove('tmp')
		### TODO: convertir py2exe --> Windows
		### TODO: Hay que conseguir capturar el output de la consola para ver que pone y sacar un mensaje de error.

	def write_in_text(self):
		'''
		Method that reads the lines in the text area and writes them in the file that is going to be used in the bash process
		'''

		input_lines = self.text_area.get('1.0', END).splitlines()
		try:  # Python 2.x
			input_lines = [u.encode('utf-8') for u in input_lines]
			input_lines = list(filter(str.strip, input_lines))
		except TypeError: # Python 3.x
			input_lines = [b.decode('utf-8') for b in input_lines]
			input_lines = list(filter(str.strip, input_lines))
		self.file = open(self.f_name, 'w+')
		for l in input_lines:
			#print('------------------')
			#print(l)
			#print('------------------')
			self.file.write(l+'\n')
		self.file.close()

	def delete_file(self):
		os.remove(self.f_name)

window = Tk()
my_gui = MusicDownloadGUI(window, 50, 100)
window.mainloop()