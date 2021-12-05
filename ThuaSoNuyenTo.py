import math
t=int(input())
while t>0:
    t-=1
    n=int(input())
    s="1"
    while n>0:
        count=0;
        while n%2==0:
            count+=1
            n/=2;

        if count>0:
            s+=" * 2^"+str(count)

        for i in range(3,int(math.sqrt(n)+1),2):
            count=0
            while n%i==0:
                n/=i
                count+=1
            if count>0:
                s+=" * "+str(i)+"^"+str(count)

        if n>1:
            s+=" * "+str(int(n))+"^"+str(1)
            n=1
        break

    print(s)



    