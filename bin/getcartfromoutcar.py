#!/usr/bin/python
import os

#f = os.popen("head -n 8 POSCAR")
f = open("POSCAR","r")
lines = f.readlines()
f.close()

natom = sum([float(item) for item in lines[6].split()])
flags = []
for i, line in enumerate(lines):
	if i < 8:
		print line[:-1]
	elif i>8 and i<(natom+9):
		flags.append(line.split()[3:6])
print "Cart"

f = os.popen("grep NIONS OUTCAR")
line = f.readline()
nions = int(line.split()[-1])

cmd = "grep -A "+str(nions+1)+" TOTAL-FORCE OUTCAR | tail -"+str(nions)
f = os.popen(cmd)
lines = f.readlines()
for i, line in enumerate(lines):
	print " ".join(line.split()[0:3]+flags[i])
