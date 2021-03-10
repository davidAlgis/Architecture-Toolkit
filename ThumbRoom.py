import tkinter as tk
from tkinter import ttk
from InteractiveView import *

class ThumbRoom(tk.Frame):
    def __init__(self, frame, interactiveView:InteractiveView):
        self.addRoomButton = tk.Button(frame, text="Add Room", command=self.addRoom)
        self.addRoomButton.grid(row=0, column=0)

        self.interactiveView = interactiveView
    
    def addRoom(self):
        self.interactiveView.bindWallOrigin()#.canvas.bind("<ButtonPress-1>", ))
        self.interactiveView.addMessage("Add the origin of the wall by clicking on the view above")