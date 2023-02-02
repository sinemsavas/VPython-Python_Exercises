import math
x = [y*2*math.pi/50 for y in range(0,51)]
for fun in x:
    z=int(50*math.sin(fun))
    if(z==0):
        print("0")
    elif(z>0):
        print("+"*z)
    else:
        print("-"*-z)
    
