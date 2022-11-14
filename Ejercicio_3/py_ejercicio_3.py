from numpy import sin,cos

class Trayectoria(object):
	
	def __init__(self):
		self.gravedad = 9.81
		self.velocidad = 0.1
		self.angulo = 0.1
		self.x = 0.1
		self.y = 0.1
		self.vx = 0.1
		self.vy = 0.1
		
		
	def paso(self,trayectoria,iteracion):
	
		trayectoria.x = trayectoria.velocidad *iteracion*cos(trayectoria.angulo)
		trayectoria.vx = trayectoria.velocidad *cos(trayectoria.angulo)
		
		trayectoria.y = trayectoria.velocidad *iteracion*sin(trayectoria.angulo)-((trayectoria.gravedad/2)*pow(iteracion,2))
		trayectoria.vy = trayectoria.velocidad *sin(trayectoria.angulo)-trayectoria.gravedad*iteracion
		
		
	def calcular(self,trayectoria,num_iter):
	
		for i in range(num_iter):
			self.paso(trayectoria,i)

	
