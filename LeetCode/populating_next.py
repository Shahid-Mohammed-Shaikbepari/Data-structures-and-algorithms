from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        stack = deque()
        stack.append(root)
        root.next = None
        while stack:
            for _ in range(len(stack)):
                node = stack.popleft()
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            prev = None
            for i in range(len(stack) - 1, -1, -1):
                node = stack[i]
                node.next = prev
                node = prev
        return root
