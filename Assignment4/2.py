n=int(input())
m=int(input())

for i in range(m) :
    for j in range(n):
        if j%2==0 :
            print('*',end='')
        else:
            print('#',end='')
    print()