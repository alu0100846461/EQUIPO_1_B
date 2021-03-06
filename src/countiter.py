#! /usr/bin/python
#!encoding: UTF-8

from math import cos
from math import sin
PI = 3.141592653589793116

def f(x):
    return cos (PI * x)

def df(x):
    return - PI * sin (PI * x)

def newton (g, tol, nmax, it, name):
    if (it < nmax):
        if (df(g) != 0):
            g = g - (f(g)/df(g))
        else:
            return 1e7
        if (abs(f(g)) > tol):
            g = newton (g, tol, nmax, it, name)
            it = it + 1
        if (abs(f(g)) < tol):
            fich = open(name, "a")
            fich.write(str(it) + "\n")
            fich.close()
            return g
    else:
        return 1e6

tol = float(raw_input("\nIntroduzca el margen de tolerancia: "))
nmax = int(raw_input("Indique la cantidad máxima de iteraciones: "))
name = raw_input("Especifique un nombre para el fichero de salida: ")

for i in range (20, 50):
    x = i/100.0
    sol = newton (x, tol, nmax, 0, name)
    if (sol != 1e6) and (sol != 1e7):
        fich = open(name, "a")
        fich.write (str(x) + "\n")
        fich.close()

print "\nOperación realizada con éxito.\n"
    
