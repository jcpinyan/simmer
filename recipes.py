#!/usr/bin/python

import csv

filename = 'recipes.csv'

cookbooks = [list() for n in range(3)]

with open(filename, newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter = ',')
    for row in reader:
        cookbooks[int(row['level'])-1].append(row)
