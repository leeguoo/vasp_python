#!/usr/bin/python
from vasp.procar import procar

def en_kp_atom(nk, atomnum):
	pc = procar()
	data = pc.data[nk]
	en = pc.band[nk]

	result = [en,[]]
	for band in data:
		item = 0.0
		for i, ion in enumerate(band):
			if i in atomnum:
				item = item+sum(ion)
		result[1].append(item)
	return result

result = en_kp_atom(0, [70])
import pylab as plt
num = len(result[0])
for i in range(num):
	x = result[0][i]
	y = result[1][i]
	print i, x, y
#	plt.plot([x, x],[0, y], c = "b")
#plt.xlim = ([0.0,10.0])
#plt.show()
