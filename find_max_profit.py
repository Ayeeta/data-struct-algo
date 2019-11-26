def min_max(arr):
    if len(arr) == 0:
        return 0
    else:
        min_val = min(arr)
        max_val = max(arr[arr.index(min_val):])
        if min_val < max_val:
            return max_val - min_val
        else:
            return 0

print(min_max([]))