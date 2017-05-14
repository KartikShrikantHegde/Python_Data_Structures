def way_up(n):
    a = b = c = 1

    for _ in range(n):
        a , b , c = c , a + b, b + c

    return a

print way_up(2)