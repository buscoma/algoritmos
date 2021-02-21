from . import Grafo

class GrafoMatrizAdyacencia(Grafo):
	def __init__(self, dirigido:bool = True):
		self.verticesGrafo = list()
		self.aristas = list()
		self.matriz = dict()
		self.dirigido = dirigido
	def agregarVertice(self, valor):
		self.verticesGrafo+=[valor]
	def eliminarVertice(self, valor):
		for otroVertice in self.verticesGrafo:
			if self.existeArista(valor, otroVertice):
				self.eliminarArista(valor, otroVertice)
			elif self.existeArista(otroVertice, valor):
				self.eliminarArista(otroVertice, valor)
		self.verticesGrafo.remove(valor)
	def vertices(self):
		return self.verticesGrafo
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
		for v in self.verticesGrafo:
			print(f"\t[{v}]", end="")
		print("")
		for verticeAuxiliar1 in self.verticesGrafo:
			matriz = f"[{verticeAuxiliar1}]\t"
			for verticeAuxiliar2 in self.verticesGrafo:
				matriz+=f"{self.matriz.get((verticeAuxiliar1, verticeAuxiliar2), 0)}\t"
			print(matriz)
	def pertenece(self, valor):
		return valor in self.verticesGrafo
	def adyacentes(self, valorVertice):
		adyacentes = list()
		for otroVertice in [v for v in self.verticesGrafo if v != valorVertice]:
			if not self.dirigido and (otroVertice, valorVertice) in self.aristas:
				adyacentes.append(otroVertice)
			elif (valorVertice, otroVertice) in self.aristas:
				adyacentes.append(otroVertice)
		return list(adyacentes)
		