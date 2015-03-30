#!/usr/bin/python

class Ingredient:
   def __init__(self, name, canBuy, color, shape):
      self.name = name
      self.canBuy = canBuy
      self.color = color
      self.shape = shape

   def __str__(self):
      return 'Ingredient("%s", %s, "%s", "%s")' % (self.name, self.canBuy, self.color, self.shape)
