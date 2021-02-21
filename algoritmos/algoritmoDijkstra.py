from clases.grafo import Grafo
from clases.colaConPrioridad import ColaConPrioridad
import sys

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
