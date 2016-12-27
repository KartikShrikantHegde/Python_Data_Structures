class Solution(object):
    def __init__(self, bin_no):
        self.my_bin = bin_no

    def count_dig(self):
        self.my_bin = str(self.my_bin)
        count_0 = 0
        count_1 = 0
        for ch in self.my_bin:
            if ch == '1':
                count_1 += 1
            else:
                count_0 += 1

        # return count_0,count_1

        print "No of zero's are: %s" % count_0
        print "No of one's are: %s" % count_1


mySol = Solution(1011)
mySol.count_dig()
