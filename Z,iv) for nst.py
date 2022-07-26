a=int(input("enter number"))
for i in range(0,a):
    for j in range(0,a):
        if i+j==2 or j-i==2 or i+j==6 or i-j==2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()