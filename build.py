from cx_Freeze import setup, Executable

setup(name = "Youtubedl-gui" ,
      version = "0.1" ,
      description = "" ,
executables = [Executable("GUI.py", targetName="YoutubeDLGUI.exe", base = "Win32GUI")])