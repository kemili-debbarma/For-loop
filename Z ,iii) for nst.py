a=int(input("enter num"))
for i in range(6,a,-1):
    for j in range(6,i,-1):
        print(" ",end=" ")
    for r in range(1,i):
        print(r,end=" ")
    print()