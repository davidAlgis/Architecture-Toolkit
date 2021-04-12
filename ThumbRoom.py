import tkinter as tk
from tkinter import ttk
from InteractiveView import *

class ThumbRoom(tk.Frame):
    def __init__(self, frame, interactiveView:InteractiveView):
        self.addRoomButton = tk.Button(frame, text="Add Room", command=self.addRoom)
        self.deleteWall = tk.Button(frame, text = "Delete Selection", command=self.deleteSelection)
        self.addRoomButton.grid(row=0, column=0)
        self.deleteWall.grid(row=1, column=0)
        self.interactiveView = interactiveView
    
    def addRoom(self):
        self.interactiveView.bindWallOrigin()
        self.interactiveView.addMessage("Add the origin of the wall by left clicking on the view below, middle click to cancel. ", True)

    def deleteSelection(self):
        listCurrentSelection = self.interactiveView.listCurrentSelection
        listContourSelection = self.interactiveView.listContourSelectionID
        listSelectable = self.interactiveView.listSelectable

        canvas = self.interactiveView.canvas
        for currentSelection in listCurrentSelection:
            canvas.delete(currentSelection.canvasID)
            listSelectable.remove(currentSelection)

        for currentContour in listContourSelection:
            canvas.delete(currentContour)