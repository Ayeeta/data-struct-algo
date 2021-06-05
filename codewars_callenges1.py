from int_roman import num_places
from sympy import simplify


def dupicate_encode(word):
    compr = word.lower()
    res = ""
    for i in word:
        if compr.count(i.lower())>1:
            res= res + ')'
        else:
            res= res + '('
    return res

# print(dupicate_encode("din"))

def in_array(a1,a2):
    r = []
    for i in a1:
        for j in a2:
            if i in j:
                r.append(i)
    return sorted(list(set(r)))

# print(in_array(["arp", "live", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"]))


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
    
    

# print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))

def rand(words):
    return ' '.join(sorted([word for word in words if word in '123456789']))


def order(sentence):
    x = {}
    sentence = sentence.split()
    for word in sentence:
        for l in word:
            if l in '123456789':
                x[int(l)]=word
    return ' '.join([v for k,v in sorted(x.items())])


# print(order("thi4s 3is on5e i1s m2y stor8y "))

def wordCount(word):
    count = 0
    for l in word:
        count = count + ord(l)%32
    return count


# print(wordCount('db'))

def high(x):
    x = x.split()
    num_count = []
    for word in x:
        num_count.append(wordCount(word))
    
    i = num_count.index(max(num_count))
    return x[i]

# print(high('cc bb aa db'))

def spin_words(sentence):
    s = sentence.split()
    for x in range(len(s)):
        if len(s[x]) >= 5:
            s[x] = s[x][::-1]
    return " ".join(s)
    

#print(spin_words("welcome"))


def num_replace(num):
    num_str = str(num)
    power = len(str(num))
    num_list = []
    for i in range(len(num_str)):
        x = int(num_str[i])*10**(power-1)
        num_list.append(x)
        power = power -1
    return num_list

def int_to_roman(num):
    rom_dict = {1: 'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX', 10:'X',
                20:'XX', 30:'XXX', 40:'XL', 50:'L', 60:'LX',70:'LXX', 80:'LXXX', 90:'XC', 100:'C',
                200:'CC', 300:'CCC', 400:'CD', 500:'D', 600:'DC', 700:'DCC', 800:'DCCC',900:'CM', 1000:'M',
                2000:'MM',3000:'MMM'}
    x = num_replace(num)
    return ''.join([rom_dict[x] for x in x if x != 0])

        

# print(int_to_roman(1000))

def anagram(word, words):
    word_list = []    
    for l in words:
        if len(l)==len(word) and set(l)==set(word):
            word_list.append(l)            
    return word_list

# print(anagram('abba', ['aabb', 'abcd', 'bbaa', 'dada']))




