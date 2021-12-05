def TongChuSo(number):
    sum=0
    for i in number:
        sum+=int(i)

    return sum;



t=int(input())
while t>0:
    t-=1
    n=int(input())
    dict=dict()
    string=input()
    for i in string.split(" "):
        dict[TongChuSo(i)]=i

    key=[i for i in dict]
    key.sort()
    for i in key:
        print(dict[i],end=" ")

    print()
    

