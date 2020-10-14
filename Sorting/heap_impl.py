import heapq
a = []

heapq.heappush(a, 25)
heapq.heappush(a, 0)
heapq.heappush(a, 42)
heapq.heappush(a, 85)
heapq.heappush(a, 12)
print(a)
a.remove(25)
print(a)
while a:
    print(heapq.heappop(a))


