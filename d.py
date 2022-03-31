n,m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))

a.reverse()
c.reverse()

b = []
for i in range(m+1):
    sho = c[i]//a[0]
    b.append(sho)
    for j in range(i,n+m+1):
        if j-i <= n:
            c[j] = c[j] - a[j-i]*sho
        else:
            break
            
b.reverse()
print(*b, sep=' ')
