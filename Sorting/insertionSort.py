class sorting:
    def InsertionSort(self, nums):
        for index in range(1,len(nums)):
            x = nums[index]
            j = index - 1
            while j >= 0 and  nums[j] > x:
                nums[j+1] = nums[j]
                j -=1

            nums[j + 1] = x

        return nums
if __name__ == "__main__":
    obj = sorting()
    import numpy as np

    a = np.arange(5)

    b = a[::-1]
    print(b)
    b = obj.InsertionSort([])
    print(b)