#!/usr/bin/python

from file.openfile import openfile

class procar(object):

	def __init__(self):
		self.lines = openfile("PROCAR")
		self.head()
		self.getdata()

	def head(self):
		item = self.lines[1].split()
		print self.lines[1][:-1]
		self.nkpoint = int(item[3])
		self.nband = int(item[7])
		self.nion = int(item[11])
		return self.nkpoint, self.nband, self.nion

	def getdata(self):
		kp = []
		band = [[] for i in range(self.nkpoint)]
		data = [[[] for i in range(self.nband)] for j in range(self.nkpoint)]
		for i, line in enumerate(self.lines):
			if i >= 2:
				item = line.split()
				if len(item)>=1:
					if item[0] == "k-point":
						nk = int(item[1])-1
						kp.append([float(e) for e in item[3:6]]+[float(item[8])])
						print "READING THE INFORMATION FOR KPOINT", nk
					elif item[0] == "band":
						nb = int(item[1])-1
						band[nk].append(float(item[4]))
					#elif int(item[0]) in range(self.nion+1):
					elif item[0] != "ion":
						data[nk][nb].append([float(e) for e in item[1:-1]])
		self.kp = kp
		self.band = band
		self.data = data
		return self.kp, self.band, self.data
				
