#did not pass tests on leetcode
def remove_element(arr, x):
    new_arr = [elem for elem in arr if elem != x]
    return len(new_arr)


def remove_element2(arr, x):
    i = 0
    for elem in range(len(arr)):
        if arr[elem] != x:
            arr[i] = arr[elem]
            i += 1
    return i

print(remove_element2([3,2,2,3], 3))