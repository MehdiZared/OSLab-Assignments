import random 


boys = ['ali', 'reza', 'yasin', 'benyamin', 'mehrdad', 'sajjad', 'aidin', 'shahin']
girls = ['sara', 'zari', 'neda', 'homa', 'eli', 'goli', 'mary', 'mina']

result=[]
for i in range(8) :
    r = random.choice(girls)
    result.append([boys[i],r])
    girls.remove(r)
print(result)


