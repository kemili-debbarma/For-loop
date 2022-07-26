a=int(input("enter number"))
k=7
for i in range(0,a):
    for j in range(6,a-i,-1):
        print(" ",end=" ")
    for c in range(1,k+1):
        print("*",end=" ")
    print()
    k=k-2