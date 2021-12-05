A = ord('A')
bang = dict((chr(i), i - A) for i in range(ord('A'), ord('Z') + 1))
        
def DRM(string):
    n = len(string)
    str1 = string[0:int(n/2)]
    str2 = string[int(n/2):n]
    tong1, tong2 = 0, 0
    res = [0]*int(n/2)
    for (chr1,chr2,i) in zip(str1,str2,range(int(n/2))):
        tong1 += bang[chr1]
        tong2 += bang[chr2]
        res[i] += bang[chr1] + bang[chr2]

    result = ''
    for num in res:
        num += tong1 + tong2
        num %= 26
        result += chr(num + A)

    return result
    

t = int(input())
while t > 0:
    t-=1
    print(DRM(input()))

    
"""
3
EWPGAJRB
BB
TPQJDRJWSQXGRRIPXFMINTELHBJA
"""