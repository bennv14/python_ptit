t=int(input())
while t>0:
    t-=1
    n=int(input())
    d=dict()
    gt=0
    ten=0
    while n>0:
        n-=1
        x=int(input())
        if x not in d:
            d[x]=1
        else:
            d[x]=d[x]+1

        if d[x]>gt:
            ten=x
            gt=d[x]
        elif d[x]==gt and ten>x:
            ten=x
    
    print(ten)
