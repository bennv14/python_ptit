a=[0]*10001
a[0]=a[1]=1
prime=[]
for i in range(2,10001):
    if a[i]==0:
        prime.append(i)
        j=i*i
        while j<=10000:
            a[j]=1
            j+=i

n,k=[int(i) for i in input().split()]

print(k,end=' ')
for i in range(n):
    print(k+prime[i],end=' ')
    k+=prime[i]
print()

