#!/usr/bin/python

import os
import sys

def GammaKpoint():
	if os.path.exists("KPOINTS"): 
		f = open("KPOINTS","r")
		lines = f.readlines()
		f.close()

		f = open("KPOINTS","w")
		for i, line in enumerate(lines):
			item = line.split()
			if i == 2:
				f.write("GAMMA\n")
			else:
				f.write(line)

		f.close()
	
