def longestPalindrome(s):
    res = [s[i:j] for i in range(len(s)) for j in range(i+1 , len(s)+1)]
    pal_list = {}
    #length_s = 0
    for word in res:
        if word == word[::-1]:
            pal_list[len(word)] = word
        return "No palindrome found"
    
    last_key =  list(pal_list.keys())[-1]
    return pal_list[last_key]


print(longestPalindrome('cbbd'))