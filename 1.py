t=int(input())
for _ in range(t):
    n=int(input())
    k=[int(x) for x in input().split()[0:n*n]]
    mat=[]
    s=0
    for i in range(n):
        x=[]
        for j in range(n):
            x.append(k[s])
            s+=1
        mat.append(x)
        w=[]
    for j in range(n):
        for i in range(n):
            q=mat[i][n-j-1]
            w.append(q)
    print(*w)
        

        
        
        
