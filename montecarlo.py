import random
import math

f= open('montecarlo.txt','w')

i = 1
while i <= 10000000:
    hitCircle = 0
    if(i<100):
        for j in range(1,i+1) :
            Xrnd = random.random()
            Yrnd = random.random()

            if math.sqrt(Xrnd**2+Yrnd**2) < 1:
                hitCircle = hitCircle + 1

        calcpi = 4*(hitCircle/i)
        
        f.write(str(i)+') '+str(calcpi)+', '+str(calcpi/3.14)+'\n')

        i = i+1

    else:
        for j in range(1,i+1) :
            Xrnd = random.random()
            Yrnd = random.random()

            if math.sqrt(Xrnd**2+Yrnd**2) < 1:
                hitCircle = hitCircle + 1

        calcpi = 4*(hitCircle/i)
        
        f.write(str(i)+') '+str(calcpi)+', '+str(calcpi/3.14)+'\n')
        i = i*10

f.close()
