def getInd(num, list):
    l, r = 0, len(list)
    if r == 1:
        if num < list[0]:
            return 0,0
    while (r - l)>1:
        m = int((l + r) / 2)
        if list[m] == num:
            return -1
        elif list[m] > num:
            r = m
        else:
            l = m
    return l, r

a = [ -1]
b = -2
c = -3
l, r =getInd(b, a)
a.insert(r, b)
l, r =getInd(c, a)
a.insert(l, c)
d = 0
l, r =getInd(d, a)
a.insert(r,d)
print(a)