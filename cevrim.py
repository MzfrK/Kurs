import matplotlib.pyplot as plt
import numpy as np

Pmin=2*10**5
Pmax=20*10**5
Vmax= 0.05
gama=1.66    # Tek Atomlu Gaz

#Carnot Çevrimi
VA= 0.012

plt.figure()
plt.subplot(221)

K1C= Pmin*Vmax
V = np.linspace(VA,Vmax,num=100)
P=K1C/V
plt.plot(V,P/10**3,'b-')

K2C= VA**(gama-1)*K1C
Vmin=(K2C/Pmax)**(1/gama)
V = np.linspace(Vmin,VA,num=100)
P=K2C/(V**gama)
plt.plot(V,P/10**3,'b-')

K3C= Pmax*Vmin
K4C= Pmin*(Vmax)**gama
VC=(K4C/K3C)**(1/(gama-1))
V = np.linspace(Vmin,VC,num=100)
P=K3C/V
plt.plot(V,P/10**3,'b-')

V = np.linspace(VC,Vmax,num=100)
P=K4C/(V**gama)
plt.plot(V,P/10**3,'b-')

plt.title('Carnot Cycle',size='xx-large',color='b')
plt.xlabel('Volume, $m^3$',{'fontsize': 13},horizontalalignment='right', x=0.8)
plt.ylabel('Pressure,kPa',{'fontsize': 13})
plt.grid(which='major', linestyle='--', linewidth='1.0', color='k')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='k')
plt.axis([0.,0.06,1*10**5/10**3,21*10**5/10**3])

# Otto Çevrimi
Vmin=0.02

plt.subplot(222)

K1O= Pmin*Vmax**gama
V = np.linspace(Vmin,Vmax,num=100)
P=K1O/V**gama
plt.plot(V,P/10**3,'r-')

PA=K1O/Vmin**gama
VminO=100*[Vmin]
P = np.linspace(PA,Pmax,num=100)
plt.plot(VminO,P/10**3,'r-')

K3O= Pmax*Vmin**gama
V = np.linspace(Vmin,Vmax,num=100)
P=K3O/V**gama
plt.plot(V,P/10**3,'r-')

PC=K3O/Vmax**gama
VmaxO=100*[Vmax]
P = np.linspace(Pmin,PC,num=100)
plt.plot(VmaxO,P/10**3,'r-')

plt.title('Otto Cycle',size='xx-large',color='r')
plt.xlabel('Volume, $m^3$',{'fontsize': 13},horizontalalignment='right', x=0.8)
plt.ylabel('Pressure,kPa',{'fontsize': 13})
plt.grid(which='major', linestyle='--', linewidth='1.0', color='k')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='k')
plt.axis([0.,0.06,1*10**5/10**3,21*10**5/10**3])

# Diesel Çevrimi
VB= 0.02

plt.subplot(223)

K1D= Pmin*Vmax**gama
VminD=(K1D/Pmax)**(1/gama)
V = np.linspace(VminD,Vmax,num=100)
P=K1D/V**gama
plt.plot(V,P/10**3,'g-')

PmaxD= np.around(100*[Pmax],decimals=1)
V = np.linspace(VminD,VB,num=100)
plt.plot(V,PmaxD/10.**3,'g-')

K3D= Pmax*VB**gama
V = np.linspace(VB,Vmax,num=100)
P=K3D/V**gama
plt.plot(V,P/10**3,'g-')

PD=K3D/Vmax**gama
VmaxD=100*[Vmax]
P = np.linspace(Pmin,PD,num=100)
plt.plot(VmaxD,P/10**3,'g-')

plt.title('Diesel Cycle',size='xx-large',color='g')
plt.xlabel('Volume, $m^3$',{'fontsize': 13},horizontalalignment='right', x=0.8)
plt.ylabel('Pressure,kPa',{'fontsize': 13})
plt.grid(which='major', linestyle='--', linewidth='1.0', color='k')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='k')
plt.axis([0.,0.06,1*10**5/10**3,21*10**5/10**3])

#Stirling Çevrimi
Vmin= 0.02

plt.subplot(224)

K1S= Pmin*Vmax
PA=K1S/Vmin
V = np.linspace(Vmin,Vmax,num=100)
P=K1S/V
plt.plot(V,P/10**3,'y-')

VminS=100*[Vmin]
P = np.linspace(PA,Pmax,num=100)
plt.plot(VminS,P/10**3,'y-')

K3S= Pmax*Vmin
PC=K3S/Vmax
V = np.linspace(Vmin,Vmax,num=100)
P=K3S/V
plt.plot(V,P/10**3,'y-')

VmaxS=100*[Vmax]
P = np.linspace(Pmin,PC,num=100)
plt.plot(VmaxS,P/10**3,'y-')

plt.title('Stirling Cycle',size='xx-large',color='y')
plt.xlabel('Volume, $m^3$',{'fontsize': 13},horizontalalignment='right', x=0.8)
plt.ylabel('Pressure,kPa',{'fontsize': 13})
plt.grid(which='major', linestyle='--', linewidth='1.0', color='k')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='k')
plt.axis([0.,0.06,1*10**5/10**3,21*10**5/10**3])

plt.subplots_adjust(top=0.92, bottom=0.09, left=0.05, right=0.95, hspace=0.8, wspace=0.45)
plt.show()

##############