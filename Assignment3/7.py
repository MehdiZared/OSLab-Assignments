
a = int(input("enter a : "))
b = int(input("enter b : "))

if a > b:
    buf=a
    a=b
    b=buf

for i in range(1, a+1):
    if((a % i == 0) and (b % i == 0)):
        Bmm = i
print("Bozorg tarin makhraje moshtarak = ",Bmm)
