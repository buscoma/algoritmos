from clases.grafo import Grafo

marca = dict()

def dfs(grafo:Grafo, origen:int):
		padres = dict({origen: None})
		marca[origen] = "Gris"
		for vertice in grafo.adyacentes(origen):
				if marca.get(vertice) == "Blanco" or not marca.get(vertice): # Es decir es Blanco
						padres.update(dfs(grafo, vertice))
						padres[vertice] = origen
		marca[origen] = "Negro"
		return padres

def dfs_forest(grafo:Grafo, inicio:int = None):
		marca.clear()
		vertices = grafo.vertices()
		marca.update({v: "Blanco" for v in vertices})
		padresDFSResult = dict()
		aux = 0
		while aux < len(vertices):
			if marca.get(vertices[aux]) not in ("Negro", "Gris"):
				padresDFSResult.update(dfs(grafo, vertices[aux]))
			aux+=1
		return padresDFSResult
		