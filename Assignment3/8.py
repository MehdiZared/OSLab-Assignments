a = int(input("enter a : "))
b = int(input("enter b : "))

if a > b:
    buf=a
    a=b
    b=buf
for i in range(b,(a*b)+1) :
    if i%a==0 and i%b==0:
        Kmm=i
        break
print("Kochektarin mazrabe moshtarak : ",Kmm)
