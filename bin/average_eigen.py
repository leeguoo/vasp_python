#!/usr/bin/python

import sys

num = sys.argv[1]

f = open("EIGENVAL","r")
lines = f.readlines()
f.close()

w = []
eigenval = []

for i, line in enumerate(lines):
	items = line.split()
	if len(items) == 4 and i > 5:
		w.append(float(items[-1]))
	if len(items) > 0 and items[0] == str(num):
		eigenval.append(float(items[-1]))

tot = 0.0

for i, item in enumerate(w):
	print eigenval[i], item
	tot = tot+item*eigenval[i]

print "==========================="
print tot

