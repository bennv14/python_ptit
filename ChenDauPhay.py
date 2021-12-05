t=1
while t>0:
    t-=1
    string = input()
    i=len(string)
    result=""
    while i>3:
        result=","+string[i-3:i]+result
        i-=3
    if i>0:
        result=string[0:i]+result
    print(result)
