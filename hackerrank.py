# # t = input()
# # for _ in xrange(t):
# #     x = input()
# #     n = input()
# #     arr = map(int, raw_input().strip().split())
# #     if canPair(arr, x):
# #         print "Yes"
# #     else:
# #         print "No"


def canPair(array, X):
    index_arr = []
    output_array = []
    for i in xrange(len(array)):
        for j in xrange(i + 1, len(array)):
            if i in index_arr and j in index_arr:
                i += 2
                j += 2
            elif i in index_arr:
                i += 1
            elif j in index_arr:
                j += 1
            else:
                if (array[i] + array[j]) % X == 0:
                    index_arr.append(i)
                    index_arr.append(j)
                    output_array.append((array[i],array[j]))
                else:
                    continue

    print index_arr
    print output_array
    if len(index_arr) == (len(array)):
        return True
    else:
        return False


print canPair(array=[6,4,8,12],X = 2)