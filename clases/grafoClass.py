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
		Precondición: El vértice debe existir previamente en el grafo
		"""
		pass
	def vertices(self) -> list:
		"""
		Descripción: Devuelve una lista con los vértices del grafo
		"""
		pass
	def agregarArista(self, valorVerticeOrigen:int, valorVerticeDestino:int, peso:int) -> None:
		"""
		Descripción: Agrega una arista entre ambos vértices
		Precondición: Ambos vértices deben existir y la arista no debe existir
		"""
		pass
	def eliminarArista(self, valorVerticeOrigen:int, valorVerticeDestino:int) -> None:
		"""
		Descripción: Elimina la arista entre ambos vértices
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
		Descripción: Valida la existencia de un vértice en el grafo
		"""
		pass
	def adyacentes(self, valorVertice:int) -> list:
		"""
		Descripción: Devuelve una lista con los vértices adyacentes al vértice dado
		Precondición: El vértice debe existir en el grafo
		"""
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
				self.eliminarArista(verticeAuxiliar.valor, actualVertice.valor)
			verticeAuxiliar = verticeAuxiliar.siguienteVertice
		if not anteriorVertice:
			self.primerVertice = self.primerVertice.siguienteVertice
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
			if not anteriorArista:
				verticeDestino.primerArista = verticeDestino.primerArista.siguienteArista
			else:
				anteriorArista.siguienteArista = actualArista.siguienteArista
		actualArista, anteriorArista = self.__buscarArista(verticeOrigen, verticeDestino)
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
	def adyacentes(self, valorVertice):
		adyacentes = list()
		arista = self.__buscarVertice(valorVertice)[0].primerArista
		while arista:
			adyacentes.append(arista.verticeDestino.valor)
			arista = arista.siguienteArista
		return adyacentes
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
		for otroVertice in self.vertices:
			if self.existeArista(valor, otroVertice):
				self.eliminarArista(valor, otroVertice)
			elif self.existeArista(otroVertice, valor):
				self.eliminarArista(otroVertice, valor)
		self.vertices.remove(valor)
	def vertices(self):
		return self.vertices
	def agregarArista(self, valorVerticeOrigen, valorVerticeDestino, peso):
		if not self.dirigido:
			self.aristas.append((valorVerticeDestino, valorVerticeOrigen))
			self.matriz.update({(valorVerticeDestino, valorVerticeOrigen): peso})
		self.aristas.append((valorVerticeOrigen, valorVerticeDestino))
		self.matriz.update({(valorVerticeOrigen, valorVerticeDestino): peso})
	def eliminarArista(self, valorVerticeOrigen, valorVerticeDestino):
		if not self.dirigido:
			self.matriz.update({(valorVerticeDestino, valorVerticeOrigen): 0})
			self.aristas.remove((valorVerticeDestino, valorVerticeOrigen))
			del self.matriz[(valorVerticeDestino, valorVerticeOrigen)]
		self.matriz.update({(valorVerticeOrigen, valorVerticeDestino): 0})
		self.aristas.remove((valorVerticeOrigen, valorVerticeDestino))
		del self.matriz[(valorVerticeOrigen, valorVerticeDestino)]
	def existeArista(self, valorVerticeOrigen, valorVerticeDestino):
		return (valorVerticeOrigen, valorVerticeDestino) in self.aristas
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
	def adyacentes(self, valorVertice):
		adyacentes = list()
		for otroVertice in [v for v in self.vertices if v != valorVertice]:
			if not self.dirigido and (otroVertice, valorVertice) in self.aristas:
				adyacentes.append(otroVertice)
			elif (valorVertice, otroVertice) in self.aristas:
				adyacentes.append(otroVertice)
		return list(adyacentes)
		