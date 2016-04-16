number = 0
reversed_bit = ""

b = bin(number)
print b

for bits in range(2,len(b)):
    if b[bits] == '1':
        reversed_bit = reversed_bit+"0"
    else:
        reversed_bit = reversed_bit + "1"

print reversed_bit
print int(reversed_bit,2)