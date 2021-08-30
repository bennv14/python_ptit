t=int(input())
while t>0:
    t-=1
    number=input()
    du=0
    result=''
    for i in range(len(number)-1,0,-1):
        if int(number[i])+du>=5:
            du=1
        else:
            du=0
        result+='0'
        

    result=str(int(number[0])+du)+result
    print(result)