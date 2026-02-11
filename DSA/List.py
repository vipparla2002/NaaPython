import math
l = list((range(3),'a',math.pi, math.e,[math.factorial(a) for a in range(7) if a%2!=0],dict(map(lambda x:(x,x**3),range(5)))))
print(l)