# Q20: Find longest subarray having target sum


def longestSubarray(array, targetSum):
    i = 0
    maxCount = 0
    while i < len(array):
        count = 0
        mySum = 0
        j = i
        while j < len(array):
            mySum = mySum + array[j]
            if mySum <= targetSum:
                count = count + 1
                j = j + 1
                if maxCount < count:
                    maxCount = count
            else:
                break
        i = i + 1
    print(maxCount)


longestSubarray([1, 1, 1, 1, 0, 5, 2, 2, 2, 4, 3], 4)
