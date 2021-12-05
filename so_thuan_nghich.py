
def chuyen_co_so(num, he_so):
    res = []
    while num > 0:
        res.append(int(num%he_so))
        num = int(num/he_so)

    return res

def thuan_nghich(number):
    return number[0:int(len(number)/2)]==number[len(number):int(len(number)/2) + 1:-1]


a,b,M = [int(i) for i in input().split()]
res = 0
for num in range(a,b+1):
    if thuan_nghich(chuyen_co_so(num, M)) == True:
        res +=1

print(res)