import itertools

def permII(arr):
    return [list(x) for x in list(set(itertools.permutations(arr)))]

print(permII([1,1,2]))