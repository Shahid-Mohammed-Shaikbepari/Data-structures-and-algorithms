def find_duplicates(arr1, arr2):
    if len(arr1) > len(arr2):
        smaller_arr = arr2
        bigger_arr = arr1
    else:
        smaller_arr = arr1
        bigger_arr = arr2

    res = []
    for i in smaller_arr:
        if BS(i, bigger_arr):
            res.append(i)
    return res


def BS(ele, arr):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = int((start + end) / 2)
        if ele == arr[mid]:
            return True
        if ele > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return False

if __name__ == "__main__":
    arr1 =  [1,2,3,5,6,7]
    arr2 =  [3,6,7,8,20]
    res = find_duplicates(arr1, arr2)
    print(res)