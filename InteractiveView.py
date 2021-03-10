import tkinter as tk
from tkinter import ttk
from Wall import *
import numpy as np
import Selectable

class InteractiveView(tk.Frame):
    currentWallEdit: Wall

    def __init__(self,parent, frame):
        self.canvas = tk.Canvas(frame)
        self.parent = parent
        self.messageString = tk.StringVar()
        self.messageInteractiveView = tk.Label(frame, textvariable = self.messageString, justify=tk.LEFT, anchor=tk.W, font =('Arial',12))
        self.messageString.set("")
        self.messageInteractiveView.grid(row = 2, column =0, sticky ="w" )

        #add scroll bar
        self.xsb = tk.Scrollbar(frame, orient="horizontal", command=self.canvas.xview)
        self.ysb = tk.Scrollbar(frame, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.ysb.set, xscrollcommand=self.xsb.set)
        self.canvas.configure(scrollregion=(0,0,1000,1000))
        self.xsb.grid(row=1, column=0, sticky="ew")
        self.ysb.grid(row=0, column=1, sticky="ns")

        self.defaultBind()
        
        self.centerX = 0
        self.centerY = 0

        self.listWall = [Selectable]
        self.currentDirectionForWall = np.array([0,1])

    

    def initCenter(self):
        self.centerX = int(self.canvas.winfo_width()/2)
        self.centerY = int(self.canvas.winfo_height()/2)

    #scroll and zoom in 
    def scroll_start(self, event):
        self.canvas.scan_mark(event.x, event.y)

    def scroll_move(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)
        self.centerX = event.x
        self.centerY = event.y

    def zoomer(self,event):
        if (event.delta > 0):
            self.canvas.scale("all", event.x, event.y, 1.1, 1.1)
        elif (event.delta < 0):
            self.canvas.scale("all", event.x, event.y, 0.9, 0.9)
        self.canvas.configure(scrollregion = self.canvas.bbox("all"))

    
    def addMessage(self,str):
        self.messageString.set(str)
        self.flashMessage()

    def flashMessage(self):
        color = ""
        if(self.messageInteractiveView.cget("fg") == self.messageInteractiveView.cget("bg")):
            color = "black"
        else:
            color = self.messageInteractiveView.cget("bg")

        self.messageInteractiveView.config(fg = color)
        self.parent.after(500, self.flashMessage)

    def bindWallOrigin(self):
        self.canvas.bind("<ButtonPress-1>", self.beginWall)

    def beginWall(self, event):
        print("enter wall origin")
        self.currentWallEdit = Wall(np.array([event.x, event.y], dtype = float))
        
        self.canvas.bind("<ButtonPress-1>", self.endWall)

    def endWall(self, event):
        print("end wall")
        end = np.array([event.x, event.y])
        length = np.linalg.norm(end - self.currentWallEdit.origin)

        vectorOriginBasis = self.currentWallEdit.origin + self.currentDirectionForWall

        if(np.linalg.norm(vectorOriginBasis) != 0):
            vectorOriginBasis/=int(np.linalg.norm(vectorOriginBasis))
        else:
            print("error divide 0")

        vectorWall = end - self.currentWallEdit.origin
        if(np.linalg.norm(vectorWall) != 0):
            vectorWall/=np.linalg.norm(vectorWall)
        else:
            print("error divide 0 1")
        
        angle = np.arccos(np.vdot(vectorOriginBasis, vectorWall))
        self.currentWallEdit.length = length
        print(self.currentWallEdit.origin, self.currentWallEdit.length)
        self.defaultBind()

        self.canvas.create_line(self.currentWallEdit.origin[0],self.currentWallEdit.origin[1], end[0], end[1])
        self.listWall.append(self.currentWallEdit)

    def defaultBind(self):
        # This is what enables scrolling with the mouse:
        self.canvas.bind("<ButtonPress-3>", self.scroll_start)
        self.canvas.bind("<B3-Motion>", self.scroll_move)
        #self.canvas.bind("<ButtonPress-2>", self.scroll_move)
        #self.canvas.bind("<B2-Motion>", self.scroll_move)
        self.canvas.bind("<MouseWheel>",self.zoomer)