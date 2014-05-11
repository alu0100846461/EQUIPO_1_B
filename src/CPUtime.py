#! /usr/bin/python
#!encoding: UTF-8

import matplotlib.pylab as pl
import numpy as np
import newton
import time

pl.rc('text', usetex=True)
pl.rc('font', family='Bookman')

g = (3.45,-5.8,-7.2,2.17)
tol = (10e-4,10e-5, 10e-7,10e-12)
nmax = (10,50,100,10)

X = []
Y = []

for i in range (0, 4):
    t0 = time.clock()
    for j in range (0, 10000):
        sol = newton.newton (g[i], tol[i], nmax[i], 0)
    tf = time.clock() - t0
    X = X + [i+1]
    Y = Y + [tf]

print Y

pl.plot(X,Y,'mp--')
pl.title(r'Costo computacional del m\'etodo de Newton') 
pl.xlabel(r'Cantidad de iteraciones (en decenas de miles)')
pl.ylabel(r'Tiempo de CPU (segundos)')

pl.xlim(0.5, 4.5)
pl.ylim(0, 0.2)

pl.savefig("CPUtime.eps", dpi=72)
pl.show()
