def maxPathSum(ar1, ar2, m, n):
    # initialize indexes for ar1[] and ar2[]
    i, j = 0, 0

    # Initialize result and current sum through ar1[] and ar2[]
    result, sum1, sum2 = 0, 0, 0

    # Below 3 loops are similar to merge in merge sort
    while (i < m and j < n):

        # Add elements of ar1[] to sum1
        if ar1[i] < ar2[j]:
            sum1 += ar1[i]
            i += 1

        # Add elements of ar2[] to sum1
        elif ar1[i] > ar2[j]:
            sum2 += ar2[j]
            j += 1

        else:  # we reached a common point

            # Take the maximum of two sums and add to result
            result += max(sum1, sum2)

            # Update sum1 and sum2 for elements after this intersection point
            sum1, sum2 = 0, 0

            # Keep updating result while there are more common elements
            while (i < m and j < n and ar1[i] == ar2[j]):
                result += ar1[i]
                i += 1
                j += 1

    # Add remaining elements of ar1[]
    while i < m:
        sum1 += ar1[i]
        i += 1
    # Add remaining elements of b[]
    while j < n:
        sum2 += ar2[j]
        j += 1

    # Add maximum of two sums of remaining elements
    result += max(sum1, sum2)

    return result

arr1 = [1, 2, 3, 5, 7, 9, 10, 11, 15, 16, 18, 25, 50]
arr2 = [3, 6, 7, 8, 10, 12, 15, 18, 100]

print maxPathSum(arr1, arr2,len(arr1),len(arr2))
