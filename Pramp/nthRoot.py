def root(x, n):
    if n == 0:
        return 0
    l = 0
    h = x

    while l <= h:
        # print("l " + str(l))
        # print("h " + str(h))

        mid = float(l + h) / 2
        # print("mid " + str(mid))
        if abs(x - mid ** n) <= 0.001:
            return mid

        elif mid ** n < x:
            l = mid

        elif mid ** n > x:
            h = mid

    return mid


print(root(7, 3))
