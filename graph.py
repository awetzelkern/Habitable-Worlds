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

data=pd.read_csv(('planet_data.csv'),header=[0],skiprows=[1])
data_v2=data.dropna()
data_v3=data_v2.drop(data_v2[data.MASS<0].index)

data_v3
print(data_v3)
Mj = 1.898e27

# loop and print results
MsSI = 1.989e30
TransitDepth_List = []
TransitProb_List = []
Mplanet = []
Mhost = []
HabitablePlanets = []
for i in range(len(data_v3["NAME"])):
  Mh = data.iloc[i]["MSTAR"]*MsSI
  if Mh<1.66*MsSI:
    Rh=1.06*Rs*pow(Mh/MsSI,0.945)
  else:
    Rh=1.33*Rs*pow(Mh/MsSI,0.555)

  Mp = data_v3.iloc[i]["MASS"]*1.898e27
  Ap = data_v3.iloc[i]["A"]*1.496e+11
  Ep = data_v3.iloc[i]["ECC"]
  Rp = pow(Mp/MsSI,0.485)*Rs
  TransitDepth_List.append(TransitDepth(Rp,Rs))
  TransitProb_List.append(TransitProb(Rh,Ap,Ep))
  Mplanet.append(Mp/9.223e18)
  Mhost.append(Mh/9.223e18)
  
plt.scatter(data_v3["MSTAR"],data_v3["MASS"],alpha=.4,s=13)
plt.xlabel("Host Star Mass (M☉)",size=15)
plt.ylabel("Exo-Planet Mass (M♃)",size=15)
plt.yscale("log")
plt.ylim(.09,50)
plt.xlim(0.2,3.5)
print(data_v3[data_v3['MASS']>21])
plt.title("Host Star Mass vs. Exo-Planet Mass",size=18)
print()

MsSI = 1.989e30
TransitDepth_List = []
TransitProb_List = []
Mplanet = []
Mhost = []
HabitablePlanets = []
for i in range(len(data_v3["NAME"])):
  Mh = data.iloc[i]["MSTAR"]*MsSI
  if Mh<1.66*MsSI:
    Rh=1.06*Rs*pow(Mh/MsSI,0.945)
  else:
    Rh=1.33*Rs*pow(Mh/MsSI,0.555)

  Mp = data_v3.iloc[i]["MASS"]*1.898e27
  Ap = data_v3.iloc[i]["A"]*1.496e+11
  Ep = data_v3.iloc[i]["ECC"]
  Rp = pow(Mp/MsSI,0.485)*Rs
  TransitDepth_List.append(TransitDepth(Rp,Rs))
  TransitProb_List.append(TransitProb(Rh,Ap,Ep))
  Mplanet.append(Mp/9.223e18)
  Mhost.append(Mh/9.223e18)
  
plt.scatter(data_v3["MSTAR"],data_v3["MASS"],alpha=.4,s=13)
plt.xlabel("Host Star Mass (M☉)",size=15)
plt.ylabel("Exo-Planet Mass (M♃)",size=15)
plt.yscale("log")
plt.ylim(.09,50)
plt.xlim(0.2,3.5)
print(data_v3[data_v3['MASS']>21])
plt.title("Host Star Mass vs. Exo-Planet Mass",size=18)
print()

HabitablePlanetsMSTAR = []
HabitablePlanetsMASS = []
Pass = []
for i in range(len(data_v3["NAME"])):
  Mh = data_v3.iloc[i]["MSTAR"]
  Sma = data_v3.iloc[i]["A"]
  Lh = HostStarLuminosity(Mh)
  HsystemC = HabitalZoneC(Lh)
  HsystemF = HabitalZoneF(Lh)
  Mass = data_v3.iloc[i]["MASS"]
  Pass.append(Mass)
  if Sma > HsystemC and Sma < HsystemF:
    HabitablePlanetsMSTAR.append(data_v3.iloc[i]["MSTAR"])
    HabitablePlanetsMASS.append(data_v3.iloc[i]["MASS"])
HabitablePlanetsMASS = np.array(HabitablePlanetsMASS)

plt.scatter(HabitablePlanetsMSTAR,HabitablePlanetsMASS,alpha=.4,s=13)
plt.xlabel("Host Star Mass (M☉)",size=15)
plt.ylabel("Exo-Planet Mass (M♃)",size=15)
plt.yscale("log")
plt.ylim(.09,50)
plt.xlim(0.2,3.5)
print(data_v3[data_v3['MASS']>21])
plt.title("Host Star Mass vs. Exo-Planet Mass",size=18)
print()

plt.figure(figsize=(15, 10))
plt.scatter(data_v3["MSTAR"],data_v3["MASS"], alpha=.9,c=data_v3["A"],cmap=plt.cm.get_cmap('RdPu_r'), s=data_v3["MASS"]*30)
cb = plt.colorbar()
cb.set_label(label='Semi-Major Axis (au)',fontsize=20)
plt.scatter(HabitablePlanetsMSTAR, HabitablePlanetsMASS,s=HabitablePlanetsMASS*30,c='black')
plt.xlabel("Host Star Mass (M☉)",fontsize=15)
plt.ylabel("Exo-Planet Mass (M♃)",size=15)
plt.plot([0, 3.5], [1, 1], 'k-', lw=1.5)
plt.yscale("log")
plt.ylim(.09,50)
plt.xlim(0.2,3.5)
print(data_v3[data_v3['MASS']>21])
plt.title("Host Star Mass vs. Exo-Planet Mass",size=18)
print()

plt.figure(figsize=(15, 10))
plt.scatter(data_v3["MSTAR"],data_v3["MASS"], alpha=.9,c=data_v3["A"],cmap=plt.cm.get_cmap('RdPu_r'), s=data_v3["MASS"]*30)
cb = plt.colorbar()
cb.set_label(label='Semi-Major Axis (au)',fontsize=20)
plt.scatter(HabitablePlanetsMSTAR, HabitablePlanetsMASS,s=HabitablePlanetsMASS*30,c='black')
plt.xlabel("Host Star Mass (M☉)",fontsize=15)
plt.ylabel("Exo-Planet Mass (M♃)",size=15)
plt.plot([0, 3.5], [1, 1], 'k-', lw=1.5)
plt.yscale("log")
plt.ylim(.09,50)
plt.xlim(0.2,3.5)
print(data_v3[data_v3['MASS']>21])
plt.title("Host Star Mass vs. Exo-Planet Mass",size=18)
print()