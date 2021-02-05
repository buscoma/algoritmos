#!python3
class Grafo:
	"""
	Clase abstracta Grafo // No implementar
	"""
	def agregarVertice(self, valor:int) -> None:
		"""
		Descripción: Agrega vértice al grafo
		Precondición: El valor a ingresar debe ser mayor a 0 y no debe existir ya en el grafo
		"""
		pass
	def eliminarVertice(self, valor:int) -> None:
		"""
		Descripción: Elimina vértice del grafo
		Precondición: El vertice debe existir previamente en el grafo
		"""
		pass
	def vertices(self) -> list:
		"""
		Descripción: Devuelve una lista con los vertices del grafo
		"""
		pass
	def agregarArista(self, valorVerticeOrigen:int, valorVerticeDestino:int, peso:int) -> None:
		"""
		Descripción: Agrega una arista entre ambos vertices
		Precondición: Ambos vértices deben existir y la arista no debe existir
		"""
		pass
	def eliminarArista(self, valorVerticeOrigen:int, valorVerticeDestino:int) -> None:
		"""
		Descripción: Elimina la arista entre ambos vertices
		Precondición: La arista debe existir
		"""
		pass
	def existeArista(self, verticeOrigen:int, verticeDestino:int) -> bool:
		"""
		Descripción: Valida la existencia de la arista en el grafo
		Precondición: Ambos vértices deben existir
		"""
		pass
	def pesoArista(self, verticeOrigen:int, verticeDestino:int) -> int:
		"""
		Descripción: Devuelve el peso de la arista
		Precondición: La arista debe existir
		"""
		pass
	def mostrar(self) -> None:
		"""
		Descripción: Muestra una representación del estado del grafo
		"""
		pass
	def pertenece(self, valor:int) -> bool:
		"""
		Descripción: Valida la existencia de un vertice en el grafo
		"""
		pass
class NodoVertice:
	def __init__(self, valor:int = None, siguienteVertice:'NodoVertice' = None, siguienteArista:'NodoArista' = None):
		self.valor = valor
		self.siguienteVertice = siguienteVertice
		self.primerArista = siguienteArista

class NodoArista:
	def __init__(self, peso:int = None, verticeDestino:'NodoVertice' = None, siguienteArista:'NodoArista' = None):
		self.peso = peso
		self.verticeDestino = verticeDestino
		self.siguienteArista = siguienteArista

