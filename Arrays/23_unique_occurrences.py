# Q23: Tell if occurrence of every element in array is unique or not


def uniqueOccurrence(array):
    occurrences = {}
    for element in array:
        if element in occurrences:
            occurrences[element] = occurrences[element] + 1
        else:
            occurrences[element] = 1

    valuesArray = []
    for value in occurrences.values():
        valuesArray.append(value)

    tempArray = []
    for element in valuesArray:
        if element in tempArray:
            return False
        else:
            tempArray.append(element)
    return True


result = uniqueOccurrence([3, 1, 2, 1, 2, 2, 2, 3, 3])
print(result)
