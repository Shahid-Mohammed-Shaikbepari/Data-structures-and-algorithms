class Solution:

    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length < 2:
            return None
        res = ""
        for i in range(length, 1, -1):
            res = self.generateSubstrings(i, res, s, length)
            if res != None:
                break
        return res

    def generateSubstrings(self, size, res, s, length):
        substring = ""
        for i in range(0, length - size + 1):
            substring = s[i:size + i]
            if self.isPalindrome(substring, res):
                res = substring
                return res
        return None

    def isPalindrome(self, string, res):
        s = 0
        e = len(string) - 1
        while s < e:
            if string[s] != string[e]:
                return False
            s, e = s + 1, e - 1
        return True


if __name__ == '__main__':
    s = "cbbd"
    sol = Solution()
    res = sol.longestPalindrome(s)
    print(res)