# Paralela_Parcial_3

Bienvenido usuario.

El proposito de este repositorio es realizar una comparativa en cuanto a tiempo de ejecucion entre python y cython, por lo que se encontraran 3 ejercicios para realizar dicha actividad.

Cada ejercicio cuenta con los elementos necesarios para ser ejecutados desde cualquier otro computador, los elementos son:

* py_ejercicio.py (ejercicio en python)
* cy_ejercicio.pyx (ejercicio en cython)
* setup (necesario para importar el programa de cython a python)
* Makefile (ejecuta el setup automaticamente, para ejecutar en consola ingresar 'make all')
* prueba.py (Programa donde se realiza la experimentacion con los 2 ejercicios)

***Datos a tener en cuenta***

* Para ejecutar prueba.py ingrese en la terminal 'pthon3 prueba.py' (tener en cuenta que se debe tener instalado python) 
* Al ejecutar prueba.py se generaran 3 archivos de texto con los tiempos de ejecucion, cada archivo represeta un conjunto de datos experimentales
* Si se desea realizar la experimentacion con otro conjunto de datos experimental, realice los cambios necesarios en el archivo prueba.py
* En el repositorio tambien encontrara otras carpetas tituladas 'solucion_ejercicio_n', estas carpetas contienen los datos resultantes de la  primera experimentacion, fueron separadas de su respectivo problema para que no fueran descargadas con los demas archivos.
.  

***Descripcion de cada ejercicio***

* Ejercicio 1: Este programa evalua la sumatoria desde a=0 hasta un numero b con f(a) = 1/(x+a*y)
* Ejercicio 2: Genera una palabra con letras aleatorias y cuenta cuantas veces aparece determinada letra en la palabra
* Ejercicio 3: Simula el movimiento de un cuerpo en caida libre con movimiento parabolico en un lapso de tiempo


***Resultados de la actividad***

A continuacion, link del analisis de los ejercicios en colab: https://colab.research.google.com/drive/1uVZ5Qu-qWf3ejejmGnunKoElAdSAXAkb?usp=sharing
