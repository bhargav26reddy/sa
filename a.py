n,m=map(int,input().split())
a=[]
b=[]
for i in range(n):
    k=int(input())
    a.append(k)
print(a)
for j in range(m):
        z,y=map(int,input().split())
        sum=0
        for g in range(z,y+1):
            sum+=a[g]
        b.append(sum)
for h in b:
    print(h)
