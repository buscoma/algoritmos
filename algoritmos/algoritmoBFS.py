from clases.grafo import Grafo
from clases.fila import Fila

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
