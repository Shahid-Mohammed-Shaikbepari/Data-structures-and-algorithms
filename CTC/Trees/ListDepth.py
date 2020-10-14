class Node:
    def __int__(self, v):
        self.val = v
        self.left = None
        self.right = None

def ListDepths(Node):
    res = []
    DFSUtil(res, 0, Node)

def DFSUtil(res, level, node):
    if node == None:
        return
    if len(res) == level:
        l = []
        res.append(l)
    else:
        l = res[level]
    l.append(node)
    DFSUtil(res, level+1, node.left)
    DFSUtil(res, level + 1, node.right)

