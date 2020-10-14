def isPalindromePermutation(s):
    if len(s) == 0:
        return False
    alpha = [0]*26
    c = index = -1
    for i in s:
        val = ord(i)
        if val >= 65 and val <= 90:
            index = val-65
            alpha[index] += 1
        elif val >= 97 and val <= 122:
            index = val - 97
            alpha[index] += 1
    odd = False
    sum = 0
    for i in alpha:
        sum |= i
        if i%2 != 0:
            if odd == False:
                odd = True
            else:
                return False
    if sum == 0:
        return False
    return True

if __name__=="__main__":
    res = isPalindromePermutation("   ****a")
    print(res)