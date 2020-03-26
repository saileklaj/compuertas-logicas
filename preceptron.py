"""
plt.plot(gradpesos[:,0],'K')
plt.plot(gradpesos[:,1],'X')
plt.plot(gradpesos[:,2],'Y')
plt.show()"""
from keras.models import Sequential
from keras.layers import Dense

class Preceptron:
	
	def __init__(self,entradas,salida):
		self.entradas=entradas
		self.salida=salida
		self.model=Sequential()

	def perceptron(self):
		
		self.model.add(Dense(16,input_dim=2, activation='relu'))
		self.model.add(Dense(1,activation='sigmoid'))
		self.model.compile(loss='mean_squared_error',
				optimizer='adam',
				metrics=['binary_accuracy'])
		self.model.fit(self.entradas,self.salida,epochs=1000)
		scores= self.model.evaluate(self.entradas,self.salida)
		print(self.model.metrics_names[1],scores[1]*1000)
		print(self.model.predict(self.entradas).round())
		input()
