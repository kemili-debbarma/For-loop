a=int(input("enter the number"))
for r in range(1,a+1):
    for j in range(r,a):
        print(" ",end="")
    for k in range(0,r):
          print("*",end=" ")
    print() 