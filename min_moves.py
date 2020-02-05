def minMoves(nums):
    return sum(nums) - min(nums)*len(nums)

print(minMoves([1,2,3]))