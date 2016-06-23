#!/usr/bin/python


separation = "----------------------------------------"

import os

fs = os.popen("grep E-fermi OUTCAR | tail -1")
line = fs.readline()
EF =  float(line.split()[2])
print "GET FERMI ENRGY FROM OUTCAR"
print "FERMI ENERGY: {0:8.4f}".format(EF)


print "READING EIGENVAL..."
f = open("EIGENVAL","r")

lines = f.readlines()

item = lines[5].split()
nkpoint = int(item[1])
print "NUMBER OF KPOINTS: {0:8n}".format(nkpoint)
nband = int(item[2])
print "NUMBER OF BANDS: {0:8n}".format(nband)

nitem = len(lines[8].split())

#SEPERATE BANDS INTO VALENCE BANDS AND CONDUCTION BANDS
def getbandedges(nitem, num):
	vb = []
	cb = []
	for i, line in enumerate(lines):
		if i>5 and i<(len(lines)-2):
			if len(line.split())==nitem and len(lines[i+1].split())==nitem:
				e1 = float(line.split()[num])
				e2 = float(lines[i+1].split()[num])
				if e1 <= EF and e2 > EF:
					vb.append(e1)
					cb.append(e2)
	vbm = max(vb)
	cbm = min(cb)
	return [vbm, cbm]

if nitem==2:
	"NON-SPIN POLARIZED CALCULATIONS!"
	bm = getbandedges(nitem, 1)
	vbm = bm[0]
	print "VALENCE BAND MAXIMUM: {0:8.4f}eV ({1:8.4f}eV TO EF)".format(vbm, vbm-EF)
	cbm = bm[1]
	print "CONDUCTION BAND MINIMUM: {0:8.4f}eV ({1:8.4f}eV TO EF)".format(cbm, cbm-EF)
	print separation
	EG = cbm-vbm
	print "ENERGY BAND GAP: {0:8.4F}eV".format(EG)
if nitem==3:
	"SPIN POLARIZED CALCULATIONS!"
	vbm = []
	cbm = []
	for i in [1, 2]:
		bm = getbandedges(nitem, i)
		vbm.append(bm[0])
		cbm.append(bm[1])
	print "VALENCE BAND MAXIMUM:"
	print "    SPIN UP: {0:8.4f}eV ({1:8.4f}eV TO EF)".format(vbm[0], vbm[0]-EF)
	print "    SPIN DOWN: {0:8.4f}eV ({1:8.4f}eV TO EF)".format(vbm[1], vbm[1]-EF)
	print "CONDUCTION BAND MINIMUM:"
	print "    SPIN UP: {0:8.4f}eV ({1:8.4f}eV TO EF)".format(cbm[0], cbm[0]-EF)
	print "    SPIN DOWN: {0:8.4f}eV ({1:8.4f}eV TO EF)".format(cbm[1], cbm[1]-EF)
	print separation
	eg_up = cbm[0]-vbm[0]
	eg_down = cbm[1]-vbm[1]
	eg = min(cbm)-max(vbm)
	print "ENERGY BAND GAP: {0:8.4F}eV (UP: {1:8.4F}eV; DOWN: {2:8.4F}eV)".format(eg,eg_up,eg_down)


