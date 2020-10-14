from math import trunc
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        left = 0
        right = dividend
        while left < right:
            mid = float(left + right)/2
            if mid*divisor ==  dividend:
                return trunc(mid)
            elif mid*divisor <  dividend:
                left = mid
            else:
                right = mid
sol = Solution()
print(sol.divide(-7, 3))