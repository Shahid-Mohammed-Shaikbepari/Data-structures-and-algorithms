def question(arr, target):
    res= set()
    if target == 0 or len(arr) < 1:
        return []
    arr.sort()
    def backtrack(i, temp):
        if i == len(arr):
            return
        for j in range(i, len(arr)):
            sumCal = sum(temp)
            while sumCal+ arr[j] <= target:
                temp.append(arr[j])
                if sumCal + arr[j] == target:
                    res.add(tuple(sorted(temp)))
                    if temp:
                        temp.pop(-1)
                    if temp:
                        temp.pop(-1)
                    backtrack(i+1, temp)

                sumCal += arr[j]
            if temp:
                n = temp.pop(-1)
                sumCal -= n


    backtrack(0, [])
    return [list(tup) for tup in res]

A = [2,3, 6, 7]
B = [2, 3, 5]
C= []
D = [3]
E = [ 4, 2, 2]
print(question(E, 8))


