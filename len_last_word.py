def length_of_last_word(S):
    l = len(S.split())
    if l == 0:
        return 0
    else:
        return len(S.split()[l-1])


s = "Hello worlds fo"
print(length_of_last_word(s))