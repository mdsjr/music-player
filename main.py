from tkinter import *   # Import tkinter library
from tkinter import ttk
from ttkthemes import ThemedTk

class Player:
    def __init__(self):

        self.window = ThemedTk(theme="equilux")  # Create a window
        self.window.title("Music Player")
        self.window.resizable(0,0)
        self.window.geometry("300x400+800+300")
        self.window.config(bg="#444444")

        self.img_add = PhotoImage(file="assets/add.png")
        self.img_remove = PhotoImage(file="assets/remove.png")
        self.img_play = PhotoImage(file="assets/play.png")
        self.img_pause = PhotoImage(file="assets/pause.png")
        self.img_previus = PhotoImage(file="assets/previus.png")
        self.img_next = PhotoImage(file="assets/next.png")


        self.list = Listbox(self.window, bg="#555555", height=13)
        self.list.pack(fill=X, padx=10, pady=10)

        self.frame = ttk.Frame(self.window)
        self.frame.pack(pady=10)

        self.remove = ttk.Button(self.frame, image=self.img_remove)
        self.remove.grid(row=0, column=0, padx=10)

        self.add = ttk.Button(self.frame, image=self.img_add)
        self.add.grid(row=0, column=1, padx=10)

        self.frame2 = ttk.Frame(self.window )
        self.frame2.pack(pady=10)

        self.previus = ttk.Button(self.frame2, image=self.img_previus)
        self.previus.grid(row=0, column=0)

        self.play = ttk.Button(self.frame2, image=self.img_play)
        self.play.grid(row=0, column=1)

        self.previus = ttk.Button(self.frame2, image=self.img_next)
        self.previus.grid(row=0, column=3)

        self.volume = ttk.Scale(self.window)
        self.volume.pack(fill=X, padx=10, pady=5)








        self.window.mainloop()


Player()  # Create an object of the Player class