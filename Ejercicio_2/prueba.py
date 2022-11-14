import time
import py_ejercicio_2
import cy_ejercicio_2
import random

txt = ["Ejercicio2_parte1.csv","Ejercicio2_parte2.csv","Ejercicio2_parte3.csv"]
longitud = [10000,100000,1000000]
oraciones = []
letra_buscar='a'

for i in range(3):
	palabra = '' 
	for h in range(longitud[i]):
		palabra += chr(random.randint(ord('a'), ord('z')))
	oraciones.append(palabra)

#Se crea un formato para la impresion sobre el fichero
formato_datos = "{},{},{}\n"

for j in range(3):

	with open(txt[j],"a") as archivo:
			archivo.write("Python,Cython,Aceleracion\n")
			
	for k in range(30):

		#en python
		
		inicioPy = time.time()
		mi_palabra_py = py_ejercicio_2.Palabra()
		mi_palabra_py.pal = oraciones[j]
	
		mi_palabra_py.contar(mi_palabra_py,letra_buscar)
		total_py = time.time() - inicioPy
		
		#en cython
		
		inicioCy = time.time()
		mi_palabra_cy = cy_ejercicio_2.Palabra()
		mi_palabra_cy.pal = oraciones[j]
	
		mi_palabra_cy.contar(mi_palabra_cy,letra_buscar)
		total_cy = time.time() - inicioCy
		
		aceleracion = total_py/total_cy
		
		with open(txt[j],"a") as archivo:
			archivo.write(formato_datos.format(total_py,total_cy,aceleracion))
	

