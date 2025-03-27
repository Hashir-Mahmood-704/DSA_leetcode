# Q5: Find target element by reverse linear search


def reverse_linear_search(array, target):
    i = len(array) - 1
    while i > -1:
        if array[i] == target:
            return i
        i = i - 1
    return -1


result = reverse_linear_search([22, 54, 76, 13, 98], 76)
print(result)
