def Isuniq(string):
    if(len(set(string))== len(string)):
        return True
    else:
        return False

print(Isuniq('Ayeeta'))