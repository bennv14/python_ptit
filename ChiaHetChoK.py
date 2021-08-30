a,K,N=[int(i) for i in input().split()]
have=False
i=1
while i*K<=N :
    b=i*K-a
    if b>0:
        print(b,end=' ')
        have=True
    i+=1

if have==False:
    print(-1)
else:
    print()