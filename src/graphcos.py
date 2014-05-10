#! /usr/bin/python
#!encoding: UTF-8

from math import cos
import matplotlib.pylab as pl
import numpy as np
PI = 3.141592653589793116

pl.rc('text', usetex=True)

def f (x):
    return np.cos(PI*x)

def r (x):
    return 0

X = np.linspace(-3, 3, 2000, endpoint=True)
XB = np.linspace(-3.5, 3.5, 2000, endpoint=True)
K = np.linspace(-1.25, 1.25, 2000, endpoint=True)
Y = f(X)
C = []
for i in range (0, 2000):
    C = C + [0]

pl.plot(X,Y,'r')
pl.plot(XB,C,'g')
pl.plot(C,K,'g')
pl.title(r'Representaci\'on gr\'afica de la funci\'on $f(x) = cos(\pi x)$ en [-3, 3]') 
pl.xlabel('Valores de X')
pl.ylabel('Valores de f(x)')

pl.xlim(-3.5, 3.5)
pl.ylim(-1.25, 1.25)

pl.savefig("cos.eps", dpi=72)
pl.show()
