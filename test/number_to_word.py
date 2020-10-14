hex_to_decimal = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "a": 10,
        "b": 11,
        "c": 12,
        "d": 13,
        "e": 14,
        "f": 15
    }

def Conv2minHexa(input):
    if len(input) == 0:
        return input
    else:
        while len(input) > 1:
            input = SumnConHex(input)
            input = sumnConDec(input)
            input = SumnConHex(input)
        return input

def SumnConHex(input):
    num = int(input)
    sum = 0
    while num != 0:
        sum += int(num%10)
        num = int(num/10)
    hexa = hex(sum)
    return str(hexa)[2:]


def sumnConDec(input):

    sum = 0
    for ch in input:
        sum += hex_to_decimal.get(ch)
    return str(sum)

if __name__ == '__main__':
    print(Conv2minHexa('8981'))
