import tkinter as tk
from tkinter import ttk
from ThumbRoom import *
from ThumbBoolean import *

class Thumb(tk.Frame):
    def __init__(self, frame, interactiveView:InteractiveView):
        self.thumb = ttk.Notebook(frame)
        

        self.thumbRoom = ttk.Frame(self.thumb)
        self.thumbRoom.pack()
        self.thumb.add(self.thumbRoom, text='Room')  
        ThumbRoom(self.thumbRoom, interactiveView)


        self.thumbBoolean = ttk.Frame(self.thumb)
        self.thumbBoolean.pack()
        self.thumb.add(self.thumbBoolean, text='Boolean')  
        ThumbBoolean(self.thumbBoolean, interactiveView)

        self.thumbStairs = ttk.Frame(self.thumb)
        self.thumbStairs.pack()
        self.thumb.add(self.thumbStairs, text='Stairs')  

        self.thumbMat = ttk.Frame(self.thumb)
        self.thumbMat.pack()
        self.thumb.add(self.thumbMat, text='Materials')  

        