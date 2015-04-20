#!/usr/bin/python

from market import *

def collectOrder():
    order = Supply('order',0,0,0,0,0,0)
    for i in order.ingredients.keys():
        try:
            chips = int(input("How many " + i.name + "? "))
            order.ingredients[i] = chips
        except ValueError:
            order.ingredients[i] = 0
    return(order)

