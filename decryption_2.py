p="ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    s=input()
    if s=='0':
        break
    k,s=s.split()
    k=int(k)
    a=list(s.encode('ascii'))
    i=len(a)-1
    result=''
    while(i>=0):
        if a[i]==95:
            a[i]=91
        if a[i]==46:
            a[i]=92
        result+=p[(a[i]+k-65)%28]
        i-=1
    print(result)
