class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = [[] for i in range(v)]
        self.visited = [-1]*v
        self.isFound = False

    def addNode(self, u, v):
        self.graph[u].append(v)
        #uncomment this for undirected graphs
        # self.graph[v].append(u)

    def visit(self, node, target):
        if self.isFound:
            return
        if self.visited[node] != -1:
            return
        else:
            self.visited[node] = 0
            if node == target:
                self.isFound = True
                return
            for u in self.graph[node]:
                if self.visited[u] == -1:
                    self.visit(u, target)
            self.visited[node] = 1
        return

if __name__ == "__main__":
   G1 = Graph(5)
   G1.addNode(0,3)
   G1.addNode(1, 4)
   G1.addNode(1, 2)
   G1.addNode(3, 2)
   G1.addNode(4, 3)
   G1.addNode(2, 0)

   G1.visit(0, 4)
   if G1.isFound == True:
       print("yes there's a route")
   else:
       print("no route detected")