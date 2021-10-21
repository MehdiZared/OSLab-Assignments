facts = []
for i in range(15) :
    buf=1
    for j in range(i+1) :
        buf*=j+1
    facts.append(buf)

userInput = int(input("Please enter a number : "))
if userInput in facts :
    print("YES")
else:
    print("NO")

