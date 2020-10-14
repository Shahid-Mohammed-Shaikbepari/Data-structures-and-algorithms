import heapq
def word_count_engine(document):
    if len(document) < 1:
        return []
    document = document.lower()
    for c in document:
        if c in "!.',?:;":
            document = document.replace(c, "")
    lis = document.split()
    wordDic = {}
    for ind, w in enumerate(lis):
        if w not in wordDic:
            wordDic[w] = (1, ind)
        else:
            freq, first = wordDic.get(w)
            wordDic[w] = (freq + 1, first)
    print(wordDic.keys())
    # hea = heapq.nlargest(len(wordDic), wordDic.keys(), key=wordDic.get)
    b = [[k, str(v[0])] for k, v in sorted(wordDic.items(), key=lambda item: (-item[1][0], item[1][1]))]
    return b



document = "Practice makes perfect. you'll only get Perfect by practice. just practice!"

print(word_count_engine(document))

