#!/usr/bin/python

from collections import defaultdict

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

# global definitions of ingredients
carrot = Ingredient('carrot', True,  'orange', 'triangle')
onion  = Ingredient('onion',  True,  'white',  'circle')
celery = Ingredient('celery', True,  'yellow', 'rectangle')
pepper = Ingredient('pepper', True,  'green',  'square')
garlic = Ingredient('garlic', True,  'tan',    'heart')
herbs  = Ingredient('herbs',  False, 'brown',  'hourglass')

players = 4
maxIngred = players+2
HERBS = 5

class Supply:
   '''Ingredients available in the market'''
   def __init__(self, name, carrots, onions, celeries, peppers, garlics, bouquets):
      self.name = name
      self.ingredients = {carrot:carrots, onion:onions, celery:celeries, pepper:peppers, garlic: garlics, herbs: bouquets}
#      self.carrot = carrots
#      self.onion = onions
#      self.celery = celeries
#      self.pepper = peppers
#      self.garlic = garlics
#      self.herbs = herbs
#      self.veggies = carrots + onions + celeries + peppers + garlics
#      self.total = self.veggies + herbs

   def __hash__(self):
      return hash(self.name)

 #  def __str__(self):
 #     return 'Supply("%s", %d, %d, %d, %d, %d, %d)' % (self.name, self.carrot, self.onion, self.celery, self.pepper, self.garlic, self.herbs)

 #  def display(self):
 #     '''displays the contents of the basket formatted nicely'''
 #     return '%s\nCarrots: %d\nOnions: %d\nCeleries: %d\nPeppers: %d\nGarlics: %d\nHerb Bouquets: %d' % (self.name, self.carrot, self.onion, self.celery, self.pepper, self.garlic, self.herbs)

   def publish(self):
      '''prints name of Supply and how many of each item'''
      print(self.name)
      for (k,v) in self.ingredients.items():
         print(k.name,v,sep='\t')




# initialize market
#farmersMarket = {i:maxIngred for i in [carrot,onion,celery,pepper,garlic]}
#farmersMarket[herbs]=5
farmersMarket = Supply('farmersMarket',maxIngred,maxIngred,maxIngred,maxIngred,maxIngred,HERBS)

# initialize basket
# basket = {i:0 for i in farmersMarket}
basket = Supply('basket',0,0,0,0,0,0)

def checkMarket(basket,farmersMarket,request):
   '''verify that market has the requested amounts'''
   for (k,v) in request.ingredients.items():
      try:
         assert v <= farmersMarket.ingredients[k]
      except AssertionError:
         print("Farmers Market only has",farmersMarket.ingredients[k],k,"but you want",v)
         return(False)
   return(True)
   
def checkRequest(request):
   '''verify that request is valid'''
   inv_map = defaultdict(list) 
   for (k, v) in request.ingredients.items():
      inv_map[v].append(k)
   if len(inv_map[1]) == 3 and len(inv_map[0]) == 3 and request.ingredients[herbs] == 0:
      return(True)
   elif len(inv_map[2]) == 1 and len(inv_map[0]) == 5 and request.ingredients[herbs] == 0:
      return(True)
   elif request.ingredients[herbs] == 1 and len(inv_map[0]) == 5:
      return(True)
   else:
      return(False)
   
