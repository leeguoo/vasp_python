#!/usr/bin/python
import os

def sp_finish(filename):
	_is_finished_ = False
	if os.path.exists(filename):
		#TO JUDGE WHETHER THE JOB ENDED NORMALLY
		filename = "'"+filename+"'"
		line = os.popen("tail -1 "+filename).readline()
		items = line.split()
		if len(items)>0:
			item = items[0]
			if item == "Voluntary":
				#TO JUDGE WHETHER THE NUMBER OF ELECTRONIC STEPS IS LESS THAN MAXIMUM
				line = os.popen("grep NELM "+filename).readline()
				maxstep = int(line.split()[2][:-1])

				line = os.popen("grep Iteration "+filename+" | tail -1").readline()
				step = int(line.split()[3][:-1])
				if step < maxstep:
					_is_finished_ = True

	return _is_finished_


