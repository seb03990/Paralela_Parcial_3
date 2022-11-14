#cython: language_level=3
"""
Este programa evalua la sumatoria desde a=0 hasta b con f(a) = 1/(x+a*y)
"""
cimport cython

cdef class Funcion(object):

	cdef public double x,y	
	
	def __init__(self):
		self.x = 0.1
		self.y = 0.1
		
	@cython.cdivision(True)
	cdef double operacion(self,Funcion funcion, int i):
	
		return (1/(funcion.x*i+funcion.y))
		
	def sumatoria(self,funcion,int a):
	
		cdef double resultado = 0
		cdef int i = 0 
		
		for i in range (a):
			resultado += self.operacion(funcion,i)

		


