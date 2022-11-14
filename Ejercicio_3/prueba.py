import time
import py_ejercicio_3
import cy_ejercicio_3
import random

txt = ["Ejercicio3_parte1.csv","Ejercicio3_parte2.csv","Ejercicio3_parte3.csv"]
tiempo = [10000,100000,1000000]


#Se crea un formato para la impresion sobre el fichero
formato_datos = "{},{},{}\n"

for j in range(3):

	with open(txt[j],"a") as archivo:
			archivo.write("Python,Cython,Aceleracion\n")
			
	for k in range(30):

		#en python
		
		inicioPy = time.time()
		mi_trayectoria_py = py_ejercicio_3.Trayectoria()
		mi_trayectoria_py.velocidad = 50
		mi_trayectoria_py.angulo = 30
	
		mi_trayectoria_py.calcular(mi_trayectoria_py ,tiempo[j])
		total_py = time.time() - inicioPy
		
		#en cython
		
		inicioCy = time.time()
		mi_trayectoria_cy = cy_ejercicio_3.Trayectoria()
		mi_trayectoria_cy.velocidad = 50
		mi_trayectoria_cy.angulo = 30
	
		mi_trayectoria_cy.calcular(mi_trayectoria_cy ,tiempo[j])
		total_cy = time.time() - inicioCy
		
		aceleracion = total_py/total_cy
		
		with open(txt[j],"a") as archivo:
			archivo.write(formato_datos.format(total_py,total_cy,aceleracion))
	

