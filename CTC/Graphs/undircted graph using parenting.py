"""
DFS for undirected graph
"""

class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = [[] for i in range(v)]
        #-1: not visited; 0: visting but not completed; 1: completed
        self.visited = [-1]*v
        self.par = [-1]*v


    def addNode(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def DFS(self):
        for i in range(len(self.graph)):
            if self.visited[i] == -1:
                self.visit(i)
        return

    def visit(self, i):
        if self.visited[i] == -1:
            self.visited[i] = 0
            for u in self.graph[i]:
                if self.visited[u] == -1 and self.par[i] != u:
                    self.par[u] = i
                    self.visit(u)
            self.visited[i] = 1
            print(i)
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

    print("DFS: for undirected graph:")
    G.DFS()
