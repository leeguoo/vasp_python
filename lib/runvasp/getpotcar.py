#!/usr/bin/python

import os

def GetPotcar():
	if os.path.exists("potcars"):
		potdir = "~/pot/paw-pbe/"

		f = open("potcars","r")
		lines = f.readlines()
		f.close()
		ps = []
		for line in lines:
			ps.append(potdir+line.split()[0]+"/POTCAR")

		string = " ".join(ps)
		cmd = "cat " + string + " > POTCAR"
		os.system(cmd)
	else:
		"WARNING: potcars not exist!"
