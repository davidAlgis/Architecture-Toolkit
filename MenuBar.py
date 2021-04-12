import tkinter as tk
from tkinter import ttk
import subprocess

class MenuBar(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        
        self.menuBar= tk.Menu(parent)
        self.menuFile = tk.Menu(self.menuBar, tearoff=0)
        self.initFileMenu()
        self.menuEdit = tk.Menu(self.menuBar, tearoff = 0)
        self.initEditMenu()
        
        self.defaultPathBlender = """C://Program Files//Blender Foundation//Blender 2.92//blender.exe"""

    def initFileMenu(self):
        
        self.menuFile.add_command(label="New", command=self.newFile)
        self.menuFile.add_command(label="Save", command=self.saveFile)
        self.menuFile.add_command(label="Save As...", command=self.saveAsFile)
        self.menuFile.add_command(label="Import", command=self.importFile)
        self.menuFile.add_command(label="Export", command=self.exportFile)
        self.menuFile.add_separator()
        self.menuFile.add_command(label="Quit", command=self.quit)
        self.menuBar.add_cascade( label="File", menu=self.menuFile)

    def initEditMenu(self):
        
        self.menuEdit.add_command(label="Settings", command=self.openSettings)
        self.menuBar.add_cascade( label="Edit", menu=self.menuEdit)
    
    def newFile(self):
        print("newFile")
        
    def saveFile(self):
        print("Menu save")

    def saveAsFile(self):
        print("Menu save as")

    def importFile(self):
        print("Menu import")

    def exportFile(self):
        print("Menu export")

    def openSettings(self):
        settingsPopup = tk.Toplevel()
        settingsPopup.title('Settings')
        defaultPathString = tk.StringVar(settingsPopup, value=self.defaultPathBlender)
        tk.Label(settingsPopup, text="Path Blender :").grid(row = 0, column =0, sticky ="w" )
        entry = tk.Entry(settingsPopup, textvariable = defaultPathString, width = 100)
        entry.grid(row = 1, column = 0)

        settingsPopup.transient(self.parent) 	  
        settingsPopup.grab_set()		  
        self.parent.wait_window(settingsPopup)  
        self.defaultPathBlender = entry.get()