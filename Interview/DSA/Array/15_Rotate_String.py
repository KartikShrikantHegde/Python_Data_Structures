def rotate(str1,str2):
    final_str = str1+str1

    if len(str1) == len(str2) and str2 in final_str:
        return True
    else:
        return False

str1 = "rotation"
str2 = "tionrotc"
print rotate(str1,str2)
