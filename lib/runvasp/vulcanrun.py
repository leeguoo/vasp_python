#!/usr/bin/python
import os
def VulcanJobList():
	jobs = []
	lines =  os.popen("squeue -u guoli").readlines()
	for i, line in enumerate(lines):
		if i > 0:
			jobname = line.split()[2]
			jobid = line.split()[0]
			jobs.append([jobid, jobname])
	return jobs

