"""
DFS for directed graph, connected graph
"""

class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = [[] for i in range(v)]
        self.visited = [-1]*v

    def addNode(self, u, v):
        self.graph[u].append(v)
        #uncomment this for undirected graphs
        # self.graph[v].append(u)

    def visit(self, node):
        if self.visited[node] != -1:
            return
        else:
            self.visited[node] = 0
            for u in self.graph[node]:
                if self.visited[u] == -1:
                    self.visit(u)
            self.visited[node] = 1
            print(node)
        return

if __name__ == "__main__":
   G1 = Graph(5)
   G1.addNode(0,3)
   G1.addNode(1, 4)
   G1.addNode(1, 2)
   G1.addNode(3, 2)
   G1.addNode(4, 3)
   G1.addNode(2, 0)

   print("DFS list: ")
   for u in range(G1.v):
       if G1.visited[u] == -1:
           G1.visit(u)
