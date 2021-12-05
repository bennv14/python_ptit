t=int(input())
while t>0:
    
    n=int(input())
    s=input()
    arr=[]
    for i in s.split():
        arr.append(int(i))

    arr.sort()
    before=-1
    count=0
    result=0
    time=0


    for i in arr:
        if i==before:
            count+=1
        else:
            if count>time:
                time=count
                result=before
            count=1
            before=i

    if count>time:
        time=count
        result=before

    if(time>=n/2):
        print(result)
    else:
        print('NO')
    
    t-=1

