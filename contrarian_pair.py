n=int(input())
s=input()
arr=[]
for i in s.split(' '):
    arr.append(i)

count=0

for i in range(0,n-1):
    for j in range(i+1,n):
        if int(arr[i])>int(arr[j]):
            count+=1

print(count)