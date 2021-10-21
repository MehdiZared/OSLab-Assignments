num = int(input("please enter a number : "))

num2=0
buf=num
count = 0

while buf != 0 :
    buf =int(buf/10) 
    count +=1

buf = num

for i in range(count):
    num2+=(buf%10)**count
    buf =int(buf / 10)

if num == num2 :
    print("yes")
else :
    print("NO")