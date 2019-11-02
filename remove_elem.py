def remove_element(arr, x):
    new_arr = [elem for elem in arr if elem != x]
    return new_arr



print(remove_element([3,2,2,3], 3))