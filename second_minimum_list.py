def second_minimum(arr):
    arr.sort()
    return arr[1]


print(second_minimum([8,2,4,1,6,4,3,7,8,9]))


#first non repeating elements of an array
def non_repeating(arr):
    elem = 0
    for i in range(len(arr)):
        elem = arr.count(arr[i])
        if elem == 1:
            return arr[i]
                

print(non_repeating([8,3,2,4,1,2,8,6,9,2]))