class GrafoListaAdyacentes(Grafo):
	def __init__(self, dirigido:bool = True):
		self.primerVertice = None
		self.dirigido = dirigido
	def agregarVertice(self, valor):
		nuevoVertice = NodoVertice(valor=valor)
		if not self.primerVertice:
			self.primerVertice = nuevoVertice
		else:
			nuevoVertice.siguienteVertice = self.primerVertice
			self.primerVertice = nuevoVertice
	def eliminarVertice(self, valor):
		actualVertice, anteriorVertice = self.__buscarVertice(valor)
		verticeAuxiliar = self.primerVertice
		while verticeAuxiliar != None:
			actualArista, _ = self.__buscarArista(verticeAuxiliar, actualVertice)
			if actualArista:
				if not self.dirigido:
					self.eliminarArista(actualVertice.valor, verticeAuxiliar.valor)	
				self.eliminarArista(verticeAuxiliar.valor, actualVertice.valor)
			verticeAuxiliar = verticeAuxiliar.siguienteVertice
		if not anteriorVertice:
			primerVertice = primerVertice.siguienteVertice
		else:
			anteriorVertice.siguienteVertice = actualVertice.siguienteVertice
	def vertices(self):
		vertices = list()
		actualVertice = self.primerVertice
		while actualVertice:
			vertices.append(actualVertice.valor)
			actualVertice = actualVertice.siguienteVertice
		return vertices
	def agregarArista(self, valorVerticeOrigen, valorVerticeDestino, peso):
		verticeOrigen, _ = self.__buscarVertice(valorVerticeOrigen)
		verticeDestino, _ = self.__buscarVertice(valorVerticeDestino)
		nuevaArista = NodoArista(peso=peso, verticeDestino=verticeDestino, siguienteArista=verticeOrigen.primerArista)
		verticeOrigen.primerArista = nuevaArista
		if not self.dirigido:
			nuevaArista = NodoArista(peso=peso, verticeDestino=verticeOrigen, siguienteArista=verticeDestino.primerArista)
			verticeDestino.primerArista = nuevaArista
	def eliminarArista(self, valorVerticeOrigen, valorVerticeDestino):
		verticeOrigen, _ = self.__buscarVertice(valorVerticeOrigen)
		verticeDestino, _ = self.__buscarVertice(valorVerticeDestino)

		if not self.dirigido:
			actualArista, anteriorArista = self.__buscarArista(verticeDestino, verticeOrigen)
			if actualArista:
				if not anteriorArista:
					verticeDestino.primerArista = verticeDestino.primerArista.siguienteArista
				else:
					anteriorArista.siguienteArista = actualArista.siguienteArista
		actualArista, anteriorArista = self.__buscarArista(verticeOrigen, verticeDestino)
		if actualArista:
			if not anteriorArista:
				verticeOrigen.primerArista = verticeOrigen.primerArista.siguienteArista
			else:
				anteriorArista.siguienteArista = actualArista.siguienteArista
	def existeArista(self, verticeOrigen, verticeDestino):
		verticeOrigen, _ = self.__buscarVertice(verticeOrigen)
		verticeDestino, _ = self.__buscarVertice(verticeDestino)
		actualArista, _ = self.__buscarArista(verticeOrigen, verticeDestino)
		return actualArista != None
	def pesoArista(self, verticeOrigen, verticeDestino):
		verticeOrigen, _ = self.__buscarVertice(verticeOrigen)
		verticeDestino, _ = self.__buscarVertice(verticeDestino)
		actualArista, _ = self.__buscarArista(verticeOrigen, verticeDestino)
		return actualArista.peso
	def mostrar(self):
		actualVertice = self.primerVertice
		flecha = ">" if self.dirigido else ""
		while actualVertice:
			print(f"[{actualVertice.valor}]>> ", end="")
			actualArista = actualVertice.primerArista
			while actualArista:
				print(f"--{actualArista.peso}--{flecha}[{actualArista.verticeDestino.valor}] ", end="")
				actualArista = actualArista.siguienteArista
			print("")
			actualVertice = actualVertice.siguienteVertice
	def pertenece(self, valor):
		vertice, _ = self.__buscarVertice(valor)
		return vertice is not None
	def __buscarVertice(self, valor:int):
		# Método privado
		actualVertice = self.primerVertice
		anteriorVertice = None
		while actualVertice and actualVertice.valor != valor:
			anteriorVertice = actualVertice
			actualVertice = actualVertice.siguienteVertice
		return actualVertice, anteriorVertice
	def __buscarArista(self, verticeOrigen:'NodoVertice', verticeDestino:'NodoVertice'):
		# Método privado
		actualArista = verticeOrigen.primerArista
		anteriorArista = None
		while actualArista and actualArista.verticeDestino.valor != verticeDestino.valor:
			anteriorArista = actualArista
			actualArista = anteriorArista.siguienteArista
		return actualArista, anteriorArista

