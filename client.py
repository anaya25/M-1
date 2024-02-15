import socket
from threading import Thread
import tkinter
from tkinter import *



PORT = 8050
IP_ADDRESS = '127.0.0.1'
SERVER = None


def musicWindow():
    #from tkinter import *
    from tkinter import ttk
    from tkinter import filedialog

    window = Tk()
    window.title('Music Window')
    window.geometry("300x300")
    window.configure(bg='LightSkyBlue')

    selectlabel = Label(window, text= "Select song", bg = 'LightSkyBlue' ,font = ("Calibri",0))
    selectlabel.place(x=2, y=1)

    listbox = Listbox(window,height = 10,width = 39,activestyle = 'dotbox', bg = 'LightSkyBlue' ,font = ("Calibri",10))
    listbox.place(x=10, y=10)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)
    
    PlayButton=Button(window,text="Play",width=10 ,bd=1, font = ("Calibri",10), bg = 'SkyBlue')
    PlayButton.place(x=30,y=200)

    Stop=Button(window,text="Stop",bd=1,width=10, font = ("Calibri",10), bg = 'SkyBlue')
    Stop.place(x=200,y=200)

    Upload=Button(window,text="Upload",bd=1,width=10, font = ("Calibri",10), bg = 'SkyBlue')
    Upload.place(x=30,y=250)

    Download=Button(window,text="Download",bd=1,width=10, font = ("Calibri",10), bg = 'SkyBlue')
    Download.place(x=200,y=250)
    
    infolabel = Label(window, text= " ", bg = 'blue' ,font = ("Calibri",0))
    infolabel.place(x=4, y=200)

    window.mainloop()


def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS,PORT))

    musicWindow()
setup()





