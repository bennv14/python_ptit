import math

def f1(string):
    hoa = 0
    thuong = 0
    for char in string:
        if char.isupper():
            hoa+=1
        elif char.islower():
            thuong+=1

    return hoa,thuong

def f2(list):
    res = set(list)
    return sorted(res)

def isPrime(number):
    if(number<2):
        return False
    else:
        for i in range(2,int(math.sqrt(number))+1):
            if number%i==0:
                return False
        
        return True
    
def f4(string):
    return string[::-1]

def f5(list):
    return max(list)

def f6(string):
    list = [s for s in string.split()]
    res = ' '.join(list)
    
    return res

print(f6('skdf sdkf klf wselfm lkv'))