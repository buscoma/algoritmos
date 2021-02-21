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

from .GrafoListaAdyacentes import GrafoListaAdyacentes
from . GrafoMatrizAdyacencia import GrafoMatrizAdyacencia