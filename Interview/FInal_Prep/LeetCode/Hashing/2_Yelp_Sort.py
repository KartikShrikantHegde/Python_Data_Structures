def minimum(a):

    for i in range(0,len(a)-1):
        if a[i+1]['y'] > a[i]['y']:
            a[i + 1] , a[i] = a[i], a[i+1]

    return a

a = [{"x": 200, "y": 1000},
     {"x": 201, "y": 900},
    {"x": 202, "y": 950}]

print minimum(a)