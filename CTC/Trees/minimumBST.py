"""
the following code is to create a BST from sort Array
"""

class Node:
    def __int__(self, v):
        self.val = v
        self.left = None
        self.right = None

class BST:

    def MinimumBST(self, arr, left, right):
        if left > right:
            return None
        mid = int((left + right)/2)
        node = Node()
        node.val = arr[mid]
        node.left = self.MinimumBST(arr, left, mid-1)
        node.right = self.MinimumBST(arr, mid+1, right)
        return node

    def traverse(self, Node):
        Q = []
        # visited = [-1]*len(arr)
        Q.append(Node)
        while Q:
            u = Q.pop(0)
            if u != None:
                print(u.val, end=" ")
                # visited[u] = 1
                Q.append(u.left)
                Q.append(u.right)







if __name__ == "__main__":
    arr = [0,1,2,3,4,5,6,7,8,9,10]
    bst = BST()
    node = bst.MinimumBST(arr, 0, len(arr)-1)
    bst.traverse(node)



