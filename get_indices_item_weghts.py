def get_indices(arr, limit):
    for i in range(len(arr)):
        x = limit - arr[i]
        if x in arr[i+1:]:
            return sorted([i, arr[i+1:].index(x)+i+1], reverse=True)
    return []


arr = [4, 6, 10, 15, 16]
lim = 21
print(get_indices([12,6,7,14,19,3,0,25,40], 7))

