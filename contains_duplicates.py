def contains_dups(arr):
    s = set(arr)
    if len(arr) == len(s):
        return False
    else:
        return True

l = []
print(contains_dups(l))