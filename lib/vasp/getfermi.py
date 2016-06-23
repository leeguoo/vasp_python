#!/usr/bin/python
import os

def getfermi():
	f = os.popen("grep E-fermi OUTCAR | tail -1")
	line = f.readline()
	item = line.split()
	fermi = float(item[2])
	return fermi
