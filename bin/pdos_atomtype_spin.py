#!/usr/bin/python
from dos.pdos_spin import pdos
#from dos.plotter import dosplotter

p = pdos()
p.get_all_pdos_sum()
p.output()


#dplot = dosplotter(p.dos.en, p.data)
#dplot.show()
