def square_digits(num):
    sq_str = ""
    for i in str(num):        
        sq_str += str(int(i)**2)
    return int(sq_str)

print(square_digits(000))