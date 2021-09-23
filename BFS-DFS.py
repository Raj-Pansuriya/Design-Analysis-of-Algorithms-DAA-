from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph=defaultdict(list)
	
	def addEdge(self,u,v):
		self.graph[u].append(v)

	def DFS_visit(self,v,visited):
		visited.add(v)
		print(v,end=" ")
		
		#recuring for all the adjacent vertices
		for neighbour in self.graph[v]:
			if neighbour not in visited:
				self.DFS_visit(neighbour,visited)

	def DFS(self):
		visited=set()
		for vertex in self.graph:
			if vertex not in visited:
				self.DFS_visit(vertex,visited)

	def BFS(self,root):
		queue=[root]
		visited=[root]
		print(root,end=" ")
		while len(queue)!=0:
			explore=queue[0]
			if explore in self.graph:
				for vertex in self.graph[explore]:
					if vertex not in visited and vertex not in queue:
						queue.append(vertex)
						visited.append(vertex)
						print(vertex, end=" ")
			else:
				visited.append(explore)
				print(explore,end=" ")
			queue.pop(0)


g=Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)
print("DFS traversal of the graph starting from vertex '0' is :",end=" ")
g.DFS()
print("\nBFS traversal of the graph starting from vertex '2' is :",end=" ")
g.BFS(2)

