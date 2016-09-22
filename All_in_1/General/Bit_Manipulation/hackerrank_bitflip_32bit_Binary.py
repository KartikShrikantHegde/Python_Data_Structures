# Convert the binary number to 32 bit and flip the bit and print corresponding binary no

def myfunc(N):
    print N ^ 0xffffffff
    # or print N ^ 4294967295 (2^32-1)


myfunc(2147483647)