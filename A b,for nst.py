a=int(input("enter number"))
k=1
for i in range(0,a):
    for j in range(1,a):
        print(" ",end=" ")
    for r in range(1,k):
        print(i,end=" ")
    print()
    k=k+2