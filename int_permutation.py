import itertools

def int_perm(int_list):
    return [list(x) for x in list(itertools.permutations(int_list))]


print(int_perm([1,2]))