#!/usr/bin/python

from file.openfile import openfile

class kpoints(object):
	def __init__(self):
		self.lines = openfile("KPOINTS")
		self.head()
		self.getdata()

	def head(self):
		item = self.lines[1].split()
		num = int(item[0])
		
		if num == 0:
			self.kmode = "auto"
			print "THE KPOINTS ARE AUTOMATICALLY GENERATED"
		else:
			item = self.lines[2].split()[0]
			if item[0]=="l" or item[0]=="L":
				self.kmode = "band"
				print "THE KPOINTS FOR BAND STRUCTURE CALCULATION"
				print "EACH PATH CONTAINS {0:3n} KPOINTS".format(num)
			else:
				self.kmode = "all"
				print "ALL KPOINTS ARE EXPLICITLY ENTERED"
				print "THERE ARE {0:5n} KPOINTS IN TOTAL".format(num)

		return self.kmode

	def getdata(self):
		data = {}
		if self.kmode == "band":
			for i, line in enumerate(self.lines):
				if i > 3:
					item = line.split()
					num = len(item)
					if num > 0:
						name0 = item[-1]
						if name0[0]=="!":
							name = name0[1:]
							kp = [float(e) for e in item[:3]]
							data[name] = kp
		self.data = data
		return self.data






