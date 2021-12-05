import math
t=int(input())
while t>0:
    t-=1
    string=input();
    sum=0
    i_past=-1
    check=True
    for i in string:
        num=int(i)
        sum+=num
        if(i_past==-1):
            i_past=num
        else:
            if abs(num-i_past)!=2:
                check=False
                break
            i_past=num
            
    
    if sum%10!=0:
        check=False
    
    if check:
        print("YES")
    else:
        print("NO")

    

