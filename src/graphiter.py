#! /usr/bin/python
#!encoding: UTF-8

import matplotlib.pyplot as pl
pl.rc('text', usetex=True)
pl.rc('font', family='Bookman')

name = raw_input("Introduzca el nombre del fichero para lectura: ")
f = open(name, "r")

flag = 0
X = []
Y = []

while (True):
    l = f.readline().rstrip()
    if (l == ""):
        break
    elif (l != "0") and (l != "1"):
        Y = Y + [flag-1]
        flag = 0
    else:
        flag += 1

f.close()

for i in range (20, 50):
    x0 = i/100.0
    dif = 0.5 - x0
    X = X + [dif]

pl.plot(X,Y,"b")
pl.title(r'Evoluci\'on en el n\'umero de iteraciones del m\'etodo de Newton') 
pl.xlabel(r'Error absoluto de la estimaci\'on inicial')
pl.ylabel('Cantidad de iteraciones')

pl.xlim(-0.05, 0.35)
pl.ylim(0.8, 3.2)

pl.savefig("iterevol.eps", dpi=72)
pl.show()

