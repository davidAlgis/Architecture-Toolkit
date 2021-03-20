import tkinter as tk
from Thumb import *
from InteractiveView import *
from MenuBar import *

class MainApplication(tk.Tk):
	def __init__(self, parent):
		tk.Frame.__init__(self, parent)
		self.parent = parent
		self.width  = root.winfo_screenwidth()
		self.height = root.winfo_screenheight()

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


if __name__ == "__main__":
	root = tk.Tk()
	main = MainApplication(root)#.pack(side="top", fill = "both", expand = True)
	width  = root.winfo_screenwidth()
	height = root.winfo_screenheight()
	
	#root.state('zoomed')
	root.geometry(f'{int(width/2)}x{height}')
	root.mainloop()
