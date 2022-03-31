n = int(input())
a = list(map(int, input().split()))

backet = [0]*2001
for i in range(n):
    backet[a[i]] = 1
    
for i in range(2001):
    if backet[i] == 0:
        print(i)
        exit()
