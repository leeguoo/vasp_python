#!/usr/bin/python

import os
import sys

def ModifyIncar():
	if os.path.exists("INCAR"): 
		f = open("INCAR","r")
		lines = f.readlines()
		f.close()

		f = open("INCAR","w")
		for line in lines:
			item = line.split()
			if item[0]=="IBRION":
				f.write("IBRION = -1\n")
			elif item[0]=="NSW":
				f.write("NSW = 0\n")
			elif item[0]=="ICHARG":
				pass
			elif item[0]=="ISIF":
				pass
			elif item[0]=="NPAR":
				pass
			elif item[0]=="ICORELEVEL":
				pass
			elif item[0]=="ICHARG":
				pass
			else:
				f.write(line)

		f.write("ICORELEVEL = 1\n")
		f.close()
	
