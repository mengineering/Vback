#!/usr/bin/python3

import subprocess
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import os


#Inizio script gui
## DA MODIFICARE

# Cerco il la directory dove si trova Backup_dev.sh

def find_files(filename, search_path):
   result = []

   for (root, dirs, files) in os.walk(search_path):
      if filename in files:
         result.append(os.path.join(root))
   return result

install_location = "%s" % "','".join(find_files("gui.py", "."))

os.chdir(install_location)

#Bottone di avvio del processo di backup
## DA MODIFICARE - NUOVO BOTTONE

def backup_launch():
   INIT_WRK_DIRECTORY = os.getcwd()
   with open('./destinations.txt', 'r') as f:
    destination = f.readline().strip()
   elenco = os.path.join(INIT_WRK_DIRECTORY, 'source_folders.txt') 
   os.chdir(destination)
   with open('log.txt', 'w') as f:
      pass
   with open('Errors_log.txt', 'w') as f:
      pass
   with open(elenco, 'r') as f:
      for line in f:
        fld_one = line.strip()
        os.system(f'cp -r -v {fld_one} {destination} 2>> Errors_log.txt >> log.txt')

## OLD - AVVIO SHELL SCRIPT
#def avvia_backup():
#   print(subprocess.check_call("./Backup_dev.sh", shell=True))

def appendi_percorso():
   os.chdir(install_location)
   with open("./source_folders.txt", "a") as f:
    f.write("%s\n" % entry.get())
    f.close

def configurazione():
   os.chdir(install_location)
   with open("./destinations.txt", "w") as f:
    f.write("%s\n" % dest_entry.get())
    f.close

#finestra di avvio
#window = tk.Tk()
#window.geometry("600x300")
#window.resizable(False,False)

#window.after(3000,lambda:window.destroy())


#creo una finestra
window = tk.Tk()
window.geometry("350x300")
window.title("Vback")
window.resizable(False,False)
#window.configure(background="white")

start_img = ImageTk.PhotoImage(Image.open("securebackup.png"))
Img_labl=ttk.Label(window, image=start_img)
Img_labl.pack(side="top", pady=10)

#creo notebook dentro la finestra
nb = ttk.Notebook(window)
nb.pack(expand=True)
frame1 = ttk.Frame(nb, width=600, height=280) #main frame
frame2 = ttk.Frame(nb, width=600, height=280) #impostazioni
frame1.pack(fill="both", expand=True)
frame2.pack(fill="both", expand=True)

nb.add(frame1, text="Home")
nb.add(frame2, text="Settings")

#pagina settings
destination_lb=ttk.Label(frame1, text="New folder path:")
destination_lb.pack(side="top")

entry = ttk.Entry(frame1)
entry.pack(side="top")

#Bottone di avvio del processo di backup
avviabkc_button = ttk.Button(frame1 ,text="Start backup", command = backup_launch)
avviabkc_button.pack(side="right", anchor="se")
    
#bottone che appende il percorso in source_folders
appendi_button = ttk.Button(frame1, text="Add folder to backup", command=appendi_percorso)
appendi_button.pack(side="right", anchor="se")

destination_lb=ttk.Label(frame2, text="Destination folder path:")
destination_lb.pack(side="top")

dest_entry=ttk.Entry(frame2)
dest_entry.pack(side="top")

#Bottone di avvio del processo di backup
settings_button = ttk.Button(frame2 ,text="Change destination", command = configurazione)
settings_button.pack(side="right", anchor="se")

if __name__ == "__main__":
    window.mainloop()
