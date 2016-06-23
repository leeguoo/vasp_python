#!/usr/bin/python

import numpy as np

f = open("POSCAR","r")
lines = f.readlines()

vectors = []
vlens = []
for line in lines[2:5]:
	vector = np.array([float(item) for item in line.split()])
	vectors.append(vector) 
	vlen = np.sqrt(np.dot(vector, vector))
	vlens.append(vlen)

vmax = max(vlens)

for i in range(20):
	kpts = []
	for vlen in vlens:
		kpt = int(round((i+1)*vmax/vlen))
		kpts.append(kpt)
	print kpts[0], kpts[1], kpts[2]
