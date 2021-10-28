f = [0,1]

n=int(input())

for i in range(2,n+1) :
    f.append(f[i-2]+f[i-1])

for i in f :
    print(i , end=' ')
    