#!/usr/bin/python

import tkinter 
from market import *
from interaction import *

class simpleapp(tkinter.Tk):
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

      # widget for box to type in
      # self.entryVariable = tkinter.StringVar()
      # self.entry = tkinter.Entry(self, textvariable=self.entryVariable)
      # self.entry.grid(column=0,row=1,sticky='EW')
      #this widget will stick to the East and West edges of its cell
      # self.entry.bind("<Return>", self.OnPressEnter)
      # self.entryVariable.set(u"Welcome to Simmer")

      # widgets for buttons
        shop = tkinter.Button(self,text=u"Market", command=self.WantToShop)
        shop.grid(column=0,row=0)
      # button2 = tkinter.Button(self,text=u"Study")
      # button2.grid(column=1, row=1)
      # button3 = tkinter.Button(self,text=u"Kitchen")
      # button3.grid(column=1, row=2)

        self.cropsVariable = tkinter.StringVar()
        self.cropsVariable.set(farmersMarket.display())
        crops = tkinter.Label(self, textvariable=self.cropsVariable,
                             anchor="w", fg="black", bg="green")
        crops.grid(column=2, row=0, columnspan=5, sticky='EW')
      
      # widget for a label
        self.messageLine = tkinter.StringVar()
        message = tkinter.Label(self, textvariable=self.messageLine,
                             anchor="w", fg="black", bg="green")
        message.grid(column=1, row=10, columnspan=5, sticky='EW')
      # self.labelVariable.set(u"Action")

      #tell layout manager to resize column 1 when resizing
        self.grid_columnconfigure(1,weight=1)
      #prohibit window resizing
      #self.resizable(False,False)

    def WantToShop(self):
        self.messageLine.set("You want to go to the Farmers Market")
        iWant = makeOrder()
        try:
            checkRequest(iWant)
            self.messageLine.set(iWant.display())
        except ValueError as e:
            self.messageLine.set(e)  
            return

   # def OnPressEnter(self,event):
     # self.labelVariable.set(self.entryVariable.get()+"You pressed Enter!")


if __name__ == "__main__":
    app = simpleapp(None)
    app.title('Simmer')
    app.mainloop()
