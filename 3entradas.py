import numpy as np
import preceptron as ptr

class operadores_logicos:

	def operador_and():
		
		entradas=np.array([[0, 0], [0, 1], [1, 0], [1, 1]],"float32")
		salida=np.array([(0),(0),(0),(1)],"float32")
		ptr1=ptr.Preceptron(entradas,salida)
		ptr1.perceptron()
		

	def operador_or():
		
		entradas=np.array([[0, 0], [0, 1], [1, 0], [1, 1]],"float32")
		salida=np.array([(0),(1),(1),(1)],"float32")
		ptr1=ptr.Preceptron(entradas,salida)
		ptr1.perceptron()

	def operador_nand():
		
		entradas=np.array([[0, 0], [0, 1], [1, 0], [1, 1]],"float32")
		salida=np.array([(1),(1),(1),(0)],"float32")
		ptr1=ptr.Preceptron(entradas,salida)
		ptr1.perceptron()

	def operador_nor():
		
		entradas=np.array([[0, 0], [0, 1], [1, 0], [1, 1]],"float32")
		salida=np.array([(1),(0),(0),(0)],"float32")
		ptr1=ptr.Preceptron(entradas,salida)
		ptr1.perceptron()

	def operador_xor():
		
		entradas=np.array([[0, 0], [0, 1], [1, 0], [1, 1]],"float32")
		salida=np.array([(0),(1),(1),(0)],"float32")
		ptr1=ptr.Preceptron(entradas,salida)
		ptr1.perceptron()

	def operador_xnor():

		entradas=np.array([[0, 0], [0, 1], [1, 0], [1, 1]],"float32")
		salida=np.array([(1),(0),(0),(1)],"float32")
		ptr1=ptr.Preceptron(entradas,salida)
		ptr1.perceptron()

operadores_logicos.operador_and()
