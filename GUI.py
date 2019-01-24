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
		self.exit_button = Button(self.master, relief = 'raised', text = 'Salir', command = lambda: exit())#self.master.quit)
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

		#print('----------------------------')
		#print(open('tmp', 'r').read())
		#print('----------------------------')

		n_songs = 0
		n_songs = 0
		if len(out) == 0:
			if 'http' not in open(self.f_name, 'r').read():
				messagebox.showerror('Error', 'Ha ocurrido un error en la ejecución \n La URL introducida no es válida')
				self.delete_file()
				os.remove('tmp')
				raise Exception('Not valid URL')
			else:  # 'youtube-dl: command not found' in line:
				messagebox.showerror('FATAL ERROR',
				                     'Youtube-dl no está instalado o en la carpeta en la que está este fichero.\nPor favor instálelo antes de continuar.')
				self.delete_file()
				os.remove('tmp')
				raise Exception('Youtube-dl not installed')
		elif len(out) == 1 and len(open(self.f_name, 'r').read()) != 0:
			# Unable to download webpage: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:661)> (caused by URLError(SSLError(1, u'[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:661)'),))
			messagebox.showerror('Error', 'Ha ocurrido un error en la ejecución \nHa habido un error con la red')
			self.delete_file()
			os.remove('tmp')
			raise Exception('URL open error')
		else:
			for line in out:
				if 'Make sure you are using the latest version; type  youtube-dl -U  to update.' in line :
					messagebox.showerror('Error', 'Ha ocurrido un error en la ejecución \n Es necesario actualizar la herramienta. \
					Pinche y dará comienzo la actualización')
					os.system('youtube-dl -U')
					#self.beep()
					messagebox.showinfo('Actualizado', 'Se ha completado la actualización. Ya continuar con la descarga')
					raise Exception ('Need to update youtube-dl')
				elif 'is not a valid URL' in line:
					messagebox.showerror('Error', 'Ha ocurrido un error en la ejecución \n La URL introducida no es válida')
					raise Exception('Not valid URL')
				elif '[ffmpeg] Destination' in line:
					n_songs += 1

		if n_songs == 1:
			str_end = str(n_songs) + ' canción'
		else:
			str_end = str(n_songs) + ' canciones'
		if n_songs > 0:
			#self.beep()
			messagebox.showinfo('Hecho', 'Se ha completado la descarga de ' + str_end)
		#(\[ffmpeg\]\sDestination\:)\s(.*)\.(.*)$
		# ERROR QUE NECESITA UPDATE: Make sure you are using the latest version; type  youtube-dl -U  to update.
		# NUMERO DE CANCIONES DESCARGADAS: Concatenacion [download] Destination: + [ffmpeg] Destination:

		self.delete_file()
		os.remove('tmp')
		### TODO: convertir py2exe --> Windows
		### TODO: Implementar multihilo
		### TODO: Implementar un sonido cuando sale una ventana

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
		if len(input_lines) == 0:
			#self.beep()
			messagebox.showerror('Error', 'No se ha insertado ninguna URL desde la que realizar la descarga')
			raise Exception('No se ha insertado ninguna URL desde la que realizar la descarga')
		self.file = open(self.f_name, 'w+')
		for l in input_lines:
			self.file.write(l+'\n')
		self.file.close()

	def delete_file(self):
		os.remove(self.f_name)

	#def beep(self):
	#	print "\a"

window = Tk()
my_gui = MusicDownloadGUI(window, 50, 100)
window.mainloop()