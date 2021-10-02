t=int(input())
for i in range(t): 
    n,m = map(int,input().split())
    arr=[0]*n
    for i in range(m):
        a,b,k=map(int,input().split())
        for x in range(a-1,b,1):
            arr[x]=arr[x]+k
        #for j in range(a,b+1):
            #arr[j]+=k
    print(max(arr))
