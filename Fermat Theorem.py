limit = 200
c=0
x=3

while c<limit :
    for y in range(1,x):
        a = (x*x)-(y*y)
        b = 2 * x * y
        c = (x*x) + (y*y)


        if c>limit:
            break
        
        print(b,a,c)

    
    x+=1

        
