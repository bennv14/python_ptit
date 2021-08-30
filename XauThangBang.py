t=int(input())
while t>0:
    t-=1
    s=input()
    a=list(s.encode('ascii'))
    n=len(s)
    i=1;
    check=True
    while i<=n/2:
        if abs(a[i]-a[i-1])!=abs(a[n-i-1]-a[n-i]):
            check=False
            break
        i+=1

    if check:
        print("YES")
    else:
        print('NO')