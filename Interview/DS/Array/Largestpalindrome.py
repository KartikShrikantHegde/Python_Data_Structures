# Naive apparoach
# def Largepalindrome(no):
#     for i in range(no, ):
#         no += 1
#         if str(no) == str(no)[::-1]:
#             print no
#             break

# Best method

def Largepalindrome(no):
    my_no = str(no)
    if len(my_no) % 2 == 0:
        first_part = my_no[:(len(my_no) / 2)]
        second_part = my_no[(len(my_no) / 2):]
        reverse_first_part = first_part[::-1]
        if int(reverse_first_part) > int(second_part):
            final_no = first_part+reverse_first_part
            print final_no
        else:
            incremented_val = int(first_part)+1
            reverse_incremented_val = str(incremented_val)[::-1]
            final_no = str(incremented_val) + reverse_incremented_val
            print final_no
    else:
        first_part = my_no[:(len(my_no) / 2)]
        second_part = my_no[(len(my_no) / 2):((len(my_no) / 2) + 1)]
        third_part = my_no[((len(my_no) / 2)+1):]
        reverse_first_part = first_part[::-1]
        if int(reverse_first_part) > int(third_part):
            final_no = first_part+second_part+reverse_first_part
            print final_no
        else:
            incremented_val = first_part+second_part
            new_incremented_val = int(incremented_val)+1
            reverse_incremented_val = str(new_incremented_val)[-2::-1]
            final_no = str(new_incremented_val)+reverse_incremented_val
            print final_no

Largepalindrome(1239712)