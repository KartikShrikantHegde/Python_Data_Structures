def merge_interval(a):
    lent = len(a)
    for i in range(1,lent):
        print a[i][i-1], a[i-1][len(a[i-1])-1]
        if a[i][i-1] < a[i-1][len(a[i-1])-1]:
            a[i-1] = [a[i-1][i-1],a[i][len(a[i])-1]]
            del a[i]

    return a

arr = [[1,3],[2,6],[8,10],[12,15]]

print merge_interval(arr)

