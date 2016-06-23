#!/usr/bin/python

from file.openfile import openfile

class eigenval(object):
	def __init__(self):
		self.lines = openfile("EIGENVAL")
		self.head()
		self.getdata()

	def head(self):
		item = self.lines[5].split()
		nkpoint = item[1]
		print "NUMBER OF KPOINTS: " + nkpoint
		self.nkpoint = int(nkpoint)
		nband = item[2]
		print "NUMBER OF BANDS: " + nband
		self.nband = int(nband)

		return self.nkpoint, self.nband

	def getdata(self):
		data = [[] for e in range(self.nkpoint)]
		kp = []
		weight = []
		for i, line in enumerate(self.lines):
			if i > 5:
				j = (i-6)/(self.nband+2)
				k = (i-6)%(self.nband+2)
				if k > 1:
					item = line.split()
					data[j].append(float(item[1]))
				elif k == 1:
					item = [float(e) for e in line.split()]
					kp.append(item[:3])
					weight.append(item[3])
		self.kp = kp
		self.weight = weight
		self.data = data
		return self.data






