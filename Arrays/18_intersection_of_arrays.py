# Q18: Intersection of two sorted arrays

def intersection(array1, array2):
    i = 0
    j = 0
    resultArray = []
    while i < len(array1) and j < len(array2):
        if array1[i] == array2[j]:
            resultArray.append(array1[i])
            i = i + 1
            j = j + 1
        elif array1[i] < array2[j]:
            i = i + 1
        else:
            j = j + 1

    print(resultArray)


intersection([1, 2, 2, 3, 3, 4, 5, 6], [2, 3, 3, 5, 6, 6, 7])
