def str_occ(haystack, needle):
    if needle == "":
        return 0
    if needle in haystack:
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                return i
    if  needle not in haystack:
        return -1
    
# print(str_occ("aaaaa", "bba"))

def str_occ2(haystack, needle):
    if needle == "":
        return 0
    return haystack.find(needle)

print(str_occ2("hello", "llo"))