#!/usr/bin/python

from market import *

def makeOrder():
    order = Supply('order',0,0,0,0,0,0)
    for i in order.ingredients.keys():
        order.ingredients[i] =  input("How many " + i.name + "? ")
    return(order)

