def isHappy(n):
        observed_dict = dict()
        while n not in observed_dict:
            observed_dict[n] = None
            sum = 0
            while n != 0:
                t = n % 10   
                if t != 0:  
                    sum += t**2
                    n -= t
                else:
                    n = int(n/10)
            n = sum

            if n == 1:
                return True
        return False

print(isHappy(19))