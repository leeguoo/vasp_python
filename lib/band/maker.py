#!/usr/bin/python
from vasp.eigenval import eigenval
from vasp.kpoints import kpoints
from vasp.getfermi import getfermi
import numpy as np

class bandmaker(object):

	def __init__(self):
		print "GETTING INFORMATION FOR BAND STRUCTURES FROM EIGENVAL"
		eg = eigenval()
		self.data = eg.data
		self.kp = eg.kp
		self.nb = eg.nband
		self.turn_k_2_x()
		self.turn_band_2_ys()

	def turn_k_2_x(self):
		x = []
		xx0 = 0.0
		kp = [np.array(e) for e in self.kp]
		for i, k in enumerate(self.kp):
		        if i == 0:
		                xx = 0.0
		        else:
		                delta = k-kp[i-1]
		                xx = xx0+np.linalg.norm(delta)
		                xx0 = xx
		        x.append(xx)
		self.x = x
		return self.x


	def turn_band_2_ys(self):
		bands = []
		for i in range(self.nb):
			band = []
			for item in self.data:
				band.append(item[i])
			bands.append(band)
		self.ys = bands
		return self.ys

	def alignfermi(self, EF=None):
		if EF == None:
			print "EF IS NOT SET"
			print "READING FERMI ENERGY FROM OUTCAR"
			EF = getfermi()

		ys0 = self.ys
		ys = []
		for y0 in ys0:
			y = []
			for e in y0:
				y.append(e-EF)
			ys.append(y)
		self.ys = ys
		return ys
				
	def get_high_sym_kps(self):
		print "GETTING HIGH SYMMETRY KPOINTS FROM KPOINTS"
		kk = kpoints()
		data = kk.data

		hsk0 = []
		for i, kp in enumerate(self.kp):
			for k in data.keys():
				if kp == data[k]:
					hsk0.append([k, self.x[i]])
		hsk = []
		if len(hsk0)>0:
			print "THE HIGH SYMMETRY KPOINTS ARE:"
			for item in hsk0:
				if item not in hsk:
					hsk.append(item)
					print item[0], data[item[0]]
		else:
			print "WARNING: NO HIGH SYMMETRY KPOINT IS FOUND"
			print "CHECK THE KPOINT FILE, ADD SYMBOLS AFTER HSK COORDINATES"
		self.hsk = hsk
		return self.hsk

