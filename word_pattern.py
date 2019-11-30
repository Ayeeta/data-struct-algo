def word_patterns(pattern, s):
    s_list = s.split(' ')

    if len(pattern) != len(s_list):
        return False
    
    pattern_dict = {}

    for i, char in enumerate(pattern):
        if char not in pattern_dict:
            if s_list[i] not in pattern_dict.values():
                pattern_dict[char] = s_list[i]
            else:
                return False
        elif pattern_dict[char] != s_list[i]:
            return False
    return True

print(word_patterns("abba", "dog cat cat dog"))