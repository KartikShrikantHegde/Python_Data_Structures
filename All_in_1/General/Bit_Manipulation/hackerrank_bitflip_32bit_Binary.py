# Convert the binary number to 32 bit and flip the bit and print corresponding binary no

def myfunc(N):
    #N = N & 0xffffffff # 32 bit representation
    #print N
    print N ^ 0xffffffff
    #print bin(N)


myfunc(2147483647)