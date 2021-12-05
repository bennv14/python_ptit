t = int(input())
l = []
while t > 0:
    t-=1
    string = input()
    so = False
    num = 0
    for chr in string:
        if chr.isdigit():
            num = num*10 + int(chr)
            so = True
        else:
            if so == True:
                l.append(num)
                num = 0
                so = False
    
    if so == True:
        l.append(num)

l.sort()
for num in l:
    print(num)
