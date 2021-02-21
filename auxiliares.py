from clases.grafo import Grafo

def popular(grafo:Grafo):
	for v in range(6,0,-1):
		grafo.agregarVertice(v)
	grafo.agregarArista(1,2,4)
	grafo.agregarArista(1,4,1)
	grafo.agregarArista(2,3,2)
	grafo.agregarArista(3,4,3)
	grafo.agregarArista(4,2,5)
	grafo.agregarArista(5,3,1)
	grafo.agregarArista(5,6,5)
	grafo.agregarArista(6,6,1)

def mostrar(resultado:dict):
	def printHijos(padre):
		hijosDePadre = [h for h in hijos if resultado[h] == padre]
		if hijosDePadre:
			print(f"<[{padre}]> ⭆", end="")
			for hijo in hijosDePadre:
				print(f" [{hijo}]", end="")
			print("")
			for hijo in hijosDePadre:
				printHijos(hijo)
	hijos = [h for h in list(resultado.keys()) if resultado.get(h)]
	padres = list(resultado.values())
	padres_origen = list(set([vertice for vertice in padres if vertice not in hijos and vertice]))
	for padre in padres_origen:
		printHijos(padre)

def mostrarDijkstra(predecesores, distancias):
	vertices = list(predecesores.keys())
	for vertice in vertices:
		print(f"Distancia a vertice {vertice}: {distancias[vertice]}\tRecorrido: [{vertice}]", end="")
		predecesor = predecesores.get(vertice)
		while predecesor:
			print(f" <-- [{predecesor}]",end="")
			predecesor = predecesores.get(predecesor)
		print("")
