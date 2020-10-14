def printcombinations(arr, max, ind):
    for i in range(ind, len(arr)):
        printcombinations(arr, max, ind+1)
        if arr[i] < max:
            arr[i] += 1
arr = [1, 1]
max = 4
printcombinations(arr, max, 0)
