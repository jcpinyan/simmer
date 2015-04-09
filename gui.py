#!/usr/bin/python

import tkinter 

class simpleapp(tkinter.Tk):
   def __init__(self,parent):
      tkinter.Tk.__init__(self,parent)
      self.parent = parent
      self.initialize()

   def initialize(self):
      pass

if __name__ == "__main__":
   app = simpleapp(None)
   app.title('simmer')
   app.mainloop()
