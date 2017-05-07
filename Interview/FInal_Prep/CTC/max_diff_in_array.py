def  maxDifference(a):
    if not a:
        return 0
    if len(a) == 1:
        return (a[0])
    max_diff = a[1] - a[0]
    min_element = a[0]
    max = a[0]
    desc = True
    for i in range(1, len(a)):
        if max > a[i]:
            max = a[i]
        else:
            desc = False
            break
    if desc:
        return (-1)
    for i in range(1, len(a)):
        if a[i] - min_element > max_diff:
            max_diff = a[i] - min_element
        if a[i] < min_element:
            min_element = a[i]
    return(max_diff)

print maxDifference(a=[])