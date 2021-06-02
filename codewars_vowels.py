def disemvowel(string_):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    return "".join([x for x in string_ if x not in vowels])

def disemvowel2(string_):
    return "".join([s for s in string_ if s.lower() not in "aeiou"])

print(disemvowel2('The website is attacked LOL'))