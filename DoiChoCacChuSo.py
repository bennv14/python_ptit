
def hoanVi(number):
    num = [n for n in number]
    i = len(num) - 2
    while num[i] <= num[i+1] and i >= 0:
        i-=1
    
    if i == -1:
        return -1

    k = len(num) - 1
    max = num[i]
    while num[k] < num[i]:
        k-=1
    
    num[k],num[i] = num[i], num[k]
    num = num[:i+1] 
    
    return num



# while t > 0:
#     num = [n for n in input()]

num = '123456'
num = [n for n in num]
num = num + [1,2,3]
print(hoanVi('354'))
