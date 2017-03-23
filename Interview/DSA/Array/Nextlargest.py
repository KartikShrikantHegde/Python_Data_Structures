def nextHigher(num):
    strNum=str(num)
    length=len(strNum)
    for i in range(length-2, -1, -1):
        current=strNum[i]
        right=strNum[i+1]
        if current<right:
            temp=sorted(strNum[i:])
            next=temp[temp.index(current)+1]
            temp.remove(next)
            temp=''.join(temp)
            return int(strNum[:i]+next+temp)
    return num
#
# def nextHigher(num):
#     strNum=str(num)
#     length=len(strNum)
#     for i in range(length-2, -1, -1):
#         current=strNum[i]
#         right=strNum[i+1]
#         if current<right:
#             current,right = right,current
#             new_str = strNum[:i] + current + right + strNum[i+2:]
#             temp = sorted(strNum[i+:])
#             print new_str
#             # temp = sorted(strNum[i+1:])
#             # final_no = strNum[:i]+current+temp
#             # print final_no

print nextHigher(3784)