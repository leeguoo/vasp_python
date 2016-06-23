#!/usr/bin/python


"""
This version doesn't distinguish spin polarization.
"""

separation = "----------------------------------------"


class DOSCAR(object):
	"""
	This class is for getting data from DOSCAR!
	Needed file is DOSCAR!

	ARG:
	self.en:	
	"""

	def __init__(self):
		self.openfile()
		self.information()
		self.readDOS()

	def openfile(self):
		"""
		Find and open the DOSCAR.
		If DOSCAR is not found, error message will be printed,
		and the job will stop.
		"""
		try:
			f = open("DOSCAR","r")
			print separation
			print "DOSCAR IS FOUND!"
			print separation
		except:
			print "ERROR: NO DOSCAR IS FOUND!"
		
		self.lines = f.readlines()
		f.close()
		return self.lines

	def information(self):
		"""
		Get and print the general inforamtion of
		atom numbers, grid numbers, and the energy range.
		"""
		self.natom = int(self.lines[0].split()[0])
		print "ATOM NUMBERS: {0:8n}".format(self.natom)
		item = self.lines[5].split()
		emax = float(item[0])
		emin = float(item[1])
		print "ENERGY RANGE: {0:5.3f} ~ {1:5.3f}".format(emin, emax)
		self.ngrid = int(item[2])
		print "NUMBER OF GRID: {0:8n}".format(self.ngrid)

		num = len(self.lines)
		ndoscar = self.ngrid+6
		npdos = (self.ngrid+1)*self.natom+5
		if num < ndoscar:	
			print "ERROR: DOSCAR IS NOT COMPLETE"
		elif num < npdos:
			print "PDOS: ABSENT OR INCOMPLETE"
			self.__is_pdos__ = False
		else:
			print "PDOS: CONTAINED"
			self.__is_pdos__ = True
		
		return self.natom, self.ngrid, self.__is_pdos__

	def readDOS(self):
		"""
		Read the energies and total DOS from DOSCAR!
		"""
		print separation
		print "READING ENERGIES AND TOTAL DOS..."
		lines = self.lines
		en = []
		dos = []
		for i, line in enumerate(lines):
			if i>=6 and i<6+self.ngrid:
				data = [float(e) for e in line.split()]
				en.append(data[0])
				dos.append(data[1])
		self.en = en
		self.dos = dos
		print "DONE!"
		print separation
		return self.en, self.dos


	def readPDOS(self, SEL_ATOMS=None):
		"""
		Read PDOS!
		"""
		if not self.__is_pdos__:
			print "ERROR: PDOS IS NOT CONTAINED!"

		if SEL_ATOMS == None:
			print "NO ATOM IS SELECTED."
			print "THE PDOS OF ALL THE ATOMS WILL BE READ."
			atoms = range(self.natom)
		else:
			atoms = SEL_ATOMS
			string = ",".join(["{0:4n}".format(e) for e in atoms])
			print "THE SELECTED ATOMS: "+string
		#`	print "ONLY THE PDOS OF THE SELECTED ATOMS WILL BE READ."
		print "READING PDOS..."

		pdoses = []
		head0 = self.ngrid+6 # number of lines before PDOS

		for j in atoms:
			head = head0+j*(self.ngrid+1)
			pdos = []
			for i, line in enumerate(self.lines):
				if i>head and i<=head+self.ngrid:
					data = [float(e) for e in line.split()]
					pdos.append(data[1:])
			pdoses.append(pdos)
		self.pdoses = pdoses
		print "DONE!"
		print separation
		return self.pdoses
