# Convert the int no to binary and flip the bis and then again convert back to int

number = 4
reversed_bit = ""

b = bin(number)

for bits in range(2,len(b)):
    if b[bits] == '1':
        reversed_bit = reversed_bit+"0"
    else:
        reversed_bit = reversed_bit + "1"

print reversed_bit
print int(reversed_bit, 2)


'''
a = 0b110 # 6
mask = 0b111 # 7
desired =  a ^ mask # 0b1
'''