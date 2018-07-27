import timeit

import math



def sects(par, cit, itv):

sep = secc(par, itv)

for j in range(0, len(sep)):

if(abs(funct(sep[j])) <= 0.00000001):

return sep[j]

va = funct(sep[0])

for i in range(1, len(sep)):

vaux = funct(sep[i])

vaux = round(vaux,8)

if ((vaux > 0 and va > 0) or (vaux < 0 and va < 0)):

va = vaux

else: 

nitv = []

cit[0] = cit[0] + 1

nitv.append(sep[i-1])

nitv.append(sep[i]) 

return sects(par,cit, nitv)



def funct(it):

return round(((1-math.exp(-10*(it/68.1)))*((9.8*68.1)/it)-40), 8)



def secc(par, itv):

sc = round(abs((itv[1])-(itv[0]))/par, 8)

f = [] 

f.append(itv[0])

for i in range(0, par-1):

f.append(round(f[i]+sc, 8))

f.append(round(itv[1], 8))

return f



csec = 3

csecf = 4

print("")

cit = [0]

itv = [10, 20]

print("Resultados con 3 y 4 secciones mas cantidad de iteraciones")

print("")

print("3 secciones:", sects(csec, cit, itv), "+- 0.00000001")

print ("Cantidad de iteraciones con 3 secciones: ", cit)

print("4 secciones:", sects(csecf, cit, itv), "+- 0.00000001")

print("Cantidad de iteraciones con 4 secciones:", cit)