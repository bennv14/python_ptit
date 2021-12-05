sandwich_orders = ['banh mi ga', 'banh mi thit nuong', 'banh mi dan to', 'banh mi pate', 'banh mi pastrami', 'banh mi xuc xich']
index = 0
while index < len(sandwich_orders):
    if sandwich_orders[index].__contains__('pastrami'):
        del sandwich_orders[index]
        index-=1
   
    index+=1

for sandwich in sandwich_orders:
    print(sandwich)