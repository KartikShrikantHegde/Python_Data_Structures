def minimum(a, b):
    if not a:
        for i in b:
            return b[i]

    if not b:
        for dict in range(len(a)):
            return [a[dict]]

    if a[0]['y'] > b[0]['y']:
        return [a[0]] + minimum(a[1:], b)
    return [b[0]] + minimum(a, b[1:])


a = [{"x": 200, "y": 1000},
     {"x": 201, "y": 900}]
b = [{"x": 203, "y": 950}]

print minimum(a, b)