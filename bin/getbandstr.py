#!/usr/bin/python
from band.maker import bandmaker
#from band.plotter import plotter
import sys

a = sys.argv

band = bandmaker()

if "-align" in a:
	band.alignfermi()

for i, e in enumerate(a):
	if e == "--yr":
		yr = [float(a[i+1]), float(a[i+2])]
		break
	else:
		yr = None

x = band.x
ys = band.ys

f = open("band.dat","w")
for y in ys:
	for i, yy in enumerate(y):
		f.write("{0:4.4f} {1:4.4f}\n".format(x[i], yy))
	f.write("\n")
f.close()

#plot = plotter(band, yr)

#if "-hsk" in a:
#	plot.plothsk()
       	
#plot.show()
