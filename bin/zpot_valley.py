#!/usr/bin/python

f = open("zpot.dat","r")

lines = f.readlines()

f.close()

data = [float(line.split()[1])for line in lines]

valleys = []

num = len(data)


for i in range(num):
	if i>0:
		im = i-1
	else:
		im = num-1

	if i<num-1:
		ip = i+1
	else:
		ip = 0

	if data[i] < data[im] and data[i] < data[ip]:
		valleys.append([i, data[i]])

for i, v in enumerate(valleys):
	if i==0:
		print v[0], v[1]
	else:
		print v[0], v[1], v[0]-valleys[i-1][0]

