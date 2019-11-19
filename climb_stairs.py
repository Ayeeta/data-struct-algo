def climb_stairs_prob(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    st = [0]*n
    st[0] = 1
    st[1] = 2
    for i in range(2, n):
        st[i] = st[i -2]+st[i -1]
    return st[n-1]

print(climb_stairs_prob(5))