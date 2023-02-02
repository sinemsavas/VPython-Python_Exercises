import random
import time

print(" "*15+"START\n")
star = 16;
print("|" + " "*star+ "*" + " "*(32-star)+"|"+ str(star-16))
i= 0

while(star !=32 and star !=0):
    move = random.choice([-1,1])
    i= i+1
    star = star+move;
    print("|"+" "*star+"*"+" "*(32-star)+"|"+str(star-16))
    time.sleep(0.01)

print("Count = " + str(i))
