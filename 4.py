x= input('Type a number : ')
x= int(x)
flag = False
flag2= False
for i in range (2,x):
    if x%i==0:
        flag = True
        break

if x%2==0:
    flag2 = True
    

if flag & flag2 :
    print('This number is EVEN and NOT PRIME.')

elif flag==False & flag2==True :
    print('This number is EVEN and PRIME.')

elif flag==False & flag2==False :
    print('This number is ODD and PRIME.')

else :
     print('This number is ODD and NOT PRIME.')



    

    
