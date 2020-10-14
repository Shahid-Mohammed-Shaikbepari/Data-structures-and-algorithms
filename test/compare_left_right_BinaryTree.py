def solution(arr):
    if len(arr) < 1:
        return ""
    node = createBT(arr)

    leftSum = getSum(node.left, 0)
    rightSum = getSum(node.right, 0)
    if leftSum > rightSum:
        return "Left"
    elif leftSum < rightSum:
        return "Right"
    else:
        return ""

def printBT(node):
    stack = [node]
    while stack:
        root = stack.pop()
        print(root.val)

        stack.append(root.left)

def getSum(node, sum):
    if not node:
        return sum
    sum += node.val
    sum = getSum(node.left, sum)
    sum = getSum(node.right, sum)
    return sum


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

def createBT(arr):
    i = 1

    def create(node, stack):
        nonlocal i
        if not node or i >= len(arr):
            return
        if i < len(arr) and arr[i] != -1:
            node.left = Node(arr[i])
            stack.append(node.left)
        i += 1
        if i < len(arr) and arr[i] != -1:
            node.right = Node(arr[i])
            stack.append(node.right)
        i += 1

    head = Node(arr[0])
    stack = deque()
    stack.append(head)
    while stack:
        node = stack.popleft()
        create(node, stack)
    return head

arr =  [1, 1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
print(solution(arr))