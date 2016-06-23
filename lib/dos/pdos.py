#!/usr/bin/python
from dos.doscar import DOSCAR

separation = "----------------------------------------"

class pdos(object):


	def __init__(self):
		self.dos = DOSCAR()
		self.readPOSCAR()


	def readPOSCAR(self):
		print separation
		try:
			print "POSCAR IS FOUND"
			f = open("POSCAR", "r")
		except:
			print "ERROR: NO POSCAR IS FOUND!"

		print separation
		lines = f.readlines()
		names = lines[5].split()
		print "ATOM NAMES: "+lines[5][:-1]
		natoms = [int(e) for e in lines[6].split()]
		print "ATOM NUMBERS: "+lines[6][:-1]

		aarange = []
		ai = 0
		for natom in natoms:
			af = ai+natom
			aa = range(ai, af)
			ai = af
			aarange.append(aa)

		self.names = names
		self.natoms = natoms
		self.atomrange = aarange

		return self.names, self.natoms, self.atomrange

	def get_atom_pdos_sum(self, atomtypenum): 
		i = atomtypenum
		name = self.names[i]
		print "GETTING PDOS OF {0:2s}".format(name)
		pdoses = self.dos.readPDOS(SEL_ATOMS=self.atomrange[i])
		p_sum = [0.0 for e in range(self.dos.ngrid)]
		for pdos in pdoses:
			for j, p in enumerate(pdos):
				p_sum[j]=p_sum[j]+sum(p)
		data = p_sum
		
		return data

	def get_single_pdos_sum(self, atomtypenum=0):
		name = self.names[atomtypenum]
		self.data = {name:self.get_atom_pdos_sum(atomtypenum)}
		return self.data

#	def get_selected_pdos_sum(self, atomnames)
#		self.data = []
#		for name in atomnames:
#			i = atomnames.index(name)

	def get_all_pdos_sum(self):
		self.data = {}
		for i, name in enumerate(self.names):
			self.data[name] = self.get_atom_pdos_sum(i)
		return self.data

	def output(self, filename="pdos.dat"):
		f = open(filename, "w")
		en = self.dos.en
		results = [en]
		for name in self.names:
			results.append(self.data[name])
		out = ["{0:12s}".format(e) for e in ["Energy"]+self.names]
		f.write(" ".join(out)+"\n")

		for i in range(len(en)):
			if i > 0:
				out = []
				for j in range(len(results)):
					string = "{0:12.4f}".format(results[j][i])
					out.append(string)
			
				f.write(" ".join(out)+"\n")


