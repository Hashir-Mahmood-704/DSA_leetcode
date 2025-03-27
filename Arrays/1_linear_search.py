# Q1: Find target using linear search

def linear_search(array, target):
    i = 0
    while i < len(array):
        if array[i] == target:
            return i
        i = i + 1
    return -1


result = linear_search([10, 20, 30, 40], 20)
print(result)
