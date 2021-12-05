t=int(input())
while t>0:
    t-=1
    string=input()
    money,interest,getMoney=[float(i) for i in string.split(' ')]
    
    year=0
    while money<=getMoney:
        money=money*(1+interest/100)
        year+=1

    print(year)