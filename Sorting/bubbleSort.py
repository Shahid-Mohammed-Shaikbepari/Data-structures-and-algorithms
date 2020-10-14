class BubbleSort:

    def BubbleSort(self, arr):
        if not len(arr):
            return None

        for iterations in range(len(arr)):
            isSwap = False
            for i in range(0 , (len(arr)-1)-iterations):
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    isSwap = True
            if not isSwap:
                break
        print(arr)

if __name__ ==  "__main__":
    bs = BubbleSort()
    import numpy as np
    a = np.arange(5)

    b = a[::-1]

    print(b)
    bs.BubbleSort(b)
