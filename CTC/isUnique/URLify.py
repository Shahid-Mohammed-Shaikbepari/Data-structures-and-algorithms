def URLify(str, tl):
    for i in range (tl):
        if str[i] == ' ':
            s = str[:i]
            s += '%20'


