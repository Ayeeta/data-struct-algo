nums = [0]

def remove_duplicates(nums):
    nums.sort()
    count_len = 1
    curr = 0
    if len(nums) == 0:
        return 0
    for i in range(1, len(nums)):
        if nums[i] != nums[curr]:
            count_len += 1
        nums[curr] = nums[i]
    return count_len

print(remove_duplicates(nums))