#!/usr/bin/python

class Ingredient:
   def __init__(self, availability, color, shape):
      self.availability = availability
      self.color = color
      self.shape = shape

   def __str__(self):
      return 'Ingredient (%s, %s, %s)' % (self.availability, self.color, self.shape)
