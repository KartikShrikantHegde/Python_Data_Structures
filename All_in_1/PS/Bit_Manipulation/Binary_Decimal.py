def Bin_Dec(binary_no):
    result = 0
    count = 0

    # Convert the no to string

    binary_no_str = str (binary_no)

    # reverse the digits

    reverse_str = binary_no_str[::-1]

    for ch in reverse_str:
        result = result + (int (ch) * (2 ** count))
        count = count + 1
    print result


Bin_Dec(1001100)