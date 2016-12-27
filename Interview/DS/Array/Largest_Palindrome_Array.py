def Largest_Palindrome(my_str):
    my_list = list(my_str)
    max_total = ""
    max_now = ""
    for i in range(0,len(my_list)):
        max_now = max_now + my_list[i]
        if (max_now == max_now[::-1]):
            max_total = max_now
    return max_total


print Largest_Palindrome(my_str="abccbabacbcacba")