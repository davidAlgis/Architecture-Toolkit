import tkinter as tk

class MenuBar(tk.Frame):
    def __init__(self, parent):
        self.menuBar= tk.Menu(parent)
        self.menuFile = tk.Menu(self.menuBar, tearoff=0)
        self.initFileMenu()
        

    def initFileMenu(self):
        
        self.menuFile.add_command(label="New", command=self.newFile)
        self.menuFile.add_command(label="Save", command=self.saveFile)
        self.menuFile.add_command(label="Save As...", command=self.saveAsFile)
        self.menuFile.add_command(label="Import", command=self.importFile)
        self.menuFile.add_command(label="Export", command=self.exportFile)
        self.menuFile.add_separator()
        self.menuFile.add_command(label="Quit", command=self.quit)
        self.menuBar.add_cascade( label="File", menu=self.menuFile)


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