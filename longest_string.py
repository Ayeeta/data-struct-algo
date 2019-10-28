# Given a string, find the length of the longest substring without repeating characters.

def longest_substring(s):
    s_dict = {}
    max_s = curr_max = start = 0

    for i, j in enumerate(s):
        if j in s_dict and s_dict[j] >= start:
            max_s = max(max_s, curr_max)
            curr_max = i - s_dict[j]
            start = s_dict[j] + 1
        else:
            curr_max += 1
        s_dict[j] = i
    return max_s


# print(longest_substring("abcabcbb"))
s = "abbcd"
subs= ""
# for i in range(len(s)):
#     subs += s[i]
#     if 
    
    
print(subs)