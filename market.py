#!/usr/bin/python

class Ingredient:
   def __init__(self, name, canBuy, color, shape):
      self.name = name
      self.canBuy = canBuy
      self.color = color
      self.shape = shape

   def __str__(self):
      return 'Ingredient("%s", %s, "%s", "%s")' % (self.name, self.canBuy, self.color, self.shape)

carrot = Ingredient('carrot', True,  'orange', 'triangle')
onion  = Ingredient('onion',  True,  'white',  'circle')
celery = Ingredient('celery', True,  'yellow', 'rectangle')
pepper = Ingredient('pepper', True,  'green',  'square')
garlic = Ingredient('garlic', True,  'tan',    'heart')
herbs  = Ingredient('herbs',  False, 'brown',  'hourglass')

players = 4
maxIngred = players+2

market = {i.name:maxIngred for i in [carrot,onion,celery,pepper,garlic]}
market[herbs.name]=5
