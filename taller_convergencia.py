import math

def funcion(x):
  return round((((9.8*68.1)/x)*(1-math.exp(-(x/68.1)*10))-40), 6)

def verificar(intervalo):
  valor_inf = funcion(intervalo[0])
  valor_sup = funcion(intervalo[1])
  return round((valor_inf*valor_sup), 6)

def sub_intervalos(intervalo, numero_secciones):
  intervalos = []
  seccion = round(abs((intervalo[1])-(intervalo[0]))/numero_secciones, 6)
  intervalos.append(intervalo[0])
  for i in range(0, numero_secciones-1):
    intervalos.append(round(intervalos[i]+seccion, 6))
  intervalos.append(intervalo[1])
  return intervalos

def operacion(intervalo, numero_secciones, cantidad_iteraciones, xrs, errores_porcentuales):
  xr = round(((intervalo[0]+intervalo[1])/2), 8)
  xrs.append(xr)
  if (cantidad_iteraciones[0] > 0):
    error_porcentual = round(((xrs[cantidad_iteraciones[0]]-xrs[cantidad_iteraciones[0]-1])/xrs[cantidad_iteraciones[0]])*100, 8)
    errores_porcentuales.append(error_porcentual)
  intervalos = sub_intervalos(intervalo, numero_secciones)
  for i in range(0, len(intervalos)-1):
    intervalo = [intervalos[i], intervalos[i+1]]
    verificacion = verificar(intervalo)
    if (verificacion < 0):
      cantidad_iteraciones[0] = cantidad_iteraciones[0] + 1
      return (operacion(intervalo, numero_secciones, cantidad_iteraciones, xrs, errores_porcentuales))
    elif(verificacion == 0):
      return intervalo[1]
  
print("Ingrese el valor inferion: ", end="")
valor_inferior = int(input())
print("Ingrese el valor superior: ", end="")
valor_superior = int(input())
intervalo = [valor_inferior, valor_superior]
cantidad_iteraciones = [0]
verificacion =verificar(intervalo)
xrs = []
errores_porcentuales = []
if (verificacion > 0):
  print("El intervalo no encierra la raiz")
else:
  print("La respuesta con 3 secciones es: ", operacion(intervalo, 3, cantidad_iteraciones, xrs, errores_porcentuales), "+- 0.000001")
  print("Cantidad de iteraciones con 3 secciones: ", cantidad_iteraciones, "\n")
  for j in range (0, cantidad_iteraciones[0]-1):
    if (errores_porcentuales[j+1] != 0):
      coeficiente_convergencia = round((errores_porcentuales[j]/errores_porcentuales[j+1]), 6)  
      print("Coefiente de convergencia en el intervalo ", j+1, " es: ", coeficiente_convergencia)
    else:
      print("Coefiente de convergencia en el intervalo ", j+1, " es: 0.0")
  cantidad_iteraciones = [0]
  xrs = []
  errores_porcentuales = []
  print("\n\n\n\nLa respuesta con 4 secciones es: ", operacion(intervalo, 4, cantidad_iteraciones, xrs, errores_porcentuales), "+- 0.000001")
  print("Cantidad de iteraciones con 4 secciones: ", cantidad_iteraciones, "\n")
  for j in range (0, cantidad_iteraciones[0]-1):
    if (errores_porcentuales[j+1] != 0):
      coeficiente_convergencia = round((errores_porcentuales[j]/errores_porcentuales[j+1]), 6)  
      print("Coefiente de convergencia en el intervalo ", j+1, " es: ", coeficiente_convergencia)
    else:
      print("Coefiente de convergencia en el intervalo ", j+1, " es: 0.0")
