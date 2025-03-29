# Q3: Find last occurrence of element using binary search


def findLastOccurrence(array, target):
    start = 0
    end = len(array) - 1
    ans = -1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            ans = mid
            start = mid + 1
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return ans


result = findLastOccurrence([1, 2, 2, 2, 2, 2, 4, 5, 5], 5)
print(result)
