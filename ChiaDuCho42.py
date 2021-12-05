a=[]
while len(a)<10:
    a+=[int(i) for i in input().split(' ')]

du=set()
count=0
for i in a:
    du.add(i%42)

print(len(du))