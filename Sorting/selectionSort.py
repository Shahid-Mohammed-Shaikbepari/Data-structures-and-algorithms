class Selection:
    def SelectionSort(self, arr):
        if not len(arr):
            return None
        for j in range(len(arr)):
            smallest = j
            for i in range(j+1, len(arr)):
                if arr[i] < arr[smallest]:
                    smallest = i
            arr[j], arr[smallest] = arr[smallest], arr[j]
        print(arr)


if __name__ =="__main__":
    import numpy as np

    a = np.arange(5)

    b = a[::-1]

    print(b)
    ss = Selection()
    ss.SelectionSort(b)