num=input("enter num") 
sum=0
for i in range(0,int(len(num))):
  a=int(num[i])
  b=len(num)
  c=a**b
  sum=sum+c
print(sum)
if int(num)==sum:
    print("it is armstrong",sum)
else:
    print("not armstrong",sum)