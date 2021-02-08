from clases import GrafoListaAdyacentes, GrafoMatrizAdyacencia, Grafo
from algoritmos import dfs, dfs_forest, bfs, bfs_forest
from auxiliares import mostrarDFS, mostrarBFS, popular

if __name__ ==  "__main__":
	gListaDir = GrafoListaAdyacentes(dirigido=True)
	popular(gListaDir)
	print("")
	print("Buscando solo por DFS:")
	resultado = dfs(gListaDir, 1) # Tomo uno como inicial
	mostrarDFS(resultado)
	print("")
	print("Buscando por DFS Forest:")
	resultado = dfs_forest(gListaDir)
	mostrarDFS(resultado)
	print("")
	print("Buscando solo por BFS:")
	resultado = bfs(gListaDir, 1) # Tomo uno como inicial
	mostrarBFS(resultado)
	print("")
	print("Buscando por BFS Forest:")
	resultado = bfs_forest(gListaDir)
	mostrarBFS(resultado)