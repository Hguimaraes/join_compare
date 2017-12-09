# -*- coding: utf-8 -*-
#UFRJ - Universidade Federal do Rio de Janeiro
#CBD - Construção de Bancos de Dados
#Grupo E - Heitor Guimaraẽs, Igor Amaral, Vinicius Almeida

#Data & relations generator for ED04
#Creates 4 files:
#Left Table Unordered
#Right Table Unordered
#Left Table Ordered
#Right Table Ordered
#Data values are integer that varies from 0 to 99

import random as rd
import sys
import datetime

size = int(sys.argv[1])
print "dataset size: " + sys.argv[1]

# Function to generate a random number between 0 and 99 to be our data
randval = lambda: rd.randint(0,99)

# Generating primary keys for left and right tables
left_pkeys = range(size)
right_pkeys = range(size)

#creating relations:
#format: {left table pkey, right table pkey}
rk = rd.sample(range(size), size)
relations = {i: val for i, val in enumerate(rk)}

#generating left table
#format: "pkey, data"
print "generating left table"
lt_data = ["{}, {}".format(k, randval()) for k in left_pkeys]


#generating right table
#format: "pkey, fkey, data"
print "generating right table"
rt_data = ["{}, {}, {}".format(k, relations[k], randval()) for k in right_pkeys]

print "Datasets generated!"

#creating left table ordered file
filename = "lefttable_ordered.txt"
print "Generating Left Table Ordered file..."
f = open(filename, "w")
for d in lt_data:
	f.write(d + "\n")

#creating left table unordered file
rd.shuffle(lt_data)
filename = "lefttable_unordered.txt"
print "Generating Left Table Unordered file..."
f = open(filename, "w")
for d in lt_data:
	f.write(d + "\n")

#creating right table ordered file
filename = "righttable_ordered.txt"
print "Generating Right Table Ordered file..."
f = open(filename, "w")
for d in rt_data:
	f.write(d + "\n")

#creating right table unordered file
rd.shuffle(rt_data)
filename = "righttable_unordered.txt"
print "Generating Right Table Unordered file..."
f = open(filename, "w")
for d in rt_data:
	f.write(d + "\n")

print "Done! All Files Created!"
