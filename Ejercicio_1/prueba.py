import time
import py_ejercicio_1
import cy_ejercicio_1

iteraciones = [10000,100000,1000000]
x = [10,200,3000]
y = [10,200,3000]
txt = ["Ejercicio1_parte1.csv","Ejercicio1_parte2.csv","Ejercicio1_parte3.csv"]

#Se crea un formato para la impresion sobre el fichero
formato_datos = "{},{},{}\n"

for j in range(3):

	with open(txt[j],"a") as archivo:
			archivo.write("Python,Cython,Aceleracion\n")
	for i in range(30):

		#en python
		
		inicioPy = time.time()
		mi_funcion_py = py_ejercicio_1.Funcion()
		mi_funcion_py.x = x[j]
		mi_funcion_py.y = y[j]
		mi_funcion_py.sumatoria(mi_funcion_py,iteraciones[j])
		total_py = time.time() - inicioPy
		
		#en cython
		
		inicioCy= time.time()
		mi_funcion_cy = cy_ejercicio_1.Funcion()
		mi_funcion_cy.x = x[j]
		mi_funcion_cy.y = y[j]
		mi_funcion_cy.sumatoria(mi_funcion_cy,iteraciones[j])
		total_cy = time.time() - inicioCy
		
		aceleracion = total_py/total_cy
		
		with open(txt[j],"a") as archivo:
			archivo.write(formato_datos.format(total_py,total_cy,aceleracion))
	

