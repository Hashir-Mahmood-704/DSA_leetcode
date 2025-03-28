# Q8: Find the one only element whose occurrence is 1 in array.


def find_once_occurred_element(array):
    occurrences = {}
    i = 0
    while i < len(array):
        if array[i] in occurrences:
            occurrences[array[i]] = occurrences[array[i]] + 1
        else:
            occurrences[array[i]] = 1
        i = i + 1
    print(occurrences)

    for key, value in occurrences.items():
        if value == 1:
            return key

    return -1


result = find_once_occurred_element([2, 4, 6, 8, 4, 2, 2, 8, 8])
print(result)
