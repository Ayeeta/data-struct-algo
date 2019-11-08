import itertools
# faster 28ms
def int_perm(int_list):
    set_lists =  list(itertools.permutations(int_list))
    l = []
    for set_list in set_lists:
        l.append(list(set_list))
    return l

#slower by 36ms
def int_perm2(int_list):
    return [list(x) for x in list(itertools.permutations(int_list))]


print(int_perm([1,2]))