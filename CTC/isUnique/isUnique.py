def isUnique(str):
    dict = {}
    if len(str) == 0:
        return False
    for i in str:
        if i in dict:
            return False
        else:
            dict[i] = 1
    return True

if __name__ == '__main__':
    print(isUnique(""))