import math

def uocSoCuaGiaiThua(number, n):
    res=0
    for num in range(n,number+1,n):
        while num%n==0:
            res+=1
            num/=n

    return res

def isReversible(number):
    number=str(number)
    n=len(number)
    for i in range(int(n/2)+1):
        if number[i]!=number[n-i-1]:
            return False;
    return True

def phanChiaNT(arrays):
    n=len(arrays)
    sum1=0
    for i in range(n):
        sum1+=arrays[i]
        if isPrime(sum1):
            sum2=0
            for j in range(i+1,n):
                sum2+=arrays[j]
            
            if isPrime(sum2):
                    return i

    return 'NOT FOUND'

def khoiPhucDaySo(matrix):
    result=[]
    result.append(int((matrix[0][1]+matrix[0][2]-matrix[1][2])/2))
    for i in range(1,len(matrix)):
        result.append(matrix[0][i]-A[0])

    return result

def soLocPhat(number):
    count=0
    for i in number:
        if i=='6':
            count=0
        elif i=='8':
            count+=1
            if count>=3:
                return False
        else:
            return False

    return True

def sxChanLe(arr,odd,even):
    odd.sort()
    odd=odd[::-1]
    even.sort()
    index_odd=0
    index_even=0
    for i in arr:
        if i%2==0:
            print(even[index_even],end=' ')
            index_even+=1
        else:
            print(odd[index_odd],end=' ')
            index_odd+=1

def convert(number,base):
    result=''
    while number:
        remainder=number%base
        if remainder>=10:
            result+=chr(64+remainder-9)
        else:
            result+=str(remainder)

        number//=base

    return result[::-1]

def demCapDongXu(matrix):
    count=0
    n=len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j]=='C':
                for k in range(i+1,n):
                    if matrix[k][j]=='C':
                        count+=1

                for k in range(j+1,n):
                    if matrix[i][k]=='C':
                        count+=1

    return count

def tongChuSo2(number):
    count=0
    while len(number)>1:
        tong=0
        for i in number:
            tong+=(ord(i)-ord('0'))

        number=str(tong)
        count+=1

    return count

def dayConChung(list1,list2,list3):
    boolean=False
    n=[0,len(list1),len(list2),len(list3)]
    n1,n2,n3=0,0,0
    while n1<n[1] and n2<n[2] and n3<n[3]:
        if list1[n1]<max(list2[n2],list3[n3]) :
            n1+=1
            if(n1>=n[1]):
                break
        if list2[n2]<max(list1[n1],list3[n3]) :
            n2+=1
            if(n2>=n[2]):
                break
        if list3[n3]<max(list1[n1],list2[n2]) :
            n3+=1
            if(n3>=n[3]):
                break

        if list1[n1]==list2[n2]==list3[n3]:
            print(list1[n1],end=" ")
            n1+=1
            n2+=1
            n3+=1
            boolean=True
   
    if boolean:
        print()
    else:
        print('NO')

def tanSuatLe(list):
    list.sort()
    num=list[0]
    count=0
    for i in list:
        if num==i:
            count+=1
        else:
            if count%2==1:
                return num
                break
            else:
                num=i
                count=1
    return num

def tongCacChuSo(list):
    n=len(list)
    list.sort()
    tong=0
    for i in list:
        if i.isdigit():
            tong+=int(i)
        else:
            print(i,end='')

    print(tong)

def mtCanDoi(list,k):
    tongTren=0
    tongDuoi=0
    n=len(list)
    for i in range(0,n):
        for j in range(0,n):
            if j<n-i-1:
                tongTren+=list[i][j]
            elif j>n-i-1:
                tongDuoi+=list[i][j]

    res=abs(tongTren-tongDuoi)
    if res<=k:
        print("YES")
    else:
        print("NO")

    print(res)

def tongPhanThuc(n):
    if(n%2==0):
        tong=0
        for i in range(2,n+1,2):
            tong+=1/i

        return tong
    else:
        tong=1
        for i in range(3,n+1,2):
            tong+=1/i

        return tong

def bo3NT(left,right,i,tup):
    if i==3:
        if(math.gcd(tup[0], tup[1])==math.gcd(tup[0],tup[2])==math.gcd(tup[1], tup[2])==1):
            print(tup)
    else:
        for j in range(left,right+1):            
            bo3NT(j+1, right, i+1, tup+(j,))

def nguyenToCungNhau(number,k,i,num,a):
    if i==int(k):
        if math.gcd(int(number), num)==1:
            a.append(num)
    else:
        for j in range(0,10):
            if i==0 and j!=0:
                nguyenToCungNhau(number, k, i+1, num*10+j,a)
            elif i>0:
                nguyenToCungNhau(number, k, i+1, num*10+j,a)
            
def soDaoNTCungNhau(number):
    gcd=math.gcd(int(number),int(number[::-1]))
    if gcd==1:
        return True
    return False

def uuTheNT(number):
    n=len(number)
    if isPrime(n)==False:
        return False
    else:
        countPrime=0
        for i in number:
            if isPrime(int(i)):
                countPrime+=1

        if 2*countPrime>n:
            return True
        
        return False

def dauCuoiNT(number):
    if isPrime(int(number[:3])) and isPrime(int(number[-3:])):
        return True

    return False

def tongChuSoLe(number):
    tong=0
    for i in range(1,len(number),2):
        tong+=int(number[i])

    return tong

def tichChuSoChan(number):
    tich=1
    check=False
    for i in range(0,len(number),2):
        if number[i]!='0':
            tich*=int(number[i])
            check=True

    if check==False:
        return 0
    else:
        return tich

def tichChuSole(number):
    tich=1
    check=False
    for i in range(1,len(number),2):
        if number[i]!='0':
            tich*=int(number[i])
            check=True

    if check==False:
        return 0
    else:
        return tich

def tongChuSoChan(number):
    tong=0
    for i in range(0,len(number),2):
        tong+=int(number[i])

    return tong

def doanCuoiNT(number):
    if isPrime(int(number[-4:])):
        return True
    
    return False

def viTriNT(number):
    n=len(number)
    for i in range(0,n):
        if isPrime(i) and isPrime(int(number[i]))==False:
            return False
        if isPrime(i)==False and isPrime(int(number[i])):
            return False

    return True

def chanLeNT(number):
    n=len(number)
    sum=0
    for i in range(0,n):
        num_i=int(number[i])
        sum+=num_i
        if i%2==0 and num_i%2==1:
            return False
        if i%2==1 and num_i%2==0:
            return False

    if isPrime(sum):
        return True
    else:
        return False
        
def soXenKe(number):
    n=len(number)
    if n%2==0 or number[0]==number[1]:
        return False

    for i in range(2,n,2):
        if number[i]!=number[i-2]:
            return False
    return True

def tichChuSo(number):
    tich=1
    for i in number:
        if i!='0':
            tich*=int(i)

    return tich

def tongChuSo(number):
    tong=0
    for i in number:
        tong+=int(i)

    return tong

def isPrime(number):
    if(number<2):
        return False
    else:
        for i in range(2,int(math.sqrt(number))+1):
            if number%i==0:
                return False
        
        return True

def ptYesOrNo(boolean):
    if boolean:
        print("YES")
    else:
        print("NO")

t=int(input())
while t>0:
    t-=1
    n=[int(i) for i in input().split()]
    list1=[int(i) for i in input().split()]
    list2=[int(i) for i in input().split()]
    list3=[int(i) for i in input().split()]
    dayConChung(list1, list2, list3)
