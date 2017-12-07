# -*- coding: utf-8 -*-
#UFRJ - Universidade Federal do Rio de Janeiro
#CBD - Construção de Bancos de Dados
#Grupo E - Heitor Guimaraẽs, Igor Amaral, Vinicius Almeida
#Directed Study 04 - Join Algorithms comparator

from BTrees.OOBTree import OOBTree
import datetime
import linecache

#Setting Datasets filenames
left_o = "lefttable_ordered.txt"
left_un = "lefttable_unordered.txt"
right_o = "righttable_ordered.txt"
right_un = "righttable_unordered.txt"

delimiter = ", "

#1a. Nested Loop in ordered and unordered files
#For this example, no data structure besides the original files are required.
#Since this is just to compare the matching time, we won't keep the results of the joins.

print "Calculating Ordered Nested Loop Join time"
start = datetime.datetime.now()
joinnum = 0;
left = open(left_o)
right = open(right_o)
for l1 in left:
	l_left = l1.split(delimiter)
	for l2 in right:
		l_right = l2.split(delimiter)
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
	l_left = l1.split(delimiter)
	for l2 in right:
		l_right = l2.split(delimiter)
		if l_left[0] == l_right[1]:
			joinnum += 1
			right.seek(0)
			break
end = datetime.datetime.now()

print "Unordered Nested Loop Time: " + str((end-start).total_seconds()) + "sec."
print "Joined " + str(joinnum) + " lines." 

#1b. Merge-Join
#For a merge-join approach, both files should be ordered. Once again, we're not keeping the
#joined data on disk.

print "Calculating Merge-Join time"
start = datetime.datetime.now()
joinnum = 0
left = open(left_o)
right = open(right_o)
l_data = left.readline().split(delimiter)
r_data = right.readline().split(delimiter)
while True:
	if l_data[0] == r_data[1]:
		joinnum += 1
	if int(l_data[0]) < int(r_data[1]):
		line = left.readline()
		if line == "":
			break
		l_data = line.split(delimiter)
	else:
		line = right.readline()
		if line == "":
			break
		r_data = line.split(delimiter)
end = datetime.datetime.now()

print "Merge-Join Time: " + str((end-start).total_seconds()) + "sec."
print "Joined " + str(joinnum) + " lines."

#1c. Hash-join
#We'll use python dictionaries as Hashtables

print "Calculating Hash-Join time"
#Build
start = datetime.datetime.now()
j_hash = {}
position = 1
f = open(right_un)
for line in f:
	l = line.split(delimiter)
	j_hash[l[1]] = position
	position += 1

#Probe
joinnum = 0
left = open(left_un)
for line in left:
	l_data = line.split(delimiter)
	position = j_hash[l_data[0]]
	r_data = linecache.getline(right_un, position).split(delimiter)
	if l_data[0] == r_data[1]:
		joinnum += 1
end = datetime.datetime.now()

print "Hash-Join Time: " + str((end-start).total_seconds()) + "sec."
print "Joined " + str(joinnum) + " lines."
