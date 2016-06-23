#!/usr/bin/python

import numpy as np
from file.openfile import openfile

class poscar(object):

        def __init__(self):
                self.lines = openfile("POSCAR")
                self.head()
                self.getdata()

	def head(self):
		#atoms
		atomtypes = self.lines[5].split()
		atomnums = [int(e) for e in self.lines[6].split()]
		atoms = {}
		for i, atomtype in enumerate(atomtypes):
			atoms[atomtype] = atomnums[i]
		self.atomtypes = atomtypes
		self.atoms = atoms

		#lattice
		lscale = float(self.lines[1].split()[0])
		latt = []
		for i, line in enumerate(self.lines):
			items = line.split()
			if i in [2, 3, 4]:
				latt.append([lscale*float(e) for e in items])
			if items[0][0]=="D" or items[0][0]=="d":
				self.coordstart = i+1
				self.type = "direct"
			elif items[0][0]=="C" or items[0][0]=="c":
				self.coordstart = i+1
				self.type = "cart"
		self.latt = latt

		return self.atomtypes, self.atoms, self.latt, self.coordstart, self.type

	def getdata(self):
		vecs = []
		for i, line in enumerate(self.lines):
			if i >= self.coordstart:
				vecs.append([float(e) for e in line.split()[:3]])

		tlatt = np.transpose(np.matrix(self.latt))
		if self.type == "direct":
			self.fracs = vecs
			self.xyzs = [np.dot(tlatt,vec).tolist()[0] for vec in vecs]
		else:
			self.xyzs = vecs
			itlatt = np.linalg.inv(tlatt)
			self.fracs = [np.dot(itlatt,vec).tolist()[0] for vec in vecs] 

		return self.fracs, self.xyzs

#pos = poscar()
#print pos.atoms
#print pos.latt
#print pos.type
#print pos.coordstart
#print '---------'
#for frac in pos.fracs:
#	print frac
#print '---------'
#for xyz in pos.xyzs:
#	print xyz
