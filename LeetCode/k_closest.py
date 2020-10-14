from queue import PriorityQueue
from math import sqrt

class Solution:
    def kClosest(self, points, K) :
        if K * len(points) * len(points[0]) < 1:
            return []

        def getDist(point):
            return (sqrt(point[0] ** 2 + point[1] ** 2))

        que = PriorityQueue()
        for point in points:
            d = getDist(point)
            que.put((d, point))
        return [que.get()[1] for _ in range(K)]

sol = Solution()
lis = sol.kClosest([[1,3],[-2,2]], 1)
print(lis)