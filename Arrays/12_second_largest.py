# Q12: Find 2nd highest element in array


def second_highest(array):
    highest_element = array[0]
    second_highest_val = -1  # or use float('-inf') if negative numbers are expected
    i = 0
    while i < len(array):
        if array[i] > highest_element:
            second_highest_val = highest_element
            highest_element = array[i]
        elif array[i] > second_highest_val and array[i] != highest_element:
            second_highest_val = array[i]
        i = i + 1
    return second_highest_val


result = second_highest([17, 4, 12, 98, 55])
print(result)
