#!/usr/bin/python

from file.openfile import openfile

lines = openfile("CONTCAR")
natoms = sum([int(e) for e in lines[6].split()])
print "TOTAL ATOM NUMBER: ", natoms

lines = openfile("OSZICAR")
for line in lines:
	item = line.split()
	if item[1]=="F=":
		energy = float(item[4])
print "TOTAL ENERGY: ", energy

print "ENERGY PER ATOM: ", energy/natoms
