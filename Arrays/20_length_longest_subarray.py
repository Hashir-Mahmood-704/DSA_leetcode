# Q20: Find length of highest length subarray having the target sum.


def findHighestLength(array, targetSum):
    i = 0
    j = 1
    length = 0
    highestLength = 0
    sum = array[i] + array[j]
    while j < len(array):
        if sum < targetSum:
            j = j + 1
            if j < len(array):
                sum = sum + array[j]
        elif sum > targetSum:
            sum = sum - array[i]
            i = i + 1
        else:
            length = j - i + 1
            if highestLength < length:
                highestLength = length
            j = j + 1
            if j < len(array):
                sum = sum + array[j]
    print(highestLength)


# findHighestLength([1, 1, 3, 4, 1, 6, 5, 2], 8)
findHighestLength([1, 1, 1, 1, 1, 2, 2, 2, 4, 3], 5)