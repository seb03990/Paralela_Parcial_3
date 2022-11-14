#cython: language_level=3

cdef class Palabra(object):

	cdef public str pal
		
	def __init__(self):
		self.pal = "hola"
  
	def contar(self,Palabra palabra,str letra):
		cdef int contador = 0
		cdef int i = 0
		for i in range(len(palabra.pal)):
			if palabra.pal[i]== letra:
				contador += 1
