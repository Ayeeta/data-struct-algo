def search_pos(arr, x):
    if x in arr:
        return arr.index(x)
    else:
        arr.append(x)
        arr.sort()
        return arr.index(x)

print(search_pos([1,3,5,6], 2))