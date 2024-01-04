# Vback

**FIRST USAGE NOTES**
open terminal in download folder and run:
chmod +x Backup_dev.sh

**ATTENTION**
It works only with folders without any spaces in its name. Rename the folder without spaces.

**LINUX NOTES**
*tested on Ubuntu 23.10*
There is an error due to PIL that is under resolution.
A simple workaround is opening the gui.py file and comment the following lines

#start_img = ImageTk.PhotoImage(Image.open("securebackup.png"))
#Img_labl=ttk.Label(window, image=start_img)
#Img_labl.pack(side="top", pady=10)
