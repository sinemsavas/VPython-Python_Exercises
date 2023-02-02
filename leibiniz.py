import math
f = open("leibiniz.txt", "w")
def leibiniz(n):

    sum=0
    for i in range(n):
        form = (-1)** i / (2*i+1)
        sum = sum + form

    return sum * 4


pi = [leibiniz(i) for i in range (1,100)]

f.write(str(pi) + " , " + str((pi)/math.pi) + " " + " \n")

f.close()


