def isPalindrome(i):
    j = str(i)
    if j == j[::-1]:
        return True
    return False