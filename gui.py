#!/usr/bin/python

import tkinter 

class simpleapp(tkinter.Tk):
   def __init__(self,parent):
      tkinter.Tk.__init__(self,parent)
      self.parent = parent
      self.initialize()

   def initialize(self):
      self.grid()

      # widget for box to type in
      self.entryVariable = tkinter.StringVar()
      self.entry = tkinter.Entry(self, textvariable=self.entryVariable)
      self.entry.grid(column=0,row=1,sticky='EW')
      #this widget will stick to the East and West edges of its cell
      self.entry.bind("<Return>", self.OnPressEnter)
      self.entryVariable.set(u"Welcome to Simmer")

      # widgets for buttons
      button = tkinter.Button(self,text=u"Market", command=self.OnButtonClick)
      button.grid(column=1,row=3)
      button2 = tkinter.Button(self,text=u"Study")
      button2.grid(column=1, row=1)
      button3 = tkinter.Button(self,text=u"Kitchen")
      button3.grid(column=1, row=2)

      # widget for a label
      self.labelVariable = tkinter.StringVar()
      label = tkinter.Label(self, textvariable=self.labelVariable,
                            anchor="w", fg="black", bg="green")
      label.grid(column=0, row=0, columnspan=2, sticky='EW')
      self.labelVariable.set(u"Simmer down there!")

      #tell layout manager to resize column 0 when resizing
      self.grid_columnconfigure(0,weight=1)
      #prohibit window resizing
      #self.resizable(False,False)

   def OnButtonClick(self):
      self.labelVariable.set(self.entryVariable.get()+"You want to go to the Farmers Market")

   def OnPressEnter(self,event):
     self.labelVariable.set(self.entryVariable.get()+"You pressed Enter!")


if __name__ == "__main__":
   app = simpleapp(None)
   app.title('simmer')
   app.mainloop()
