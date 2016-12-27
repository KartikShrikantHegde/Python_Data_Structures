def reverse(my_string):
    temp_string = my_string.split(" ")
    reverse_str = temp_string[::-1]
    return " ".join(reverse_str)

my_str = "reverse words of a sentence"
print reverse(my_str)
