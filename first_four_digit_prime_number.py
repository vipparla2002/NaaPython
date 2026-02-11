import math


a = 1000

while(a/1000 >=1 and a/1000 <10): 
    if a%1000 in [0,2,4,5,6,8] or a%3 == 0 :
        pass
    else:
        is_prime = True
        for i in range(2, int(math.pow(a,1/2)) + 1):
            if a % i == 0:
                is_prime = False
                break
        if is_prime:
            print(a)
            break


    a += 1