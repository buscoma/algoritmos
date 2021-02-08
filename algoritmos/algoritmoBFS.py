from clases import Grafo

marca = dict()

def bfs(grafo:Grafo, origen:int):
	marca[origen] = "Gris"
	padres = dict({origen: None})
	fila = Fila()
	fila.agregar(origen)
	while not fila.esVacia():
		actual = fila.recuperar()
		for ady in grafo.adyacentes(actual):
			if marca.get(ady) == "Blanco" or not marca.get(ady): # Es decir es Blanco
				marca[ady] = "Gris"
				padres[ady] = actual
				fila.agregar(ady)
		marca[actual] = "Negro"
	return padres

def bfs_forest(grafo:Grafo):
	marca.clear()
	vertices = grafo.vertices()
	marca.update({v: "Blanco" for v in vertices})
	padresBFSResult = dict()
	aux = 0
	while aux < len(vertices):
		if marca.get(vertices[aux]) not in ("Negro", "Gris"):
			padresBFSResult.update(bfs(grafo, vertices[aux]))
		aux+=1
	return padresBFSResult

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