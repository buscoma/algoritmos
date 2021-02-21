class Fila:
	def __init__(self):
		self.primero = None
	
	def agregar(self, valor:int):
		class Nodo:
			def __init__(self, valor):
				self.valor = valor
				self.siguiente = None
		actual = self.primero
		anterior = None
		nuevo = Nodo(valor)
		while actual != None:
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