def gen(n):
    for i in range(1,n):
        if i % 2 == 0:
            yield i

for i in gen(6):
    print i