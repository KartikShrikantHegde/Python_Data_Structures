def reverse_str(my_str):
    print my_str.isalnum()
    return my_str.lower() == my_str[::-1].lower() and my_str.isalnum() == my_str[::-1].isalnum()

print reverse_str(my_str="A man, a plan, a canal: Panama")