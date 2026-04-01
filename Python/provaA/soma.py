class Somatoria():
	def __init__(self):
		self._soma = 0
		self._quantosValoresSomados = 0
		self._soma_inversos = 0.0
		self._quantos_inversos_somados = 0
		self._minimo = float("inf")
		self._maximo = float("-inf")
		self._m2 = 0

	@property
	def valor(self):
		return self._soma

	@property
	def quantos(self):
		return self._quantosValoresSomados

	def somar(self, valorASomar):

			
			if valorASomar < self._minimo:
					self._minimo = valorASomar
			if valorASomar >self._maximo:
					self._maximo = valorASomar
			if self._quantosValoresSomados > 0:
				
				delta = valorASomar - (self._soma / self._quantosValoresSomados)
			else:
				delta = valorASomar

			self._quantosValoresSomados += 1
			self._soma += valorASomar
			
			delta2 = valorASomar - (self._soma / self._quantosValoresSomados)
			self._m2 = delta * delta2
			
	@property
	def minimo(self):
		return self._minimo

	@property
	def variancia(self):
		return self._m2


	@property
	def maximo(self):
		return self._maximo


	def variancia(self) -> float:
		if self._quantosValoresSomados >=2:
			return self._m2/(self._quantosValoresSomados -1)
		else:
			return 0

	def somar_inverso(self, x:float)->float:

		if x == 0:
			raise ZeroDivisionError("Para soma do inverso, o valor referido não pode assumir valor 0. ")
		else:
			self._soma_inversos +=1/x
			self._quantos_inversos_somados +=1	


	@property
	def soma_inversos(self):
		return self._soma_inversos
	
	@property
	def media_harmonica(self):
		mediaHarm = self._quantos_inversos_somados/self._soma_inversos
		return mediaHarm




	def mediaAritmetica(self):
		if self._quantosValoresSomados > 0 :
			
			return self._soma / self._quantosValoresSomados

		raise ZeroDivisionError("Não houve valores somados.")
	
