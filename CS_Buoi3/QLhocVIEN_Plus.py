#người dùng nhập thông tin học viên và thực hiện đăng ký khóa học

class KhoaHoc:
    def __init__(self, maKhoaHoc, tenKhoaHoc, hinhThuc, hocPhi):
        self.maKhoaHoc = maKhoaHoc
        self.tenKhoaHoc = tenKhoaHoc
        self.hinhThuc = hinhThuc
        self.hocPhi = hocPhi

    def thongTinKhoaHoc(self):
        return f"Mã KH: {self.maKhoaHoc}, Tên KH: {self.tenKhoaHoc}, Hình thức: {self.hinhThuc}, Học phí: {self.hocPhi}"

class HocVien:
    def __init__(self, maHV, tenHV, ngaySinh):
        self.maHV = maHV
        self.tenHV = tenHV
        self.ngaySinh = ngaySinh
        self.khoaHoc = []

    def dangKyKhoaHoc(self, khoaHoc):
        self.khoaHoc.append(khoaHoc)

    def hienThiKhoaHoc(self):
        print(f"Danh sách khóa học của {self.tenHV}:")
        for khoa in self.khoaHoc:
            print(f" - {khoa.thongTinKhoaHoc()}")


danhSachKhoaHoc = [
    KhoaHoc("KH01", "Python cơ bản", "Online", 2000000),
    KhoaHoc("KH02", "Python nâng cao", "Offline", 3000000),
]

def nhapThongTinHocVien():
    maHV = input("Nhập mã học viên: ")
    tenHV = input("Nhập tên học viên: ")
    ngaySinh = input("Nhập ngày sinh (dd/mm/yyyy): ")
    return HocVien(maHV, tenHV, ngaySinh)

def dangKyKhoaHocChoHocVien(hocVien):
    print("\nDanh sách khóa học có sẵn:")
    for idx, khoaHoc in enumerate(danhSachKhoaHoc):
        print(f"{idx + 1}. {khoaHoc.thongTinKhoaHoc()}")

    while True:
        chon = input("Chọn khóa học để đăng ký (nhập số, 0 để thoát): ")
        if chon == "0":
            break
        try:
            chon = int(chon)
            if 1 <= chon <= len(danhSachKhoaHoc):
                hocVien.dangKyKhoaHoc(danhSachKhoaHoc[chon - 1])
                print("Đăng ký thành công!")
            else:
                print("Lựa chọn không hợp lệ!")
        except ValueError:
            print("Vui lòng nhập số hợp lệ!")

print("=== HỆ THỐNG QUẢN LÝ HỌC VIÊN ===")
hocVien = nhapThongTinHocVien()
dangKyKhoaHocChoHocVien(hocVien)

print("\nKết quả:")
hocVien.hienThiKhoaHoc()
