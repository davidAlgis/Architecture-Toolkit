import tkinter as tk
from tkinter import ttk
from InteractiveView import *
from ToBlender import *

class ThumbBoolean(tk.Frame):
    def __init__(self, frame, interactiveView:InteractiveView):
        self.addBooleanButton = tk.Button(frame, text="Add Boolean", command=self.addBoolean)
        self.booleansListBox = tk.Listbox(frame)
        #self.addRoomButton = tk.Button(frame, text="Add Room", command=self.addRoom)
        #self.deleteWall = tk.Button(frame, text = "Delete Selection", command=self.deleteSelection)
        self.addBooleanButton.grid(row = 0, column = 0)
        self.booleansListBox.grid(row = 0, column = 2)
        #self.addRoomButton.grid(row=0, column=0)
        #self.deleteWall.grid(row=1, column=0)
        self.interactiveView = interactiveView
    
    def initBooleansListBox(self):
        print("ksdnflsnfs")

    def addBoolean(self):
        print("add boolean")
        ToBlender.testAddCube()
