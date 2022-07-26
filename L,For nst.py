a=int(input("enter number"))
k=1
for i in range(1,a):
    for j in range(1,i):
        print(k,end=" ")
        k=k+1
    print()