m=0
def make(i,n,result):
    if i==n:
        if int(result+result[::-1])>=m:
            return
        print(result+result[::-1],end=' ')
    else:
        for j in range(0,10,2):
            #make(i+1,n,result+str(j))
            if i==0 and j!=0:
                make(i+1,n,result+str(j))
            elif i>0:
                make(i+1,n,result+str(j))

t=int(input())
while t>0:
    t-=1
    m=int(input())
    length=len(str(m))
    length=int(length/2)+1
    for i in range(1,length):
        result = ''
        make(0,i,result)

    print()