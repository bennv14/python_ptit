def tongChuSo(number):
    tong=0
    for i in number:
        tong+=int(i)

    return tong

def ktThuanNghich(number):
    if(number<10):
        return False
    num=str(number)
    n=len(num)
    for i in  range(int(n/2)):
        if num[i]!=num[n-i-1]:
            return False
    
    return True

t=int(input())
while t>0:
    t-=1
    number=input()
    check=ktThuanNghich(tongChuSo(number))
    if check:
        print('YES')
    else:
        print('NO')