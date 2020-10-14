"""
BFS for directed, connected graph
"""
from collections import defaultdict
class Graph:
    def __init__(self):
        # self.v = v
        # self.graph = [[] for i in range(v)]
        # self.visited = [False]*v
        self.graph = defaultdict(list)

    def addNode(self, u, v):
        self.graph[u].append(v)
        #uncomment this for undirected graphs
        # self.graph[v].append(u)
    def BFS(self, s):
        visited = [False]*len(self.graph)
        Q = []
        Q.append(s)
        visited[s] = True
        while Q:
            u = Q.pop(0)
            print(u)
            for v in self.graph[u]:
                if visited[v] == False:
                    Q.append(v)
                    visited[v] = True


if __name__ == "__main__":
    G1 = Graph()
    G1.addNode(0, 3)
    G1.addNode(1, 4)
    G1.addNode(1, 2)
    G1.addNode(3, 2)
    G1.addNode(4, 3)
    G1.addNode(2, 0)

    print("BFS:")

    G1.BFS(0)
