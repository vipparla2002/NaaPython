import math

a = 10**3

for i in range(10*a,a,-1):
    if i%10 in [0,2,4,5,6,8] or i%3 == 0:
        pass
    else:
        for j in range(3,int(math.pow(i,1/2))+1):
            if i%j == 0:
                break
        else:
            print(i)
            break