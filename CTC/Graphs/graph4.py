"""
BFS for undirected graphs
"""
class Graph:
    def __init__(self, v):
        self.v = v
        self.graph= [[] for i in range(v)]

    def addNode(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def BFS(self, s):
        # -1: not visited; 0: added to Q but not yet visited; 1: visited
        visited = [-1]*self.v
        Q = []
        Q.append(s)

        while Q:
            u = Q.pop(0)
            visited[u] = 1
            print(u)
            for v in self.graph[u]:
                if visited[v] == -1:
                    Q.append(v)
                    visited[v] = 0
        return


if __name__ == "__main__":
    G = Graph(5)
    G.addNode(0, 1)
    G.addNode(0, 4)
    G.addNode(4, 1)
    G.addNode(2, 1)
    G.addNode(2, 4)
    G.addNode(2, 3)
    G.addNode(4, 3)

    print("BFS: for undirected graph:")
    G.BFS(0)
