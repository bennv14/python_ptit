while True:
    n=int(input())
    if(n==0):
        break
    giaTri=set()
    giaTri.add(n)
    while n!=1:
        if n%2==0:
            n/=2
        else:
            n=n*3+1

        giaTri.add(n)

    print(len(giaTri))


