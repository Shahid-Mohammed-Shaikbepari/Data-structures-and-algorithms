
def reverse_words(arr):

    if len(arr) < 1:
        return []
    def mirrorRev(start, end):
        while start <= end:
            arr[start], arr[end] = arr[end], arr[start]
            start, end = start +1, end -1

    h , t = 0, len(arr ) -1
    mirrorRev(h, t)
    print (arr)
    wordStart = -1
    for i in range(0, len(arr)):
        if arr[i] == " " and wordStart != -1:
            mirrorRev(wordStart, i- 1)
            print(arr)
            wordStart = -1
        elif i == len(arr) - 1:
            mirrorRev(wordStart, len(arr) - 1)
        elif wordStart == -1:
            wordStart = i

    return arr

    '''  
    arr = "".join(arr).split()
    arr.reverse()
    return list(arr)
    '''

    '''
    reversed_Sent = ""
    for w in range(len(sent_li)-1, -1, -1):
      reversed_Sent += sent_li[w]
      reversed_Sent += " "
  
    return list(reversed_Sent)[:-1]
   '''


arr = ['p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
       'm', 'a', 'k', 'e', 's', '  ',
       'p', 'r', 'a', 'c', 't', 'i', 'c', 'e']

print(reverse_words(arr))





