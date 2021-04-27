def two_sum(nums, target):
    for i in range(len(nums)):
        x = target - nums[i]
        if x in nums[i+1:]:
            return [i, nums[i+1:].index(x)+i+1]
    
    

l = [3,2,4]
t = 6

print(two_sum(l, t))

def TwoSum(nums, target):
    for i in range(len(nums)):
        x = target - nums[i]
        if x in nums[i+1]:
            return [i, nums[i+1:].index(x)+1]