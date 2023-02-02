
import math

def factorial (n):
    res =1
    defaultnum = (math.sqrt(math.pi))/2
    
    if n == 0.5:
        res= defaultnum
    elif isinstance(n, float):
        while(n>0.5):
            res = res*n
            n= n-1
            res=res*defaultnum
    else:
        for i in range(n):
            res= res *(i+1)

    print (res)
    return res
factorial(1.5)
