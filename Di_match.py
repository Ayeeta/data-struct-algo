def diStringMatch(s):
    pt1, pt2 = 0, len(s)
    arr = []

    for i in s:
        if i == 'I':
            arr.append(pt1)
            pt1 += 1
        else:
            arr.append(pt2)
            pt2 -= 1
    return arr + [pt1]