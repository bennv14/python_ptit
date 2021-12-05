
number=input()
k=int(input())
dic=dict()
for i in range(0,len(number)-1,2):
    num=int(number[i:i+2])
    if num not in dic: 
        dic[num]=1
    else:
        dic[num]+=1

dic={key:dic[key] for key in sorted(dic.keys()) if dic[key]>=k}

for key in dic.keys():
    print(key,dic[key])

if len(dic)==0:
    print("NOT FOUND")
