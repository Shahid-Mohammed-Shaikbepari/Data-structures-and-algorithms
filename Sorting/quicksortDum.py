def quickS(arr, left, right):
    if left >= right:
        return
    mid = int((left + right)/2)
    pivot = arr[mid]
    l = left
    r = right
    while l <= r:
        while arr[l] < pivot:
            l += 1
        while arr[r] >= pivot:
            r -= 1
        if l <= r:
            arr[l], arr[r] = arr[r], arr[l]

    quickS(arr, left, mid-1)
    quickS( arr, mid+1, right)


a = [6, 7, 8, 5, 4, 3, 2, 1,0]
quickS(a, 0, 8)
print(a)
