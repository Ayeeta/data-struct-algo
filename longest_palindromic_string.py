def longestPalindrome(s):
    res = [s[i:j] for i in range(len(s)) for j in range(i+1 , len(s)+1)]
    return res


print(longestPalindrome('geeks'))