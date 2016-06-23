#!/usr/bin/python

import numpy as np
from vasp.poscar import poscar
import sys

def simplecleave001(layernum, vacuum):
	print "THIS CODE WILL CLEAVE A (001) SLAB!"
	pos = poscar()
	latt = pos.latt
	atomtypes = pos.atomtypes
	atoms = pos.atoms
	xyzs = pos.xyzs

	#atoms
	for k in atomtypes:
		atoms[k]=atoms[k]*layernum
	#coordinations_1
        slabxyzs = []
        for xyz in xyzs:
                for i in range(layernum):
			slabxyz = [xyz[j]+i*latt[2][j] for j in range(3)]
                        slabxyzs.append(slabxyz)

	#lattice
	vacnum = abs(vacuum/latt[2][2])
	slablatt = latt
	slablatt[2] = [layernum*e+vacnum*e for e in latt[2]]
	tlatt = np.transpose(np.matrix(slablatt))
	itlatt = np.linalg.inv(tlatt)

        #coordinations_2
	fracs = []
	for xyz in slabxyzs:
		frac = np.dot(itlatt,xyz).tolist()[0]
		fracs.append(frac)

	#write file
	f = open("slabposcar","w")
	string = str(layernum)+"L+"+str(vacuum)+"V\n"
	f.write(string)   #1st line
	f.write("1.0\n")  #2nd line
	#lattice
	for l in slablatt:
		string = "{0:5.5f} {1:5.5f} {2:5.5f}\n".format(l[0],l[1],l[2])
		f.write(string)
	#atomtype
	f.write(" ".join(atomtypes)+"\n")
	#atomnum
	atomnums = []
	for k in atomtypes:
		atomnums.append("{0:4n}".format(atoms[k]))
	string = " ".join(atomnums)+"\n"
	f.write(string)
	#coordination type
	f.write("Direct\n")
	#coordinations
	for frac in fracs:
		string = "{0:5.5f} {1:5.5f} {2:5.5f}\n".format(frac[0],frac[1],frac[2])
		f.write(string)
	print "SLAB COORDINATES ARE STORED IN FILE slabposcar!"
	f.close()

a = sys.argv
if "-L" in a:
	i = a.index("-L")
	layernum = int(a[i+1])
	print "THE NUMBER OF LAYERS IN THE SLAB: ", layernum
else:
	layernum = 1
        print "WARNING: NO LAYER NUMBER IS SET!"
        print "USING DEFAULT LAYER NUMBER:", layernum

if "-V" in a:
	i = a.index("-V")
	vacuum = float(a[i+1])
	print "THE VACUUM THICKNESS IS ", vacuum
else:
	vacuum = 20.0
	print "WARNING: NO VACUUM THICKNESS IS SET!"
	print "USING DEFAULT VACUUM THICKNESS:", vacuum

simplecleave001(layernum, vacuum)
