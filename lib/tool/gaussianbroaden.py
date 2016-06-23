#!/usr/bin/python

import numpy as np

def gbroaden(data, weight=None, xrange=None, sigma=None):
	num = len(data)
	if weight == None:
		print "PARAMETER weight IS NOT SET!"
		print "USE THE DEFAULT VALUE 1!"
		weight = [1.0 for i in range(num)]
	elif num != len(weight):
		print "WARNING: LEN(DATA)/=LEN(WEIGHT)!"
		print "ABANDON THE INFORMATION OF WEIGHT!"
		print "USE THE DEFAULT VALUE 1!"
		weight = [1.0 for i in range(num)]
	else:
		print "WEIGHT IS SET!"


	if xrange == None:
		xmin = min(data)
		xmax = max(data)
		print "PARAMTER xrange IS NOT SET!"
		print "THE DEFAULT RANGE IS: "
	else:
		xmin = xrange[0]
		xmax = xrange[1]
		print "THE RANGE IS:"
	print xmin, " ~ ", xmax
	delta = (xmax-xmin)/999.0
	x = [ delta*float(i)+xmin for i in range(1000)]
	y = [0.0 for i in range(1000)]

	if sigma == None:
		print "PARAMETER sigma IS NOT SET!"
		print "USE THE DEFAULT VALUE 0.1!"
		sigma = 0.1
	else:
		print "SIGMA:", sigma

	ssq = sigma**2.0
	for j, mu in enumerate(data):	
		for i in range(1000):
			gf = np.exp(-(x[i]-mu)**2/2/ssq)/np.sqrt(2*np.pi*ssq)
			y[i] = y[i]+weight[j]*gf

	result = [x, y]

	return result


