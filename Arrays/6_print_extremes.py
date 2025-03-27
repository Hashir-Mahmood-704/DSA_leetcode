# Q6: Print extreme elements of array, one by one


def print_extremes(array):
    output = ""
    i = 0
    j = len(array) - 1
    while i <= j:
        if i == j:
            output = output + " " + str(array[i])
        else:
            output = output + " " + str(array[i]) + " " + str(array[j])
        i = i + 1
        j = j - 1
    return output


result = print_extremes([1, 2, 3, 4, 5, 6])
print(result)
