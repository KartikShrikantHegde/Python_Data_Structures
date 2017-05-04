def checkRecord(self, s):
    """
    :type s: str
    :rtype: bool
    """

    if s is None:
        return False

    if not s:
        return True

    if s[0] == 'A':
        no_of_a = 1
    else:
        no_of_a = 0

    no_of_con_l = 0

    for i in range(1, len(s)):

        if s[i] == 'A':
            no_of_a += 1

        if no_of_a > 1:
            return False

        if s[i] == 'L' and s[i - 1] == 'L':
            no_of_con_l += 1
            if no_of_con_l > 1:
                return False
        else:
            no_of_con_l = 0

    return True