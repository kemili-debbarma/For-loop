a=int(input("enter number"))
k=1
for i in range(0,a):
    for j in range(1,a-i):
        print(" ",end=" ")
    for c in range(1,k-1):
        print(i,end=" ")
    print()
    k=k+2