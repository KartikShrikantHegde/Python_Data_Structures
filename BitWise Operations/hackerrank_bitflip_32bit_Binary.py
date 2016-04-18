# Convert the binary number to 32 bit and flip the bit and print corresponding binaray no

for _ in range(int(raw_input())):
    N = int(raw_input())
    N = N & 0xffffffff # 32 bit representation
    print N ^ 0xffffffff
