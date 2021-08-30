t=int(input())
while(t>0):
    t-=1
    string=input()

    s=''
    result=''
    time=0
    stack=[]
    for i in string:
        if i.isalpha():
            if len(stack)>0:
                result+=stack.pop()*time
            s+=i
            time=0
            
        elif i.isalpha()==False:
            if len(s)>0:
                stack.append(s)
                s=''
            time=time*10+int(i)

    result+=stack.pop()*time

    print(result)