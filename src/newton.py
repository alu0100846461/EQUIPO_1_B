#! /usr/bin/python
#!encoding: UTF-8

from math import cos
from math import sin
PI = 3.141592653589793116

def f(x):
    return cos (PI * x)

def df(x):
    return - PI * sin (PI * x)

def newton (g, tol, nmax, it):
    if (it < nmax):
        if (df(g) != 0):
            g = g - (f(g)/df(g))
        else:
            return 1e7
        if (abs(f(g)) > tol):
            g = newton (g, tol, nmax, it)
            it = it + 1
        if (abs(f(g)) < tol):
            return g
    else:
        return 1e6

g = float(raw_input("\nProporcione una estimación para iniciar el cálculo: "))
tol = float(raw_input("Introduzca el margen de tolerancia: "))
nmax = int(raw_input("Indique la cantidad máxima de iteraciones: "))
it = 0
sol = newton (g, tol, nmax, it)
if (sol == 1e6):
    print "\n\tLo sentimos, no hemos localizado ninguna raíz \n\ttras alcanzar el máximo de iteraciones permitidas."
    print " \nInténtelo de nuevo proporcionando una mejor estimación como inicio del método,\no bien incrementando la cota de iteraciones.\n"
elif (sol == 1e7):
    print "\n\tHemos alcanzado una anulación de la derivada durante la ejecución, \n\tpor lo que el método no es aplicable para los valores aportados.\n"
    print "Inténtelo de nuevo modificando los parámetros iniciales.\n"
else:
    print "\nRaíz encontrada para la función:", sol, "\n"

