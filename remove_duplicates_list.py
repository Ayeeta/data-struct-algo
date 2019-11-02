def remove_duplicates(nums):
    if len(nums) == 0:
        return 0
    i = 0
    for elem in range(1, len(nums)):
        if nums[elem] != nums[i]:
            i += 1
            nums[i] = nums[elem]
            
    return i + 1

print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]))