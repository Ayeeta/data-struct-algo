def rob(house_list):
    even, odd = 0,0

    for i in range(len(house_list)):
        if i % 2 == 0:
            even = max(odd, even + house_list[i])
        else:
            odd = max(even, odd + house_list[i])
    return max(even, odd)