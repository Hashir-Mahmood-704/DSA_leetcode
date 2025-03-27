# Q2: Find the highest element of array

def find_highest_element(array):
    highest_element = array[0]
    i = 0
    while i < len(array):
        if array[i] > highest_element:
            highest_element = array[i]
        i = i + 1
    return highest_element


result = find_highest_element([125, 9, 21, 917, 3])
print(result)
