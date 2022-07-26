a=int(input("enter number"))
k=1
for i in range(1,a):
    for j in range(1,5):
        if i==1 or j==1 or i==4 or j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    k=k+1