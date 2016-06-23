#!/usr/bin/python
import pylab as plt

class dosplotter(object):

	def __init__(self, energy, dos):
		self.x = energy
		names = []
		ys = []
		for key in dos.keys():
			names.append(key)
			ys.append(dos[key])
		self.names = names
		self.ys = ys
		self.frame()
		self.plot()

	def frame(self): 
		return plt

	def plot(self):
		x = self.x[1:]
		ys = self.ys
		names = self.names
		for i, y in enumerate(ys):
			plt.plot(x, y[1:], label=names[i])
		plt.legend()
		return plt

	def show(self):
		plt.show()

	def save(self, filename="dos.pdf"):
		plt.savefig(filename)


