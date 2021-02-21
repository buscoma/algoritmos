from . import Grafo

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
