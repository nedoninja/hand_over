import tkinter
from tkinter import ttk
from PIL import Image, ImageTk
from mikro import *
from display import *
from server import *
from came import *
from tkinter.messagebox import showerror
import os

class GUI:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def create_root(self):
        root = tkinter.Tk()
        root.configure(background='#30364a')
        root.geometry(f"{self.x}x{self.y}+350+150")

        # camon = Image.open("C:\\Users\\svatoslav\\Downloads\\EXEZE\GUI\\python\\img\\СAMON.png")
        # camoff = Image.open("C:\\Users\\svatoslav\\Downloads\\EXEZE\GUI\\python\\img\\CAMOFF.png")
        # dison = Image.open("C:\\Users\\svatoslav\\Downloads\\EXEZE\GUI\\python\\img\\DISON.png")
        # disoff = Image.open("C:\\Users\\svatoslav\\Downloads\\EXEZE\GUI\\python\\img\\DISOFF.png")
        # mkon = Image.open("C:\\Users\\svatoslav\\Downloads\\EXEZE\GUI\\python\\img\\MKON.png")
        # mkoff = Image.open("C:\\Users\\svatoslav\\Downloads\\EXEZE\GUI\\python\\img\\MKOFF.png")
        # ineton = Image.open("C:\\Users\\svatoslav\\Downloads\\EXEZE\GUI\\python\\img\\WION.png")
        # inetoff = Image.open("C:\\Users\\svatoslav\\Downloads\\EXEZE\GUI\\python\\img\\WIOFF.png")

        camon = Image.open("img\\СAMON.png")
        camoff = Image.open("img\\CAMOFF.png")
        dison = Image.open("img\\DISON.png")
        disoff = Image.open("img\\DISOFF.png")
        mkon = Image.open("img\\MKON.png")
        mkoff = Image.open("img\\MKOFF.png")
        ineton = Image.open("img\\WION.png")
        inetoff = Image.open("img\\WIOFF.png")

        sx = 400 
        sy = 200

        camonr = camon.resize((sx, sy))
        camoffr = camoff.resize((sx, sy))
        disonr = dison.resize((sx, sy))
        disoffr = disoff.resize((sx, sy))
        mkonr = mkon.resize((sx, sy))
        mkoffr = mkoff.resize((sx, sy))
        inetonr = ineton.resize((sx, sy))
        inetoffr = inetoff.resize((sx, sy))

        camoni = ImageTk.PhotoImage(camonr)
        camoffi = ImageTk.PhotoImage(camoffr)
        disoni = ImageTk.PhotoImage(disonr)
        disoffi = ImageTk.PhotoImage(disoffr)
        mkoni = ImageTk.PhotoImage(mkonr)
        mkoffi = ImageTk.PhotoImage(mkoffr)
        inetoni = ImageTk.PhotoImage(inetonr)
        inetoffi = ImageTk.PhotoImage(inetoffr)

        mk = mikro()
        cm = came()
        dsp = display()
        iner = server()

        is_prod = True

        if mk.proverka_mk() == True:
            mkonl = tkinter.Label(image=mkoni, highlightthickness="0", borderwidth="0", background="#30364a")
            mkonl.pack(anchor="nw", padx=20, pady=30)
        else:
            mkoffl = tkinter.Label(image=mkoffi, highlightthickness="0", borderwidth="0", background="#30364a")
            mkoffl.pack(anchor="nw", padx=20, pady=30)
            is_prod = False
            showerror(message="подключите микрофон к компьютеру")
            root.destroy()
            # os.system("C:\\Users\\svatoslav\\Downloads\\EXEZE\\GUI\\c#\\App\\main\\bin\Debug\\main.exe")
            #os.system("main.exe")

        if cm.proverka_cm() == True:
            cmonl = tkinter.Label(image=camoni, highlightthickness="0", borderwidth="0", background="#30364a")
            cmonl.pack(anchor="w", padx=20)
        else:
            cmonl = tkinter.Label(image=camoffi, highlightthickness="0", borderwidth="0", background="#30364a")
            cmonl.pack(anchor="w", padx=20)
            is_prod = False
            showerror(message="подключите веб-камеру к компьютеру")
            root.destroy()
            # os.system("C:\\Users\\svatoslav\\Downloads\\EXEZE\\GUI\\c#\\App\\main\\bin\Debug\\main.exe")
            # os.system("main.exe")

        if dsp.proverka_dsp() == True:
            dvil = tkinter.Label(image=disoni, highlightthickness="0", borderwidth="0", background="#30364a")
            dvil.pack(anchor="w", padx=20)
        else:
            cmonl = tkinter.Label(image=disoffi, highlightthickness="0", borderwidth="0", background="#30364a")
            cmonl.pack(anchor="w", padx=20)
            is_prod = False
            showerror(message="у вас подлюченно 2 или более дисплеев, оставте только один")
            root.destroy()
            # os.system("C:\\Users\\svatoslav\\Downloads\\EXEZE\\GUI\\c#\\App\\main\\bin\Debug\\main.exe")
            # os.system("main.exe")

        if iner.proverka_inet() == True:
            inetil = tkinter.Label(image=inetoni, highlightthickness="0", borderwidth="0", background="#30364a")
            inetil.pack(anchor="w", padx=20)
        else:
            inetil = tkinter.Label(image=inetoffi, highlightthickness="0", borderwidth="0", background="#30364a")
            inetil.pack(anchor="w", padx=20)
            is_prod = False
            showerror(message="нет подключения к интернету")
            root.destroy()
            # os.system("C:\\Users\\svatoslav\\Downloads\\EXEZE\\GUI\\c#\\App\\main\\bin\Debug\\main.exe")
            # os.system("main.exe")

        if is_prod:
            # os.system("C:\\Users\\svatoslav\\Downloads\\EXEZE\\GUI\\c#\\Base\\bin\\Debug\\Base.exe")
            os.system("Base.exe")
            root.destroy()

        root.mainloop()