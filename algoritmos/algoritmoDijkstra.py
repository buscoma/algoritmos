from clases import Grafo
import sys

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

def dijkstra(grafo: Grafo, inicio: int):
	D = dict() # Distancias
	P = dict() # Predecesores
	for vertice in grafo.vertices():
		D[vertice] = sys.maxsize
		P[vertice] = None
	D[inicio] = 0 # Al tratarse del vertice de inicio la distancia al mismo es 0
	S = list() # Arreglo vertices visitados
	Q = ColaConPrioridad()
	Q.agregar(inicio, 0)
	while not Q.esVacia():
		u = Q.recuperar() # Extrae el vertice de coste menor de los que quede por visitar
		S += [u]
		agregarAdyacentes(Q, grafo, u, S)
		for verticeAdyacente in grafo.adyacentes(u):
			if verticeAdyacente not in S: # Si el vertice no se encuentra en los definitivos
				if D[verticeAdyacente] > D[u] + grafo.pesoArista(u, verticeAdyacente): # Me fijo que tenga una distancia menor a la que tenga
					D[verticeAdyacente] = D[u] + grafo.pesoArista(u, verticeAdyacente) # Actualizo
				if not P[verticeAdyacente]:
					P[verticeAdyacente] = u # Marco a u como padre del vertice adyacente
	return P, D

def agregarAdyacentes(Q: ColaConPrioridad, grafo: Grafo, vertice: int, S: list):
	adyacentes = grafo.adyacentes(vertice)
	for verticeAdyacente in adyacentes:
		if verticeAdyacente not in S:
			peso = grafo.pesoArista(vertice, verticeAdyacente)
			Q.agregar(verticeAdyacente, peso)
