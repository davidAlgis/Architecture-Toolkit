import tkinter as tk
from tkinter import ttk
from Wall import *
from Utils import * 
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
        self.sizeCanvas = 50000
        self.canvas.configure(scrollregion=(-self.sizeCanvas,-self.sizeCanvas,self.sizeCanvas,self.sizeCanvas))
        self.xsb.grid(row=1, column=0, sticky="ew")
        self.ysb.grid(row=0, column=1, sticky="ns")
        self.offsetXPrev = 0
        self.offsetYPrev = 0
        self.offsetXNew = 0
        self.offsetYNew = 0
        self.originMovesX = 0
        self.originMovesY = 0

        self.initGrid()
        self.defaultBind()

        self.listSelectable = [Selectable]
        self.currentDirectionForWall = np.array([0,1])
        

    #------Scroll and zoom part-----#
    def scroll_start(self, event):
        self.canvas.scan_mark(event.x, event.y)
        self.originMovesX = event.x 
        self.originMovesY = event.y 


    def scroll_move(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)
        self.offsetXNew = self.offsetXPrev + (self.originMovesX - event.x)
        self.offsetYNew = self.offsetYPrev + (self.originMovesY - event.y)


    def scroll_end(self, event):
        self.offsetXPrev = self.offsetXNew
        self.offsetYPrev = self.offsetYNew


    def zoomer(self,event):
        if (event.delta > 0):
            self.canvas.scale("all", event.x, event.y, 1.1, 1.1)
        elif (event.delta < 0):
            self.canvas.scale("all", event.x, event.y, 0.9, 0.9)
        self.canvas.configure(scrollregion = self.canvas.bbox("all"))

    #------Message part-----#
    def addMessage(self,str, flash:bool = False):
        self.messageString.set(str)
        if(flash):
            self.flashMessage()

    def flashMessage(self):
        color = ""
        if(self.messageInteractiveView.cget("fg") == self.messageInteractiveView.cget("bg")):
            color = "black"
        else:
            color = self.messageInteractiveView.cget("bg")

        self.messageInteractiveView.config(fg = color)
        self.parent.after(500, self.flashMessage)

    #------Grid part-----#
    def initGrid(self):
        sizeGrid = 100 #1 meters
        nbrOfLine = int(2*self.sizeCanvas/sizeGrid)
        for i in range(nbrOfLine):
            y = -self.sizeCanvas + i*sizeGrid
            self.canvas.create_line(-self.sizeCanvas,y,self.sizeCanvas,y, fill="#ff0000", dash=(5,))
        for j in range(nbrOfLine):
            x = -self.sizeCanvas + j*sizeGrid
            self.canvas.create_line(x,-self.sizeCanvas,x,self.sizeCanvas, fill="#ff0000", dash=(5,))

    def test(self):
        print("i")
    #------Wall part-----#
    def bindWallOrigin(self):
        self.canvas.bind("<ButtonPress-1>", self.beginWall)
        self.canvas.bind("<ButtonPress-2>", self.stopAddWall)
        self.canvas.unbind("<B1-Motion>")

    def beginWall(self, event):
        point = np.array([event.x + self.offsetXNew, event.y+ self.offsetYNew])
        point = self.magnet(point)
        self.magnetToAnotherWall = False
        self.beginWallAddPoint(point)

    def beginWallAddPoint(self, point):
        self.currentWallEdit = Wall(point)
        self.bindWallMoveEnd()

    def bindWallMoveEnd(self):
        self.canvas.bind("<Motion>", self.moveBeginWall)
        self.canvas.bind("<ButtonPress-1>", self.endWall)

    def magnet(self, point, end=False):
        for selectable in self.listSelectable:
            if(type(selectable) == Wall):
                selectable.__class__ = Wall
                if(np.linalg.norm(point - selectable.origin) < 25):
                    if(end):
                        self.magnetToAnotherWall = True
                    return selectable.origin
                if(np.linalg.norm(point - selectable.end) < 25):
                    if(end):
                        self.magnetToAnotherWall = True
                    return selectable.end
        return point

    def moveBeginWall(self, event):
        end = np.array([event.x + self.offsetXNew, event.y+ self.offsetYNew])
        end = self.magnet(end)
        self.canvas_id = self.canvas.create_line(self.currentWallEdit.origin[0],self.currentWallEdit.origin[1], end[0], end[1])
        self.canvas.after(10, self.canvas.delete, self.canvas_id)

    def endWall(self, event):
        end = np.array([event.x + self.offsetXNew, event.y+ self.offsetYNew])
        end = self.magnet(end, True)
        length = np.linalg.norm(end - self.currentWallEdit.origin)

        vectorOriginBasis = self.currentWallEdit.origin + self.currentDirectionForWall

        if(np.linalg.norm(vectorOriginBasis) != 0):
            vectorOriginBasis[0]/=(int)(np.linalg.norm(vectorOriginBasis))
            vectorOriginBasis[1]/=(int)(np.linalg.norm(vectorOriginBasis))
        else:
            print("error divide 0")

        vectorWall = end - self.currentWallEdit.origin
        if(np.linalg.norm(vectorWall) != 0):
            vectorWall[0]/=(int)(np.linalg.norm(vectorWall))
            vectorWall[1]/=(int)(np.linalg.norm(vectorWall))
        else:
            print("error divide 0 1")
        
        angle = np.arccos(np.vdot(vectorOriginBasis, vectorWall))
        self.currentWallEdit.length = length
        
        self.currentWallEdit.end = end
        self.canvas.create_line(self.currentWallEdit.origin[0],self.currentWallEdit.origin[1], end[0], end[1], width = self.currentWallEdit.width)
        self.listSelectable.append(self.currentWallEdit)
        self.currentWallEdit.updatePolygon()

        if(self.magnetToAnotherWall):
            self.stopAddWall(event)
        else:
            self.beginWallAddPoint(end)

        '''self.parent.after(100, self.defaultBind)
       
        self.defaultMessage()'''


    def stopAddWall(self,event):
        print("stop add wall")
        self.parent.after(100, self.defaultBind)
        self.defaultMessage()

    def defaultBind(self):
        # This is what enables scrolling with the mouse:
        #self.canvas.bind("<ButtonPress-3>", self.scroll_start)
        #self.canvas.bind("<B3-Motion>", self.scroll_move)
        #self.canvas.bind("<ButtonRelease-3>", self.scroll_end)
        self.canvas.bind("<ButtonPress-1>", self.click)
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.unbind("<Motion>")
        #self.canvas.bind("<ButtonPress-2>", self.scroll_move)
        #self.canvas.bind("<B2-Motion>", self.scroll_move)
        #self.canvas.bind("<MouseWheel>",self.zoomer)

    def defaultMessage(self):
        self.addMessage("")

    #-----Selection part-----#
    def click(self, event):
        utils = Utils()
        point = np.array([event.x, event.y])


        currentSelectable = None
        currentPolygonArea = 0
        for selectable in self.listSelectable:
            if(type(selectable) == Wall):
                selectable.__class__ = Wall
                polygon = selectable.polygon

                if(utils.isInsidePolygon(point, polygon) == True):
                    area = Utils.polygonArea(polygon)
                    if(area < currentPolygonArea or currentPolygonArea == 0):
                        currentSelectable = selectable
                        currentPolygonArea = area
        if(currentSelectable != None):
            polygon = currentSelectable.polygon
            self.canvas.create_line(polygon[0,0],polygon[1,0],polygon[0,1],polygon[1,1],polygon[0,2],polygon[1,2],polygon[0,3],polygon[1,3],polygon[0,0],polygon[1,0],width =3, fill='red')
