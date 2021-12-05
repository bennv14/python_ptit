from typing import Collection, Counter


def TinhTuoi(nam):
    return 2021 - nam

def DemTu(ten):
    return len([string for string in ten.split()])

class SinhVien:
    gioi_tinh = "nu"
    def __init__(self, ten,nam_sinh , gioi_tinh, que_quan, toan, ly, hoa):
        self.ten = ten
        self.nam_sinh = nam_sinh
        self.gioi_tinh = gioi_tinh
        self.que_quan = que_quan
        self.toan = toan
        self.ly = ly
        self.hoa = hoa
        

    def diemTB(self):
        return (self.toan + self.ly + self.hoa)/3
    
    def diemXT(self):
        return self.toan*2 + self.ly + self.hoa

danh_sach = []

danh_sach.append(SinhVien('nguyen van a', 2001, 'nam', 'bac ninh', 9, 9, 9))
danh_sach.append(SinhVien('nguyen van b', 2000, 'nam', 'ha noi', 8, 9, 9))
danh_sach.append(SinhVien('nguyen van c', 2004, 'nam', 'hai duong', 9, 7, 3))
danh_sach.append(SinhVien('nguyen van d', 1999, 'nu', 'hai phong', 5, 7, 9))
danh_sach.append(SinhVien('nguyen van e', 2000, 'nam', 'nghe an', 9, 3, 9))
danh_sach.append(SinhVien('nguyen van f', 1998, 'nu', 'ha tinh', 6, 9, 9))
danh_sach.append(SinhVien('nguyen van g', 1997, 'nam', 'thanh hoa', 9, 8, 7))
danh_sach.append(SinhVien('nguyen van h', 2003, 'nam', 'ha nam', 7, 9, 5))
danh_sach.append(SinhVien('nguyen van i', 2001, 'nu', 'lao cai', 8, 8, 8))
danh_sach.append(SinhVien('nguyen van j', 2001, 'nam', 'thai nguyen', 6, 7, 6))

print("in ra ten va tuoi:")
for sv in danh_sach:
    print(f'{sv.ten}: {TinhTuoi(sv.nam_sinh)}')

print('\n in ra ten va diem tb:')


danh_sach = sorted(danh_sach, key=lambda SinhVien : (SinhVien.toan+SinhVien.ly+SinhVien.hoa)/3)

for sv in danh_sach:
    print(sv.ten + ": " + "{:.2f}".format((sv.toan + sv.ly + sv.hoa)/3))

count = 0
for sv in danh_sach:
    if(sv.gioi_tinh == 'nu'):
        count+=1

print(f'so sinh vien nu la: {count}')

print(f'nam: {len(danh_sach) - count} nu: {count}')

for sv in danh_sach:
    print(f'{sv.ten}: {DemTu(sv.ten)}')

danh_sach = sorted(danh_sach, key=lambda sv : -sv.diemXT())
for sv in danh_sach:
    print(sv.ten,sv.diemXT())

