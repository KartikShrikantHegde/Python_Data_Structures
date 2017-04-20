def climbStairs( n):
    """
    :type n: int
    :rtype: int
    """
    a = b = 1
    for _ in range(n):
        a, b = b, a + b
    return a

print climbStairs(n=4)