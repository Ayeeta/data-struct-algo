def non_repeating(string):  
    count_list = []
    print(string.isalpha())
    if string.isalpha() == True:
        l = string.lower()
        for i in range(len(l)):
            if l.count(l[i]) == 1:
                return string[i]
    for l in string:
        print(l)
        if l.isalpha():
            print(l)
            if string.count(l.lower()) == 1:
                return l
        if string.count(l) == 1:
            return l
           
        
    
    
    

    

print(non_repeating('Go hang a salami, I\'m a lasagna hog!'))