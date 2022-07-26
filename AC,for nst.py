a=int(input("enter number"))
r=65
for i in range(65,a):
     for j in range(65,i):
          print(chr(r),end=" ")
          r=r+1
     print()
