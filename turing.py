def comp(nums):
    m = float("-inf")
    for n in nums:
        if n > m:
            m+= 1
    return m  

print(comp([1,2,3]))