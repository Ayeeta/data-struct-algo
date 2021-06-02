def dupicate_encode(word):
    compr = word.lower()
    res = ""
    for i in word:
        if compr.count(i.lower())>1:
            res= res + ')'
        else:
            res= res + '('
    return res

print(dupicate_encode("din"))

def in_array(a1,a2):
    r = []
    for i in a1:
        for j in a2:
            if i in j:
                r.append(i)
    return sorted(list(set(r)))

print(in_array(["arp", "live", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"]))


def isEven(i):
    if i%2==0:
        return 'True'
    else:
        return 'False'


def find_outlier(int_arr):
    res = []
    for i in range(len(int_arr)):
        a = isEven(int_arr[i])
        res.append(a)
    if res.count('True')> res.count('False'):
        i = res.index('False')
        return int_arr[i]
    else:
        x = res.index('True')
        return int_arr[x]
    
    

print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))

