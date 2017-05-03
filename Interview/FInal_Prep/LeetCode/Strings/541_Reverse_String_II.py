def reverseStr(self, s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """

    if not s:
        return s

    if s is None:
        return None

    if len(s) < k:
        s = s[::-1]

    elif len(s) < (2 * k) and len(s) >= k:
        s = s[0:k][::-1] + s[k:]

    else:
        s = s[0:k][::-1] + s[k: (2 * k)] + self.reverseStr(s[(2 * k):], k)

    return s