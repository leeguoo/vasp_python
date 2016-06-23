#!/usr/bin/python

def openfile(filename):
	"""
	Find and open the file.
	If DOSCAR is not found, error message will be printed,
	and the job will stop.
	"""
	
	try:
		f = open(filename,"r")
		print filename + " IS FOUND!"
	except:
		print "ERROR: NO " + filename
	
	lines = f.readlines()
	f.close()
	return lines

