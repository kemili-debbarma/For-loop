a=int(input("enter num"))
for i in range(1,a):
    for j in range(1,a-i):
        print(" ",end=" ")
    for k in range(0,i):
        print(i-k,end=" ")
    for r in range(2,i+1):
        print(r,end=" ")
    print()
