def contains_dups(nums, k):
    seen = {}
    for i, x in enumerate(nums):
        if x in seen and abs(seen[x] - i) <= k:
            return True
        else:
            seen[x] = i
    return False

nums = [1,2,3,1]
k = 3
print(contains_dups(nums, k))