n,k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

pre1 = a[0]
pre2 = b[0]
for i in range(n-1):
    if (pre1 != -1 and abs(a[i] - a[i+1]) <= k) or (pre2 != -1 and abs(b[i] - a[i+1]) <= k):
        crr1 = a[i+1]
    else:
        crr1 = -1
        
    if (pre1 != -1 and abs(a[i] - b[i+1]) <= k) or (pre2 != -1 and abs(b[i] - b[i+1]) <= k):
        crr2 = b[i+1]
    else:
        crr2 = -1

    if crr1 == -1 and crr2 == -1:
        print('No')
        exit()
    pre1 = crr1
    pre2 = crr2

        
print('Yes')
