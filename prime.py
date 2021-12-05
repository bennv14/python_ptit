import math
def isPrime(n):
    if n<2:
        return False
    elif n==2 or n==3:
        return True
    else:
        for i in range(2,int(math.sqrt(n)+1)):
            if n%i==0:
                return False

        return True

t=int(input())
while t>0:
    t-=1
    count=0
    n=int(input())
    for i in range(1,n):
        if math.gcd(i,n)==1:
            count+=1

    if isPrime(count):
        print('YES')
    else:
        print('NO')