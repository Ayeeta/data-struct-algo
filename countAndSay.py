def cAndS(n):
    if n == 1:
        return "1"
    elif n == 2:
        return "11"
    string = "11"
    for i in range(2, n):
        newsb = []
        prev = string[0]
        cnt = 1
        for symbol in string[1:]:
            if symbol == prev:
                cnt += 1
            else:
                newsb.append(str(cnt) + prev)
                prev = symbol
                cnt = 1
        newsb.append(str(cnt) + prev)
        string = "".join(newsb)
    return string