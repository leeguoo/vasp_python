#!/usr/bin/python
import os
import sys

#currentdir = os.path.dirname(os.path.realpath(__file__))
currentdir = "./"
def get_mp_list(path=currentdir):
	"""
	Get the name list of files or folders beginning with "mp".
	Default path: Current folder.
	"""
	dirlist0 = os.popen("ls "+path).readlines()
	dirlist = []
	for e in dirlist0:
		if e[:2]=="mp":
			dirlist.append(e[:-1])
	return dirlist

