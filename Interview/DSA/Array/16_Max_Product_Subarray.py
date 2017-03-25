def lps(A):
    MinTemp = A[0]
    MaxTemp = A[0]
    Max = A[0]
    for i in xrange(1, len(A)):
        MinTemp, MaxTemp = min(A[i], A[i]*MinTemp, A[i]*MaxTemp),max(A[i], A[i] * MaxTemp,A[i]*MinTemp)
        Max = max(Max, MaxTemp)
    return Max


print lps(A=[-2,3,-4])