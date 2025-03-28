# Q23: Merge two ascending order arrays


def mergeArrays(array1, elements1, array2, elements2):
    i = elements1
    print(i)
    j = 0
    while j < elements2:
        array1[i] = array2[j]
        i = i + 1
        j = j + 1

    array1.sort()
    print(array1)


mergeArrays([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
