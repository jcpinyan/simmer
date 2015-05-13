#!/usr/bin/python

import csv
from ingredients import *


# class Recipe:
#     '''recipes available in the cookbooks'''
#     def __init__(self, name, resource, carrots, onions, celeries, \
#         peppers, garlics, ):
#         self.name = name
#         self.ingredients = OrderedDict([(carrot,carrots), \
#             (onion,onions), (celery,celeries), (pepper,peppers), \
#             (garlic,garlics), )])
# 
#     def __hash__(self):
#         return hash(self.name)
# 
#     def __str__(self):
#         return 'Supply("%s", %d, %d, %d, %d, %d, %d)' % (self.name, self.ingredients[carrot], self.ingredients[onion], self.ingredients[celery], self.ingredients[pepper], self.ingredients[garlic], self.ingredients[herbs])
# 
#     def publish(self):
#         '''prints name of Supply and how many of each item'''
#         print(self.name)
#         for (k,v) in self.ingredients.items():
#             print(k.name,v,sep='\t')
# 
#     def display(self):
#         '''prepares string of market status'''
#         status = str()
#         for (k,v) in self.ingredients.items():
#             status+=k.name+': '+str(v)+' '
#         return(status)
# 
#     def quantity(self):
#         '''finds how many Ingredients are in Supply'''
#         return( sum([v for v in self.ingredients.values()]) )



filename = 'recipes.csv'

cookbooks = [list() for n in range(3)]

with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    next(reader) # to skip the header row
    for row in reader:
        cookbooks[int(row[-1])-1].append(row)
#       cookbooks[int(row[int('level')])-1].append(row)
