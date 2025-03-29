# Q6: Print extreme elements of array, one by one


def print_extremes(array):
    i = 0
    j = len(array) - 1
    while i <= j:
        if i == j:
            print(array[i], end=" ")
        else:
            print(array[i], array[j], end=" ")
        i = i + 1
        j = j - 1


print_extremes([1, 2, 3, 4, 5, 6])

