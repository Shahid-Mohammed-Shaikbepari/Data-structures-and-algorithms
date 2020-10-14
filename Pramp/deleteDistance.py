def deletion_distance(str1, str2):
    """
    insights
    approach;
    1. compare two chars at a time
    2. if equal continue
    3. if not equal, delete one at char
    4. base case: when we reach end

    test cases:
    1. "" ""
    2. "ab", "tt"  mem[(1,1)]
    3. 'a', 'a'

    dog frog

    complexities:
    1. O(m+n)
    2. O(m*n)

    """
    if len(str1) == len(str2) == 0:
        return 0

    memo = {}

    def helper(i, j):
        if i == len(str1) and j == len(str2):
            return 0
        if (i, j) in memo:
            return memo.get((i, j))
        if i == len(str1):
            return len(str2) - j
        if j == len(str2):
            return len(str1) - i
        if 0 <= i < len(str1) and 0 <= j < len(str2) and str1[i] == str2[j]:
            res = helper(i + 1, j + 1)
        else:
            a1 = helper(i + 1, j)
            a2 = helper(i, j + 1)
            # a3 = helper(i+1, j+1)
            res = 1 + min(a1, a2)
        memo[(i, j)] = res
        return memo[(i, j)]

    return helper(0, 0)


print(deletion_distance("abc", "adbc"))
