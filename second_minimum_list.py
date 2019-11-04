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


#merge two sorted arrays

def merge_arr(arr_a, arr_b):
    return sorted(arr_a + arr_b)

print(merge_arr([3,2,1], [1,2,3]))


#arrange +ve and -ve alone
def arrange_only(arr):
    positve_vals = [x for x in arr if x >= 0]
    negative_vals = [y for y in arr if y < 0]
    return sorted(negative_vals) + sorted(positve_vals)

print(arrange_only([3,2,4,-1,3,-5,0]))