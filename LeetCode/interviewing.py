import heapq, collections
def leastUniqueNum(arr, k):
    if len(arr) < 1:
        return 0
    count = collections.Counter(arr)
    heap = []
    for e in count.keys():
        heapq.heappush(heap, (count.get(e), e))
    while k > 0:
        freq, e = heapq.heappop(heap)
        if freq <= k:
            k -= freq
            del count[e]
        else:
            break
    return len(count)


arr = [ 4]
k = 1

print(leastUniqueNum(arr, k))