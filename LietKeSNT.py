a=[0]*100001
a[0]=a[1]=1
for i in range(2,100001):
    if a[i]==0:
        j=i*i
        while j<=100000:
            a[j]=1
            j+=i

n=int(input())
s=input()
d=dict()

for i in s.split():
    if i in d:
        pass
    elif a[int(i)]==0:
        count=0
        for j in s.split():
            if i==j:
                count+=1
        d[i]=count
        print(i,count)

