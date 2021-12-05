def delColumn(matrix):
    i=0
    while len(matrix)!=len(matrix[0]):
        del matrix[i]
        i+=1
        
def delRow(matrix):
    j=1
    while len(matrix)!=len(matrix[0]):
        for i in range(len(matrix)):
            del matrix[i][j]

        j+=1

def convertMaTranVuong(matrix):
    if len(matrix)>len(matrix[0]):
        delColumn(matrix)
    else :
        delRow(matrix)

def Print(matrix):
    for arr in matrix:
        for num in arr:
            print(num,end=' ')
        print()
    print()

n,m=[int(i) for i in input().split()]
matrix=[]
while n>0:
    n-=1
    matrix.append([int(i) for i in input().split()])

convertMaTranVuong(matrix);

Print(matrix)



