# Q19: Find the only missing number in array of range [0, n].


def findMissingNumber(array):
    n = len(array)
    occurrences = {}
    i = 0
    while i <= n:
        occurrences[i] = 0
        i = i + 1
    i = 0
    while i < len(array):
        occurrences[array[i]] = occurrences[array[i]] + 1
        i = i + 1

    for key, value in occurrences.items():
        if value == 0:
            return key
    return n


result = findMissingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1])
print(result)
