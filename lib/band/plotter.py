#!/usr/bin/python
from band.maker import bandmaker
import pylab as plt

class plotter(object):
	def __init__(self, band, yrange=None):
		x = band.x
		ys = band.ys
		self.band = band
		self.plotdata(x, ys)
		self.plotframe(x, yrange)

	def plotframe(self, x, yrange):
		xmax = max(x)
		xmin = min(x)
		plt.xlim([xmin, xmax])

		if yrange == None:
			self.ymin, self.ymax = plt.ylim()
			print "WARNING: ENERGY RANGE IS NOT SET"
			print "The DEFAULT RANGE IS", plt.ylim()
		else:
			self.ymin = yrange[0]
			self.ymax = yrange[1]
			plt.ylim(yrange)
			print "THE ENERGY RANGE IS ", yrange
		return plt 


	def plotdata(self, x, ys):
		for y in ys:
			plt.plot(x, y, c='b')
		return plt

	def plothsk(self):
		print "PLOTTING HIGH SYMMETRY POINTS"
		self.band.get_high_sym_kps()
		hsk = self.band.hsk
		plt.xticks([e[1] for e in hsk], [e[0] for e in hsk])
		for e in hsk:
			plt.plot([e[1],e[1]], [self.ymin,self.ymax], ls='--', c="k")
		return plt

	def show(self):
		plt.show()

