def solution(A, K):
    n = len(A)
    for i in range(n - 1):
        if not (A[i]+1 == A[i+1] or A[i] == A[i+1]):
            return False

    if (A[0] != 1 or A[n - 1] != K):
        return False
    else:
        return True

A = [1,  1, 3]
K = 3
# print(solution(A, K))


def solution1(S):
    lower = [False] * 26
    upper = [False] * 26
    result = "NO"
    a_ascii = ord('a')
    A_ascii = ord('A')
    for i in range(len(S)):
        if S[i].islower():
            lower[ord(S[i]) - a_ascii] = True
        else:
            upper[ord(S[i]) - A_ascii] = True
    for i in range(26):
        if lower[i] and upper[i]:
            result = chr(ord("A") + i)
    return result

S= 'aaBabcDaA'
# print(solution1(S))

from collections import Counter
def solution3(S):
    res = 0
    uniqueSet = set()
    count = Counter(S)
    val = count.values()
    for i in val:
        temp = i
        while temp>0 and temp in uniqueSet:
            temp -=1
            res += 1
        if temp > 0:
            uniqueSet.add(temp)
    return res

S1= ""

print(solution3(S1))


