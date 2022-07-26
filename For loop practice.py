a=int(input("enter number"))
for i in range(1,a):
    for j in range(1,a):
        if i==4 or i+j==5 or j-i==3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()