def int_rom(x):
    rom_dict = {1: 'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX', 10:'X',
                20:'XX', 30:'XXX', 40:'XL', 50:'L', 60:'LX',70:'LXX', 80:'LXXX', 90:'XC', 100:'C',
                200:'CC', 300:'CCC', 400:'CD', 500:'D', 600:'DC', 700:'DCC', 800:'DCCC',900:'CM', 1000:'M',
                2000:'MM',3000:'MMM'}
    if len(str(x)) == 1:
        return rom_dict[x]
    if len(str(x)) == 2:
        y = x % 10
        if y == 0:
            return rom_dict[x]
        j = x - y
        return rom_dict[j] + rom_dict[y]
    if len(str(x)) == 3:
        y = x % 100
        if y == 0:
            return rom_dict[x]
        j = x - y
        if len(str(y)) == 1:
            return rom_dict[j] + rom_dict[y]
        i = y % 10
        a = y - i
        return rom_dict[j] + rom_dict[a] + rom_dict[i]
    if len(str(x)) == 4:
        y = x % 1000
        if y == 0:
            return rom_dict[x]
        j = x - y
        if len(str(y)) == 1:
            return rom_dict[j] + rom_dict[y]
        if len(str(y)) == 2:
            i = y % 10
            a = y - i
            return rom_dict[j] + rom_dict[a] + rom_dict[i]
        if len(str(y)) == 3:
            i = y % 100
            if len(str(i)) == 1:
                a = y - i
                return rom_dict[j]+rom_dict[a] + rom_dict[i]
            if len(str(i)) == 2:
                a = y - i
                b = i % 10
                c = i - b
                return rom_dict[j] + rom_dict[a] + rom_dict[c] + rom_dict[b]
    

print(int_rom(3999))

#print(56%10)