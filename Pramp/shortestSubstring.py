#
# def get_shortest_unique_substring(arr, str):
# if len(arr) > len(str):
# return ""
#
# startSize = len(arr)
# for size in range(startSize, len(str)+1):
# for num in range(0, len(str)+1- size):
# subString = str[num : num+size]
# if Check(subString, arr):
#   return subString
# return ""
#
# def Check(s, arr):
# for let in arr:
# if let not in set(s):
# return False
# return True
#
#
def get_shortest_unique_substring(arr, str):
    if len(arr) > len(str):
        return ""

    hp = tp = 0
    counter = 0
    dict = {}
    result = ""
    for tp in range(0, len(str)):
        if str[tp] in arr:
            if str[tp] not in dict or dict[str[tp]] == 0:
                counter += 1
                dict[str[tp]] = 1
            else:
                dict[str[tp]] += 1

        while counter == len(arr):
            subStr = str[hp: tp + 1]
            if len(subStr) == len(arr):
                return subStr
            if result == "" or len(result) > len(subStr):
                result = subStr
            ch = str[hp]
            if ch in dict:
                dict[ch] -= 1
                if dict[ch] == 0:
                    counter -= 1
            hp += 1

    return result


print(get_shortest_unique_substring(['a', 'b'], "edcbag"))
