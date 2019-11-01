def num_places(x):
    nums = []
    a = 1
    while x != 0:
        y = x % 10
        nums.append(y * a)
        x = x // 10
        a = a * 10
    return sorted(nums, reverse=True)



def int_rom(num):
    rom_dict = {1: 'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX', 10:'X',
                20:'XX', 30:'XXX', 40:'XL', 50:'L', 60:'LX',70:'LXX', 80:'LXXX', 90:'XC', 100:'C',
                200:'CC', 300:'CCC', 400:'CD', 500:'D', 600:'DC', 700:'DCC', 800:'DCCC',900:'CM', 1000:'M',
                2000:'MM',3000:'MMM'}
    x = num_places(num)
    return ''.join([rom_dict[a] for a in x if a != 0])


print(int_rom(1200))

    
        
    

# print(int_rom(56))



#fix condition 110 1110
