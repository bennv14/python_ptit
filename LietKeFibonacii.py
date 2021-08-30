t=int (input())
fi=[0,1,1]
for i in range(3,200):
    fi.append(fi[i-1]+fi[i-2])
while t>0:
    t-=1
    a,b=[int(i) for i in input().split()]

    for i in range(a,b+1):
        print(fi[i],end=' ')
    print()
