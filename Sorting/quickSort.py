class QS:
    def quickSort(self, nums, left_index, right_index):
        if left_index >= right_index:
            return
        left, right = left_index, right_index
        mid = int((left + right)/2)
        pivot = nums[mid]

        while left <= right:
            while nums[left] < pivot:
                left += 1
            while nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1

        self.quickSort(nums, left_index, mid-1)
        self.quickSort(nums, mid+1, right_index)



if __name__ == '__main__':
    import numpy as np

    a = np.arange(10)

    b = a[::-1]
    print(b)

    qs = QS()
    qs.quickSort(b, 0, len(b)-1)
    print(b)