class GrafoMatrizAdyacencia(Grafo):
	def __init__(self, dirigido:bool = True):
		self.vertices = list()
		self.aristas = list()
		self.matriz = dict()
		self.dirigido = dirigido
	def agregarVertice(self, valor):
		self.vertices+=[valor]
	def eliminarVertice(self, valor):
		self.vertices.remove(valor)
		for otroVertice in self.vertices:
			self.eliminarArista(valor, otroVertice) if self.existeArista(valor, otroVertice) else None
			self.eliminarArista(otroVertice, valor) if self.existeArista(otroVertice, valor) else None
	def vertices(self):
		return self.vertices
	def agregarArista(self, valorVerticeOrigen, valorVerticeDestino, peso):
		if (valorVerticeOrigen, valorVerticeDestino) not in self.aristas:
			self.aristas.append((valorVerticeOrigen, valorVerticeDestino))
		if not self.dirigido:
			self.matriz.update({(valorVerticeOrigen, valorVerticeDestino): peso})
			self.matriz.update({(valorVerticeDestino, valorVerticeOrigen): peso})
			if (valorVerticeDestino, valorVerticeOrigen) not in self.aristas:
				self.aristas.append((valorVerticeDestino, valorVerticeOrigen))
		else:
			self.matriz.update({(valorVerticeOrigen, valorVerticeDestino): peso})
	def eliminarArista(self, valorVerticeOrigen, valorVerticeDestino):
		self.aristas.remove((valorVerticeOrigen, valorVerticeDestino))
		del self.matriz[(valorVerticeOrigen, valorVerticeDestino)]
		if not self.dirigido:
			self.aristas.remove((valorVerticeDestino, valorVerticeOrigen))
			del self.matriz[(valorVerticeDestino, valorVerticeOrigen)]
	def existeArista(self, valorVerticeOrigen, valorVerticeDestino):
		return (valorVerticeOrigen, valorVerticeDestino) in self.vertices
	def pesoArista(self, valorVerticeOrigen, valorVerticeDestino):
		return self.matriz.get((valorVerticeOrigen, valorVerticeDestino))
	def mostrar(self):
		for v in self.vertices:
			print(f"\t[{v}]", end="")
		print("")
		for verticeAuxiliar1 in self.vertices:
			matriz = f"[{verticeAuxiliar1}]\t"
			for verticeAuxiliar2 in self.vertices:
				matriz+=f"{self.matriz.get((verticeAuxiliar1, verticeAuxiliar2), 0)}\t"
			print(matriz)
	def pertenece(self, valor):
		return valor in self.vertices

def demo():
	def popular(g):
		g.agregarVertice(1)
		g.agregarVertice(2)
		g.agregarVertice(3)
		g.agregarArista(1,2,5)
		g.agregarArista(2,3,4)
		g.agregarArista(1,3,6)
	g1 = GrafoListaAdyacentes(dirigido = True)
	g2 = GrafoMatrizAdyacencia(dirigido = True)
	g3 = GrafoListaAdyacentes(dirigido = False)
	g4 = GrafoMatrizAdyacencia(dirigido = False)
	popular(g1)
	popular(g2)
	popular(g3)
	popular(g4)
	return g1, g2, g3, g4

if __name__ == "__main__":
	gListaDir, gMatrizDir, gListaNoDir, gMatrizNoDir = demo()
	print("Grafo dirigido con lista de adyacentes:")
	gListaDir.mostrar()
	print("Grafo dirigido con matriz de adyacencia:")
	gMatrizDir.mostrar()
	print("Grafo no dirigido con lista de adyacentes:")
	gListaNoDir.mostrar()
	print("Grafo no dirigido con matriz de adyacencia:")
	gMatrizNoDir.mostrar()

"""
$ python3 grafo.py
Grafo dirigido con lista de adyacentes:
[3]>>
[2]>> --4-->[3]
[1]>> --6-->[3] --5-->[2]
Grafo dirigido con matriz de adyacencia:
        [1]     [2]     [3]
[1]     0       5       6
[2]     0       0       4
[3]     0       0       0
Grafo no dirigido con lista de adyacentes:
[3]>> --6--[1] --4--[2]
[2]>> --4--[3] --5--[1]
[1]>> --6--[3] --5--[2]
Grafo no dirigido con matriz de adyacencia:
        [1]     [2]     [3]
[1]     0       5       6
[2]     5       0       4
[3]     6       4       0
"""