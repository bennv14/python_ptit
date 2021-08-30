t=int(input())
while(t>0):
    t-=1
    n=int(input())
    arr1=[]
    arr2=[]
    s1=input()

    for i in s1.split(' '):
        arr1.append(int(i))

    s2=input()

    for i in s2.split(' '):
        arr2.append(int(i))

    arr1.sort()
    arr2.sort()

    check=True
    for i,j in arr1,arr2:
        if i>j:
            check=False
            break

    if check:
        print('YES')
    else:
        print('NO')