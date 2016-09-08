def Count_Dig(my_Binary):
    my_str_binary = str(my_Binary)
    count_0 = 0
    count_1 = 0
    for ch in my_str_binary:
        if (ch == '1'):
            count_1 += 1
        else:
            count_0 = count_0 + 1

    print  "No of zeroe's are: %s" % count_0
    print  "No of one's are: %s" % count_1


Count_Dig(1000)
