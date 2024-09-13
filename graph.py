import numpy as np
from math import pi
Jsma = 7.785672e11
Je = 0.0489
Rj = 69911000
Ms = 1.989e30
Rs1 = 6.957e+8


def TransitProb(a,b,c):
  equation = a/(b*(1-pow(c,2)))
  return equation

def TransitDepth(a,b):
  solve = pow(a/b,2)
  return solve

def Rplanet(a,b,c):
  solve = (a/b)**0.485*c
  return solve

#If M > 1.66*Ms
def RstarM(a,b,c):
  solve = 1.33*a*(b/c)**0.555
  return solve

Ms = 1.989e30
Rs1 = 6.957e+8
#If M < 1.66*Ms
def RstarL(a,b,c):
  solve = 1.06*a*(b/c)**0.945
  return solve
Rs = RstarL(Rs1,Ms,Ms)