def substr(s):
    start, maxlen = 0, 0
    used_char = {}
    for i, char in enumerate(s):
        if char in used_char and start <= used_char[char]:
            start = used_char[char] + 1
        else:
            maxlen = max(maxlen, i - start + 1)
        used_char[char] = i
    return maxlen

print substr('dvdf')
