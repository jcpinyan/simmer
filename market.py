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

from collections import OrderedDict

class Supply:
   '''Ingredients available in the market'''
   def __init__(self, name, carrots, onions, celeries, peppers, garlics, bouquets):
      try:
         assert isinstance(carrots,int) and isinstance(onions,int) and isinstance(celeries,int) and isinstance(peppers,int) and isinstance(garlics,int) and isinstance(bouquets,int)
      except AssertionError:
         print('ingredients must be ints')
         raise
      self.name = name
      self.ingredients = OrderedDict([(carrot,carrots), (onion,onions), (celery,celeries), (pepper,peppers), (garlic,garlics), (herbs,bouquets)])

   def __hash__(self):
      return hash(self.name)

   def __str__(self):
      return 'Supply("%s", %d, %d, %d, %d, %d, %d)' % (self.name, self.ingredients[carrot], self.ingredients[onion], self.ingredients[celery], self.ingredients[pepper], self.ingredients[garlic], self.ingredients[herbs])

   def publish(self):
      '''prints name of Supply and how many of each item'''
      print(self.name)
      for (k,v) in self.ingredients.items():
         print(k.name,v,sep='\t')


# initialize market
farmersMarket = Supply('farmersMarket',maxIngred,maxIngred,maxIngred,maxIngred,maxIngred,HERBS)

# initialize basket
basket = Supply('basket',0,0,0,0,0,0)

def checkMarket(farmersMarket,request):
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
      print('invalid request')
      return(False)
# TODO: error message so that it says specifically what is wrong with the request.


def transaction(basket,farmersMarket,request):
   '''moves Ingredients between two Supply objects
      example: get Ingredients from market for basket
      example: pay Ingredients from basket to market
   '''
   try:
      assert checkMarket(farmersMarket, request) and checkRequest(request)
   except AssertionError:
      print("Try again with a valid request for this market.")
      return(basket,farmersMarket)
   for (k,v) in request.ingredients.items():
      basket.ingredients[k]+=v
      farmersMarket.ingredients[k]-=v
   return(basket,farmersMarket)




   
