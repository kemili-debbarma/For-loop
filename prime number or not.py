a=int(input("enter num"))
for i in range(2,a):
    if a%i==0:
        print("not prime number")
        break
else:
    print("prime number")