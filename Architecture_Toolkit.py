import tkinter as tk
from Thumb import *
from MenuBar import *

class MainApplication(tk.Tk):
	def __init__(self, parent):
		tk.Frame.__init__(self, parent)
		self.parent = parent
		self.width  = root.winfo_screenwidth()
		self.height = root.winfo_screenheight()

		#Frame
		self.frameThumb = tk.Frame(parent,  height = int(2*self.height/3), width = int(self.width/2))
		self.frameTopView = tk.Frame(parent, height = int(self.height/3), width = int(self.width/2), bg = 'blue')
		self.frameThumb.pack(fill=tk.BOTH, expand=True)
		self.frameTopView.pack(fill=tk.BOTH, expand=True)

		#init class
		self.thumb = Thumb(self.frameThumb)
		self.thumb.thumb.pack(fill = tk.BOTH, expand = True)

		self.menu = MenuBar(self)
		
		self.parent.config(menu = self.menu.menuBar)

if __name__ == "__main__":
	root = tk.Tk()
	main = MainApplication(root)#.pack(side="top", fill = "both", expand = True)
	width  = root.winfo_screenwidth()
	height = root.winfo_screenheight()
	
	#root.state('zoomed')
	root.geometry(f'{int(width/2)}x{height}')
	root.mainloop()

#from tkinter import *

#class Frame1(Frame):
#    def __init__(self, parent):
#        Frame.__init__(self, parent, bg="red")
#        self.parent = parent
#        self.widgets()

#    def widgets(self):
#        self.text = Text(self)
#        self.text.insert(INSERT, "Hello World\t")
#        self.text.insert(END, "This is the first frame")
#        self.text.grid(row=0, column=0, padx=20, pady=20) # margins


#class MainW(Tk):

#    def __init__(self, parent):
#        Tk.__init__(self, parent)
#        self.parent = parent
#        self.mainWidgets()

#    def mainWidgets(self):

#        self.label1 = Label(self, text="Main window label", bg="green")
#        self.label1.grid(row=0, column=0)

#        self.label2 = Label(self, text="Main window label", bg="yellow")
#        self.label2.grid(row=1, column=0)

#        self.window = Frame1(self)
#        self.window.grid(row=0, column=10, rowspan=2)

#if __name__=="__main__":
#    app = MainW(None)
#    app.mainloop()
