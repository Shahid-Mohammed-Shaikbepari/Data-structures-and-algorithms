def isPermutation(s1, s2):
    if len(s1) != len(s2) or len(s1) == 0:
        return False
    d1 = {}
    d2 = {}
    for i in s1:
        if i in d1:
            d1[i] = d1.get(i)+1
        else:
            d1[i] = 1
    for j in s2:
        if j in d2:
            d2[j] = d2.get(j)+1
        else:
            d2[j] = 1
    for i in d1:
        if not i in d2:
            return False
        if d1[i] != d2[i]:
            return False
    return True

if __name__ == "__main__":
    print(isPermutation('@=+-#', '#@+='))