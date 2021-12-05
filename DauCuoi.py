t=int(input())
while t>0:
    t-=1
    s=input()
    if s[0:2]==s[-2:]:
        print("YES")
    else:
        print('NO')