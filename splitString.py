def balancedStringSplit(s):
        count=0
        balance=0
        for i in s :
            if i == "R" :
                balance+=1
            if i == "L":
                 balance-=1
            if balance == 0 :
                count+=1
        return count

print(balancedStringSplit('RRRLLLL'))