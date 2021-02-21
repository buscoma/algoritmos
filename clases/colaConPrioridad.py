class ColaConPrioridad:
	def __init__(self):
		self.primero = None
	
	def agregar(self, valor:int, prioridad:int):
		class Nodo:
			def __init__(self, valor, prioridad):
				self.valor = valor
				self.siguiente = None
				self.prioridad = prioridad
		actual = self.primero
		anterior = None
		nuevo = Nodo(valor, prioridad)
		while actual != None and actual.prioridad < nuevo.prioridad: # Utilizo una cola de prioridad invertida
			anterior = actual
			actual = actual.siguiente
		if not anterior:
			self.primero = nuevo
		else:
			anterior.siguiente = nuevo

	def recuperar(self):
		valor = self.primero.valor
		self.primero = self.primero.siguiente
		return valor

	def esVacia(self):
		return not self.primero

	def pasajeALista(self):
		resultado = list()
		while self.primero:
			resultado.append(self.primero)
		return resultado