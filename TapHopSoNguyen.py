def tapGiao(array1,array2):
    result=[]
    for i in array1:
        if i in array2:
            result.append(i)
        
    result.sort()
    return result

def tapKhac(array1,array2):
    result=[]
    for i in array1:
        if i not in array2:
            result.append(i)

    result.sort()
    return result

n,m=[int(i) for i in input().split()]
array1=[int(i) for i in input().split()]
array2=[int(i) for i in input().split()]
A=set(array1)
B=set(array2)
for i in tapGiao(A,B):
    print(i,end=' ')
print()
for i in tapKhac(A, B):
    print(i,end=' ')
print()
for i in tapKhac(B, A):
    print(i,end=' ')
print()
