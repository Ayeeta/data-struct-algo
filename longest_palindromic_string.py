def longestPalindrome(s):
    if len(s) >= 1:
        if s == s[::-1]:
            return s
        else:
            res = [s[i:j] for i in range(len(s)) for j in range(i+1 , len(s)+1)]
            pal_list = {}
   
            for word in res:
                if word == word[::-1]:
                    pal_list[len(word)] = word
            
            last_key = max(list(pal_list.keys()))
            return pal_list[last_key]
    return ""


print(longestPalindrome("abadd"))