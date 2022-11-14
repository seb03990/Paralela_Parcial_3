#cython: language_level=3

from numpy import sin,cos

cdef class Trayectoria(object):
	
	cdef public double gravedad, velocidad, angulo, x, y, vx, vy
	
	def __init__(self):
		self.gravedad = 9.81
		self.velocidad = 0.1
		self.angulo = 0.1
		self.x = 0.1
		self.y = 0.1
		self.vx = 0.1
		self.vy = 0.1
		
		
	cdef void paso(self,Trayectoria trayectoria, int iteracion):
		trayectoria.x = trayectoria.velocidad *iteracion*cos(trayectoria.angulo)
		trayectoria.vx = trayectoria.velocidad *cos(trayectoria.angulo)
		
		trayectoria.y = trayectoria.velocidad *iteracion*sin(trayectoria.angulo)-((trayectoria.gravedad/2)*pow(iteracion,2))
		trayectoria.vy = trayectoria.velocidad *sin(trayectoria.angulo)-trayectoria.gravedad*iteracion
		
		
	def calcular(self,Trayectoria trayectoria, int num_iter):
		cdef int i = 0
		for i in range(num_iter):
			self.paso(trayectoria,i)
