def reverse(my_str):
    my_str = my_str.split()
    my_str = my_str[::-1]
    my_str = " ".join(my_str)

    return my_str

print reverse(my_str="reverse words of a sentence")


