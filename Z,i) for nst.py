a=int(input("enter number"))
for i in range(0,a):
    for c in range(0,a):
        if i+c==2 or c-i==2 or i-c==2 or i+c==6 or i-c==2 or i==2 or c==2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()