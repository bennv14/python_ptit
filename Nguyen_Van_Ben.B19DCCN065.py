#6-1
ten_xe = input("ban muon xe gi: ")
print('de xem chung toi con xe' + ten_xe + 'khong nha. roi chung toi se bao lai')

#6-2
so_cho = int(input("so cho ban muon dat: "))
if so_cho > 8:
    print('xin loi ban can cho de chung toi tim ban cho ban')
else :
    print('ban cua ban da san sang')

#6-3
number = int(input('nhap so: '))
if number%10 == 0:
    print(number , "la boi so cua 10")
else :
    print(number , "k phai boi so cua 10")

#6-4
while True:
    topping = input('nhap ten lop phu banh: ')
    if topping == 'quit':
        break
    else:
        print('da them ' + topping + " vao banh")

#6-5
tuoi = int(input('nhap so tuoi : '))
if tuoi < 3:
    print('mien phi')
elif tuoi <= 12:
    print('giá vé là 10$')
else:
    print('giá vé là 15$')

#6-6
active = 10
while active > 0:
    active -=1
    topping = input('nhap ten lop phu banh: ')
    if topping == 'quit':
        break
    else:
        print('da them ' + topping + " vao banh")

active = 10
while active > 0:
    tuoi = input('nhap so tuoi: ')
    if tuoi == 'quit':
        break;

    tuoi = int(tuoi)
    if tuoi < 3:
        print('mien phi')
    elif tuoi <= 12:
        print('giá vé là 10$')
    else:
        print('giá vé là 15$')

#6-7
"""
while True:
    pass
"""
#6-8
sandwich_orders = ['banh mi ga', 'banh mi thit nuong', 'banh mi dan to', 'banh mi pate', ' banh mi xuc xich']
finish_sandwiches = []
for sandwich in sandwich_orders:
    print('da lm xong '+ sandwich_orders)
    finish_sandwiches.append(sandwich)

print('sandwich da duoc lam la:')
for sandwich in finish_sandwiches:
    print(sandwich)

#6-9
print('cua hang het pastrami')
index = 0
while index < len(sandwich_orders):
    if sandwich_orders[index].__contains__('pastrami'):
        del sandwich_orders[index]
        index-=1;
    index+=1

for sandwich in sandwich_orders:
    print(sandwich)
#6-10
dia_diem = input('ki nghi nghi mo uoc cua ban o dau')
print(dia_diem)

#7-1
def display_message():
    print('minh dang hoc python')

#7-2
def favourite_book(name_book):
    print('cuon sach yeu thich cua toi la '+name_book);

#7-3
def make_shirt(kich_thuoc, noi_dung):
    print('size ao la '+ kich_thuoc + ' noi dung la ' + noi_dung)

#7-4
def make_shirt(kich_thuoc='M',noi_dung='toi yeu python'):
    print('size ao la '+ kich_thuoc + ' noi dung la ' + noi_dung)

make_shirt()
