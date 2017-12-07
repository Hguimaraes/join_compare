# -*- coding: utf-8 -*-
#UFRJ - Universidade Federal do Rio de Janeiro
#CBD - Construção de Bancos de Dados
#Grupo E - Heitor Guimaraẽs, Igor Amaral, Vinicius Almeida

#Directed Study 04 - Join Algorithms comparator

from BTrees.OOBTree import OOBTree
import datetime

#Setting Datasets filenames
left_o = "lefttable_ordered.txt"
left_un = "lefttable_unordered.txt"
right_o = "righttable_ordered.txt"
right_un = "righttable_unordered.txt"

limiter = ", "

#1a. Nested Loop in ordered and unordered files
#For this example, no data structure besides the original files are required.
#Since this is just to compare the matching time, we won't keep the results of the joins.

print "Calculating Ordered Nested Loop Join time"
start = datetime.datetime.now()
joinnum = 0;
left = open(left_o)
right = open(right_o)
for l1 in left:
	l_left = l1.split(limiter)
	for l2 in right:
		l_right = l2.split(limiter)
		if l_left[0] == l_right[1]:
			joinnum += 1
			right.seek(0)
			break
end = datetime.datetime.now()

print "Ordered Nested Loop Time: " + str((end-start).total_seconds()) + "sec."
print "Joined " + str(joinnum) + " lines."

print "Calculating Unordered Nested Loop Join time"
start = datetime.datetime.now()
joinnum = 0;
left = open(left_un)
right = open(right_un)
for l1 in left:
	l_left = l1.split(limiter)
	for l2 in right:
		l_right = l2.split(limiter)
		if l_left[0] == l_right[1]:
			joinnum += 1
			right.seek(0)
			break
end = datetime.datetime.now()

print "Unordered Nested Loop Time: " + str((end-start).total_seconds()) + "sec."
print "Joined " + str(joinnum) + " lines." 
