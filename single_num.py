#not efficient
def single_number(nums):
    for i in range(len(nums)):
        if nums.count(nums[i]) == 1:
            return nums[i]

#soln 1
def single_number2(nums):
    dups = []
    for i in nums:
        if i not in dups:
            dups.append(i)
        else:
            dups.remove(i)
    return dups.pop()

def single_number3(nums):
    hash_t = {}
    for i in nums:
        try:
            hash_t.pop(i)
        except:
            hash_t[i] = 1
    return hash_t.popitem()[0]


print(single_number3([2,2,1]))