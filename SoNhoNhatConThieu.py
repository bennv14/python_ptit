t=int(input())
a=[i for i in input().split(' ')]
count=0
x=a[0]
for i in range(1,len(a)):
    if x !=a[i]:
        count+=1
    
    x=a[i]

print(count)

