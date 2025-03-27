# Q17: Union of 2 sorted arrays

def makeUnion(array1, array2):
    resultArray = []
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] <= array2[j]:
            if len(resultArray) == 0 or resultArray[-1] != array1[i]:
                resultArray.append(array1[i])
            i = i + 1
        else:
            if len(resultArray) == 0 or resultArray[-1] != array2[j]:
                resultArray.append(array2[j])
            j = j + 1

    while i < len(array1):
        if len(resultArray) == 0 or resultArray[-1] != array1[i]:
            resultArray.append(array1[i])
        i = i + 1

    while j < len(array2):
        if len(resultArray) == 0 or resultArray[-1] != array2[j]:
            resultArray.append(array2[j])
        j = j + 1

    print(resultArray)


makeUnion([5, 6, 7, 8, 9], [5, 6, 7, 10])
