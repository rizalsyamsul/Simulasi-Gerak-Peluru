# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 09:11:31 2020

@author: Sam
"""
import math
import matplotlib.pyplot as plt
import numpy

#array
x = numpy.zeros((1000))
y = numpy.zeros((1000))
xHambatan = numpy.zeros((1000))
yHambatan = numpy.zeros((1000))
xAnalitik = numpy.zeros((1000))
yAnalitik = numpy.zeros((1000))

#deklarasi variabel
m = 0.15
v0 = 50
sudut = 35
d = 0.0013
perubahanwaktu = 0.01
g = 9.806
t = 0

#tanpa hambatan udara
ax = 0
ay = -g
vx = v0 * math.cos(math.radians(sudut))
vy = v0 * math.sin(math.radians(sudut))

#dengan hambatan udara
vxHambatan = v0 * math.cos(math.radians(sudut))
vyHambatan = v0 * math.sin(math.radians(sudut))

#analitik
vxAnalitik = v0 * math.cos(math.radians(sudut))
vyAnalitik = v0 * math.sin(math.radians(sudut))

#perhitungan tanpa hambatan udara
i = 0
while x[i] >= 0 and y[i] >= 0:
  #posisi x
  vx = vx + (ax * perubahanwaktu)
  x[i+1] = x[i] + (vx * perubahanwaktu)
  #posisi y
  vy = vy + (ay * perubahanwaktu)
  y[i+1] = y[i] + (vy * perubahanwaktu)
  
  i= i + 1

#perhitungan dengan hambatan udara
j = 0
while xHambatan[j] >= 0 and yHambatan[j] >= 0:
  vHambatan = ((vxHambatan**2) + (vyHambatan**2))**0.5
  #posisi x
  axHambatan = -(d/m)*(vHambatan*vxHambatan)
  vxHambatan = vxHambatan + (axHambatan * perubahanwaktu)
  xHambatan[j+1] = xHambatan[j] + (vxHambatan * perubahanwaktu)
  #posisi y
  ayHambatan = -g -(d/m)*(vHambatan*vyHambatan)
  vyHambatan = vyHambatan + (ayHambatan * perubahanwaktu)
  yHambatan[j+1] = yHambatan[j] + (vyHambatan * perubahanwaktu)
  j= j + 1
  
  
#perhitungan dengan analitik
k = 0
while xAnalitik[k-1] >= 0 and yAnalitik[k-1] >= 0 :
  #posisi x
  xAnalitik[k] = xAnalitik[0] + (vxAnalitik * t) + (0.5 * ax * t**2)
  #posisi y
  yAnalitik[k] = yAnalitik[0] +(vyAnalitik * t) + (0.5 * ay * t**2)
  k = k + 1
  t = t + perubahanwaktu

#proyeksi
plt.title('Soal1')
plt.xlabel('Jarak')
plt.ylabel('Ketinggian')
plt.plot(x,y,'b')
plt.plot(xHambatan,yHambatan,'r-o')
plt.legend(['Tanpa Hambatan Udara','Dengan Hambatan Udara'],loc = 'best')
plt.show()
print('Posisi objek ketika menyentuh tanah tanpa hambatan udara : ',x[i])
print('Posisi objek ketika menyentuh tanah dengan hambatan udara : ',xHambatan[j]) 

plt.title('Soal2')
plt.xlabel('Jarak')
plt.ylabel('Ketinggian')
plt.plot(x,y,'b')
plt.plot(xAnalitik,yAnalitik,'r')
plt.legend(['Numerik','Analitik'],loc = 'best')
plt.show()
print('Posisi objek ketika menyentuh tanah Numerik: ',x[i])
print('Posisi objek ketika menyentuh tanah Analitik: ',xAnalitik[k-1]) 