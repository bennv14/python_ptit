import math
def prime(n):
    if n<2:
        return False
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                return False
        
        return True


x,y=input().split()
y=int(y)
x=int(x)
i=0
a=[]
while i<y:
    i+=1
    s=input()
    a.append(s)

i=0
while i<y:
    
    for number in a[i].split():
        if prime(int(number)):
            print(1,end=' ')
        else:
            print(0,end=' ')

    print()
    i+=1
        


