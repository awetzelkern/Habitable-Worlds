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

def shift(g,a,e,m,i,w):
  solve = np.sqrt(g/a*(1-pow(e,2))*(m*np.sin(i)/pow(w,.5)))
  return solve
g =  6.674e11

#Planet_Name=np.array['mercury','venus','earth','mars','jupiter','saturn','uranus','neptune','pluto']
Mplanet = np.array([0.330114e24,4.86747e24,5.97237e24,0.641712e24,1898.187e24,568.3174e24,86.8127e24,102.4126e24,0.013030e24])
Aplanet = np.array([5.790905e10,1.082e11,1.496e11,2.27987e+11,7.785672e11,1.433537e12,2.8750467e12,4.498408e12,5.9064381e12])
print('The Probability of Transit for our planets in the solar system is',TransitProb(Rs,Aplanet,0))
print('The radial velocity for our planets in the solar system is',shift(g,Aplanet,0,Mplanet,90,Ms))

Ls = 1
Ms = 1
o = 3.31e-12

def HostStarLuminosity(a):
  solve = Ls*pow(a/Ms,3.5)
  return solve

def HabitalZoneC(a):
  solve = pow(a/(4*pi*o*pow(373,4)),1/2)
  return solve
def HabitalZoneF(a):
  solve = pow(a/(4*pi*o*pow(273,4)),1/2)
  return solve

sunhzone = HabitalZoneF(Ls)
print(sunhzone)

import matplotlib.pyplot as plt
import matplotlib.colors as cl
import numpy as np
import pandas as pd

data=pd.read_csv(('fwOly9Fl.csv'),header=[0],skiprows=[1])
data_v2=data.dropna()
data_v3=data_v2.drop(data_v2[data.MASS<0].index)

data_v3
print(data_v3)
Mj = 1.898e27