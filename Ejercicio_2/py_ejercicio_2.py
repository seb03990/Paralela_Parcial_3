class Palabra(object):

	def __init__(self):
 		self.pal = "buen dia"
    	
	def contar(self,palabra,letra):
		contador = 0
		for i in range(len(palabra.pal)):
			if palabra.pal[i]== letra:
				contador += 1
