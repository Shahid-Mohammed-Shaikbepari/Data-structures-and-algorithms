class sorting:
    def MergeSort(self, nums):
        if len(nums) <= 1:
            return nums
        left = []
        right = []

        for ind, num in enumerate(nums):
            if ind < int(len(nums)/2):
                left.append(num)
            else:
                right.append(num)

        left = self.MergeSort(left)
        right = self.MergeSort(right)

        return self.Merge(left, right)

    def Merge(self, left_ar, right_ar):
        res = []
        left = right = 0
        while left < len(left_ar) and right < len(right_ar):
            if left_ar[left] < right_ar[right]:
                res.append(left_ar[left])
                left +=1
            else:
                res.append(right_ar[right])
                right += 1

        while left < len(left_ar):
            res.append(left_ar[left])
            left += 1

        while right < len(right_ar):
            res.append(right_ar[right])
            right +=1

        return res

if __name__ == "__main__":
    s = sorting()

    import numpy as np

    a = np.arange(5)

    b = a[::-1]
    print(b)
    b = s.MergeSort([])
    print(b)


