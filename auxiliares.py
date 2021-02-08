from clases import Grafo

def popular(grafo:Grafo):
	for v in range(6,0,-1):
		grafo.agregarVertice(v)
	grafo.agregarArista(1,2,8)
	grafo.agregarArista(1,4,8)
	grafo.agregarArista(2,3,8)
	grafo.agregarArista(2,4,8)
	grafo.agregarArista(2,5,8)
	grafo.agregarArista(3,4,8)
	grafo.agregarArista(4,2,8)
	grafo.agregarArista(5,3,8)
	grafo.agregarArista(5,6,8)
	grafo.agregarArista(1,6,8)
	grafo.agregarArista(6,6,8)

def mostrarDFS(resultado:dict):
	def hijoDe(unPadre):
		for hijo, padre in resultado.items():
			if unPadre == padre:
				return hijo
		return None
	hijos = [h for h in list(resultado.keys()) if resultado.get(h)]
	padres = list(resultado.values())
	padres_origen = list(set([vertice for vertice in padres if vertice not in hijos and vertice]))
	for padre in padres_origen:
		hijosDePadre = [h for h in hijos if resultado[h] == padre]
		print(f"[{padre}] ", end="")
		for hijo in hijosDePadre:
			print(f"==> [{hijo}] ", end="")
			hijo = hijoDe(hijo)
		print("")

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


