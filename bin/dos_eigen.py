#!/usr/bin/python

from vasp.eigenval import eigenval
from tool.gaussianbroaden import gbroaden
import numpy as np
import os

line = os.popen("grep E-fermi OUTCAR | tail -1").readline()
ef = float(line.split()[2])

e = eigenval()

data = []
weight = []
for i, item in enumerate(e.data):
	num = len(item)
	weight = weight+[e.weight[i] for j in range(num)] 
	data = data+[energy-ef for energy in item]


result = gbroaden(data, weight, xrange=[-5,5], sigma=0.05)

x = result[0]
y = result[1]

f = open("dos","w")
for i in range(len(x)):
	string = "{0:8.3f} {1:8.3f}".format(x[i], y[i])
	f.write(string+"\n")
f.close()

