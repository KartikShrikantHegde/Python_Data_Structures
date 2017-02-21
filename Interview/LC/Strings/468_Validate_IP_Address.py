class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """

        hex = ['A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f', '1', '2', '3', '4', '5', '6', '7', '8', '9',
               '0']
        ary = IP.split(":")
        if len(ary) == 8 and len(ary[0]) <= 4 and len(ary[1]) <= 4 and len(ary[2]) <= 4 and len(ary[3]) <= 4 and len(
                ary[4]) <= 4 \
                and len(ary[5]) <= 4 and len(ary[6]) <= 4 and len(ary[7]) <= 4 \
                and ary[0] in (ary[0],16) and ary[1] in (ary[1],16) :
            return "IPv6"
        ary = IP.split(".")
        if len(ary) == 4:
            if ary[0].isdigit() and ary[1].isdigit() and ary[2].isdigit() and ary[3].isdigit() \
                    and int(ary[0]) < 256 and int(ary[1]) < 256 and int(ary[2]) < 256 and int(ary[3]) < 256 \
                    and not ary[0].startswith('0') and not ary[1].startswith('0') and not ary[2].startswith('0') and not \
            ary[3].startswith('0'):
                return "IPv4"
        return "Neither"

my_ip = Solution()
print my_ip.validIPAddress(IP="20EE:FGb8:85a3:0:0:8A2E:0370:7334")
