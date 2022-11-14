"""
Este programa evalua la sumatoria desde a=0 hasta b con f(a) = 1/(x+a*y)
"""
class Funcion(object):

	def __init__(self):
		self.x = 0.1
		self.y = 0.1
		
	def operacion(self,funcion,i):
	
		return (1/(funcion.x*i+funcion.y))
		
	def sumatoria(self,funcion,a):
		resultado = 0
		for i in range (a):
			resultado += self.operacion(funcion,i)
		
		

