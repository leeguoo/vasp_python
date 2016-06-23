#!/usr/bin/python

def GetBatch(name="sys"):
	f = open("batch","w")
	f.write("#!/bin/bash\n")
	f.write("#SBATCH --job-name="+name+"\n")
	f.write("#SBATCH --partition=vulcan\n")
	f.write("#SBATCH --account=vulcan\n")
	f.write("#SBATCH --qos=normal\n")
	f.write("#SBATCH --nodes=8\n")
	f.write("#SBATCH --ntasks-per-node=8\n")
	f.write("#SBATCH --time=12:00:00\n")

	f.write("module load vasp\n")
	f.write("EXE='vasp'\n")
	f.write("mpirun $EXE\n")
	f.close()
