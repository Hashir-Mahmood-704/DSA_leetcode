# Q1_Find target element in sorted array using binary search
# Note: In binary search, the array must be sorted


def findTarget(array, target):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1


result = findTarget([2, 4, 11, 14, 19, 22, 29], 2)
print(result)
