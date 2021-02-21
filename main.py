#!python3

from clases.grafo import GrafoListaAdyacentes, GrafoMatrizAdyacencia
from algoritmos import dfs, dfs_forest, bfs, bfs_forest, dijkstra
from auxiliares import mostrar, popular, mostrarDijkstra

if __name__ ==  "__main__":
	g1 = GrafoListaAdyacentes(dirigido=True)
	popular(g1)
	print("")
	print("Buscando solo por DFS:")
	resultado = dfs(g1, 1) # Tomo uno como inicial
	mostrar(resultado)
	print("")
	print("Buscando por DFS Forest:")
	resultado = dfs_forest(g1)
	mostrar(resultado)
	print("")
	print("Buscando solo por BFS:")
	resultado = bfs(g1, 1) # Tomo uno como inicial
	mostrar(resultado)
	print("")
	print("Buscando por BFS Forest:")
	resultado = bfs_forest(g1)
	mostrar(resultado)
	print("")
	print("Recorriendo por Dijkstra para saber el camino mas corto:")
	g2 = GrafoMatrizAdyacencia(dirigido=False)
	popular(g2)
	predecesores, distancias = dijkstra(g2, 1)
	mostrarDijkstra(predecesores, distancias)
