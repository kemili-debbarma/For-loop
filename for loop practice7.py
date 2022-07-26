a=int(input("enter number"))
for i in range(1,a):
    for j in range(1,a):
        if i==1 or j==1 or i==3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()  