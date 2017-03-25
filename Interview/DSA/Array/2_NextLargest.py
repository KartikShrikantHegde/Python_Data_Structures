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

print nextHigher(5963)