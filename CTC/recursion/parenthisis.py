def GenParen(n):
    res = []
    str = [None]*(n*2)
    parenHelp(res, str, n, n, 0 )
    return res
def parenHelp(res, str, openC, closedC, index):
    if openC<0 or closedC<openC:
        return
    elif openC == 0 and  closedC == 0:
        s = ""
        res.append(s.join(str))
    else:
        str[index] = '('
        parenHelp(res, str, openC-1, closedC, index+1)
        str[index] = ')'
        parenHelp(res, str, openC, closedC-1, index+1)


def PrintPar(list):
    for l in list:
        print(l)

if __name__ == '__main__':
    list = GenParen(0)
    PrintPar(list)