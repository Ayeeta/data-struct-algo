#not efficient
def single_number(nums):
    for i in range(len(nums)):
        if nums.count(nums[i]) == 1:
            return nums[i]

#efficient
def single_number2(nums):
    dups = []
    for i in range(len(nums)):
        if i not in dups:
            dups.append(i)
        else:
            dups.remove(i)
    return dups.pop()

print(single_number2([4,1,2,1,2]))