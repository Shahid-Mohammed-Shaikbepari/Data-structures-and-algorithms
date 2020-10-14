def reverse_words(arr):
    if len(arr) < 1:
        return []

    def mirrorRev(arr, start, end):
        while start <= end:
            arr[start], arr[end] = arr[end], arr[start]
            start, end = start + 1, end - 1

    h, t = 0, len(arr) - 1
    mirrorRev(arr, h, t)
    print(arr)
    wordStart = None
    for i in range(0, len(arr)):
        if arr[i] == " " and wordStart != None:
            mirrorRev(arr, wordStart, i - 1)
            wordStart = None
        elif i == len(arr) - 1:
            mirrorRev(arr, wordStart, len(arr) - 1)
        elif wordStart == None:
            wordStart = i

    return arr


arr = ['p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
       'm', 'a', 'k', 'e', 's', '  ',
       'p', 'r', 'a', 'c', 't', 'i', 'c', 'e']

print(reverse_words(arr))