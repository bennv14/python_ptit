while True:
    s=input()
    if(s=='0 0 0 0'):
        break
    a,b,c,d=s.split()
    a=int(a)
    b=int(b)
    c=int(c)
    d=int(d)
    a_past=a
    count=0

    while True:
        if a==b and b==c and c==d:
            break
        a=abs(a-b)
        b=abs(b-c)
        c=abs(c-d)
        d=abs(d-a_past)
        a_past=a
        count+=1
        

    print(count)