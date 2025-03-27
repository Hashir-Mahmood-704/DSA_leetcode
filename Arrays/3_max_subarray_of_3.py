# Q3: Find subarray of length 3 with max sum


def max_subarray(array):
    if len(array) < 3:
        print("Error! Array length must be more than 2")
        return
    mySum = array[0] + array[1] + array[2]
    maxSum = mySum
    targetIndex = 0
    i = 1
    while i + 2 <= len(array) - 1:
        mySum = mySum - array[i - 1]
        mySum = mySum + array[i + 2]
        if mySum > maxSum:
            maxSum = mySum
            targetIndex = i
        i = i + 1

    print(array[targetIndex], array[targetIndex + 1], array[targetIndex + 2])


max_subarray([2, 4, 1, 8, 3, 9, 1])
