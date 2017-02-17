add_sum = '1234'
x = map(str, list(add_sum))
print x


pasccal triangle


def generate(self, numRows):
    res = [[1]]
    for i in range(1, numRows):
        res += [map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1])]
    return res[:numRows]