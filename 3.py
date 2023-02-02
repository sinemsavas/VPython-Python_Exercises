perfectnum = []
i=1

while (len(perfectnum) < 4):
    sum = 0
    for j in range(1,i):
        if i % j == 0:
            sum = sum + j

    if sum ==i:
        perfectnum.append(i)
    i= i +1

print (perfectnum)
