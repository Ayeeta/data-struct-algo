def mergeSortedLists(l1, l2):
    return sorted(l1+l2)

l1 = [1,2,4]
l2 = [1,3,4]

print(mergeSortedLists(l1,l2))