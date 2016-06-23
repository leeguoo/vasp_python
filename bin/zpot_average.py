#!/usr/bin/python
import sys

wide = int(sys.argv[1])
if wide%2 == 0:
	low = -wide/2
	high = wide/2
else:
	low = -wide/2
	high = wide/2


f = open("zpot.dat","r")

lines = f.readlines()

f.close()

data = [float(line.split()[1])for line in lines]

num = len(data)

aves = []
for i in range(num):
	p = 0.0
	for j in range(low,high):
		k = i+j
		if k<0:
			k = num+k
		if k>=num:
			k = k-num
		p = p+data[k]
	aves.append(p/wide)

for i, ave in enumerate(aves):
	print "{0:5n} {1:4.3f}".format(i, ave)

