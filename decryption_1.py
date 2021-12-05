t=int(input())
while t>0:
    t-=1
    s=input()
    result=''
    char=''
    time=0
    for i in s:
        if char==i:
            time+=1
        else:
            if time>0:
                result+=str(time)+char
            time=1
            char=i
    result+=str(time)+char
    print(result)
    
