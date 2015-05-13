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
        return 'Ingredient("{0}", {1}, "{2}", "{3}")'.format(self.name, \
            self.canBuy, self.color, self.shape)

# global definitions of ingredients
carrot = Ingredient('carrot', True,  'orange', 'triangle')
onion  = Ingredient('onion',  True,  'white',  'circle')
celery = Ingredient('celery', True,  'yellow', 'rectangle')
pepper = Ingredient('pepper', True,  'green',  'square')
garlic = Ingredient('garlic', True,  'tan',    'heart')
herbs  = Ingredient('herbs',  False, 'brown',  'hourglass')
