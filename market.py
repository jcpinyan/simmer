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

class Supply:
   '''Ingredients available in the market'''
   def __init__(self, name, carrots, onions, celeries, peppers, garlics, bouquets):
      self.name = name
      self.carrots = carrots
      self.onions = onions
      self.celeries = celeries
      self.peppers = peppers
      self.garlics = garlics
      self.bouquets = bouquets

   def __hash__(self):
      return hash(self.name)

   def __str__(self):
      return 'Supply("%s", %d, %d, %d, %d, %d, %d)' % (self.name, self.carrots, self.onions, self.celeries, self.peppers, self.garlics, self.bouquets)

   def display(self):
      '''displays the contents of the basket formatted nicely'''
      return '%s\nCarrots: %d\nOnions: %d\nCeleries: %d\nPeppers: %d\nGarlics: %d\nHerb Bouquets: %d' % (self.name, self.carrots, self.onions, self.celeries, self.peppers, self.garlics, self.bouquets)


# initialize market
#farmersMarket = {i:maxIngred for i in [carrot,onion,celery,pepper,garlic]}
#farmersMarket[herbs]=5
farmersMarket = Supply('farmersMarket',maxIngred,maxIngred,maxIngred,maxIngred,maxIngred,5)

# initialize basket
# basket = {i:0 for i in farmersMarket}
basket = Supply('basket',0,0,0,0,0,0)

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
   
