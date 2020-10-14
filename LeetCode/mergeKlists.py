import heapq
class ListNode:
    def __init__(self, val):
        self.val= val
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        q = []
        for node in lists:
            if node:
                heapq.heappush(q, (node.val,node))
        while q:
            val, node = heapq.heappop(q)
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                heapq.heappush(q,(node.val, node))
        return head.next

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
lists = []
lists.append(l3)
lists.append(l1)
lists.append(l2)
sol = Solution()
node = sol.mergeKLists(lists)
while node:
    print(node.val)
    node = node.next
