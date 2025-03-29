# Q24: Find repeated and missing elements in array of range [1, n]


def findRepeatedAndMissingNumber(array):
    n = len(array)
    occurrences = {}
    i = 1
    while i <= n:
        occurrences[i] = 0
        i = i + 1
    i = 0
    while i < len(array):
        occurrences[array[i]] = occurrences[array[i]] + 1
        i = i + 1
    ansArray = [None, None]
    for key, value in occurrences.items():
        if value == 2:
            ansArray[0] = key
        if value == 0:
            ansArray[1] = key
    return ansArray


result = findRepeatedAndMissingNumber([3, 2, 2])
print(result)
