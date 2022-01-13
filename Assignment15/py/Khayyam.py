n= int(input())
arr = [[1],[1,1]]
for i in range(2, n+1):
    temp = [1]
    for  j in range(1, i):
        temp.append(arr[i-1][j-1] + arr[i-1][j])
    temp.append(1)
    arr.append(temp)
    
for i in range(n):
    for j in arr[i] : 
        print(j,end = "\t")
    print()
