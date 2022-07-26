a=int(input("enter num"))
for i in range(1,a+1,2):
    for j in range(i,a,2):
        print(" ",end=" ")
    for k in range(0,i):
        print("*",end=" ")
    print( )



