import tkinter as tk
from Thumb import *
from InteractiveView import *
from MenuBar import *
from win32api import GetMonitorInfo, MonitorFromPoint
import subprocess

class MainApplication(tk.Tk):
	def __init__(self, parent):
		tk.Frame.__init__(self, parent)
		self.parent = parent
		monitor_info = GetMonitorInfo(MonitorFromPoint((0,0)))
		work_area = monitor_info.get("Work")
		self.width =  root.winfo_screenwidth()
		self.height =  root.winfo_screenheight()
		self.parent.geometry("%dx%d+0+0" % (self.width/2, self.height-95))
		#Frame
		self.frameThumb = tk.Frame(parent,  height = int(2*self.height/3), width = int(self.width/2))
		self.frameInteractiveView = tk.Frame(parent, height = int(self.height/3), width = int(self.width/2))
		self.frameThumb.pack(fill=tk.BOTH, expand=True)
		self.frameInteractiveView.pack(fill=tk.BOTH, expand=True)

		#menu bar
		self.menu = MenuBar(self)
		self.parent.config(menu = self.menu.menuBar)

		#interactive view
		self.interactiveView = InteractiveView(self,self.frameInteractiveView)
		self.interactiveView.canvas.grid(row=0, column=0, sticky="nsew")
		self.frameInteractiveView.grid_rowconfigure(0, weight=1)
		self.frameInteractiveView.grid_columnconfigure(0, weight=1)

		#thumb
		self.thumb = Thumb(self.frameThumb,self.interactiveView )
		self.thumb.thumb.pack(fill = tk.BOTH, expand = True)
		
		#init blender
		self.initBlender()

	def initBlender(self):
		listArg = [self.menu.defaultPathBlender] 
		#use blender arguments to initialize it
		#https://docs.blender.org/manual/en/latest/advanced/command_line/arguments.html
		#open a script when blender is open
		listArg.append('-P')
		listArg.append('initBlenderScript.py')
		#Set the position and the size of the windows
		listArg.append('--window-geometry')

		#TODO: change this to have more generally settings 
		listArg.append('960') #position x
		listArg.append('0') #position y
		listArg.append('960') #size x
		listArg.append('1080') #size y
		
		subprocess.Popen(listArg)

if __name__ == "__main__":
	root = tk.Tk()
	main = MainApplication(root)
	
	root.mainloop()
