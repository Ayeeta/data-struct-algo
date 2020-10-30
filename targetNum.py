def target(numList, i):
    for j in numList:
        x = i - j
        if x in numList:
            return [numList.index(j) + 1, numList.index(x) + 1]


print(target([-1,0], -1))