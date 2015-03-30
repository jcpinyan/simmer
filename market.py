#!/usr/bin/python

class Ingredient:
   '''Ingredients available in the market'''
   def __init__(self, name, canBuy, color, shape):
      self.name = name
      self.canBuy = canBuy
      self.color = color
      self.shape = shape

   def __hash__(self):
      return hash(self.name)

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

# initialize market
farmersMarket = {i:maxIngred for i in [carrot,onion,celery,pepper,garlic]}
farmersMarket[herbs]=5

# initialize basket
basket = {i:0 for i in farmersMarket}

def purchase(basket,farmersMarket,shoppingDict):
   '''moves requested items from farmers market to basket'''
   # verify that market has the requested amounts
   for (k,v) in shoppingDict.items():
      try:
         assert v <= farmersMarket[k]
      except AssertionError:
         print("Farmers Market only has",farmersMarket[k],k,"but you want",v)
         return(False)
   return(True)
   
