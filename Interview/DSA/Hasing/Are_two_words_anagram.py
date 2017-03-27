def anargams(a,b):
    len1 = len(a)
    len2 = len(b)

    from collections import Counter
    counter1 = Counter(a).items()
    counter2 = Counter(b).items()

    if counter1 == counter2 and len1 == len2:
        return True
    else:
        return False

a = "listen"
b = "enlise"
print anargams(a,b)