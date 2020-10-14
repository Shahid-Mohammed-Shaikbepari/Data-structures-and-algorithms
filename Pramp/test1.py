def is_match(text, pattern):
    def recurse(i, p):
        if i == len(text) and p == len(pattern):
            return True
        if p == len(pattern):
            return False
        if i == len(text):
            return False
        if 0 <= p < len(pattern) - 1 and pattern[p + 1] == "*":
            if recurse(i, p + 2) or recurse(i + 1, p):
                return True

        if 0 <= i < len(text) and 0 <= p < len(pattern) and (text[i] == pattern[p] or pattern[p] == "."):
            return recurse(i + 1, p + 1)
        return False

    return recurse(0, 0)


print(is_match("abbdbb", "ab*d"))