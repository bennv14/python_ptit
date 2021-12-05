t= int(input())
dic=dict()
while t>0:
    t-=1
    string = input()
    key=''
    for char in string:
        if char.isalpha():
            key+=char
        elif len(key)>0:
            key=key.lower()
            if key in dic:
                dic[key]+=1
            else:
                dic[key] = 1
            
            key=''

    key=key.lower()
    if key in dic :
        if len(key) > 0:
            dic[key]+=1
    else :
        if len(key) > 0:
            dic[key] = 1
dic=dict(sorted(dic.items(),key=lambda item: (-item[1],item[0])))

for key in dic.keys():
    if key.isalpha():
        print(key,dic[key])

