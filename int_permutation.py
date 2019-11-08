import itertools

def int_perm(int_list):
    set_lists =  list(itertools.permutations(int_list))
    l = []
    for set_list in set_lists:
        l.append(list(set_list))
    return l


print(int_perm([1,2]))