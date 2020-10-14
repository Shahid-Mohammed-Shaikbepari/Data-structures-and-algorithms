from collections import deque
class ListNode:
    def __init__(self, val, left=None, right=None):
        self.val= val
        self.left = left
        self.right = right

def mirrorImage( root):
    if not root:
        return None
    node = ListNode(root.val)
    node.left = mirrorImage(root.right)
    node.right = mirrorImage(root.left)
    return node
def mirrorImageNoSpace(root):
    if not root:
        return None
    left = root.left
    right = root.right
    root.left = right
    root.right = left
    mirrorImageNoSpace(root.left)
    mirrorImageNoSpace(root.right)
    return root


def printBST(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        temp = []
        for _ in range(len(queue)):
            node = queue.popleft()
            temp.append(node.val)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        while temp:
            print(temp.pop(), end=" ")
        print("\n")
    return



node1 = ListNode(1)
node4 = ListNode(4)
node7 = ListNode(7)
node6 = ListNode(6, node4, node7)
node13 = ListNode(13)
node14 = ListNode(14, node13)
node10 = ListNode(10, None, node14)
node3 = ListNode(3, node1, node6)
node8 = ListNode(8, node3, node10)


printBST(node8)

root = mirrorImageNoSpace(node8)

printBST(root)

