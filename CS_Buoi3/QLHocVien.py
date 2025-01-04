class KhoaHoc:
    def __init__(self, maKhoaHoc, tenKhoaHoc, hinhThuc, hocPhi):
        self.maKhoaHoc = maKhoaHoc
        self.tenKhoaHoc = tenKhoaHoc
        self.hinhThuc = hinhThuc
        self.hocPhi = hocPhi
        
    def thongTinKhoaHoc(self):
        return f"Mã khóa học : {self.maKhoaHoc}, tên khóa học: {self.tenKhoaHoc}, hình thức : {self.hinhThuc}, học phí: {self.hocPhi}"
        
class HocVien:
    def __init__(self, maHV, tenHV, ngaySinh, khoaHoc):
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
                
khoaHoc1 = KhoaHoc("PY001", "PYTHON cơ bản", "online", 1000)
khoaHoc2 = KhoaHoc("PY001", "PYTHON nâng cao", "offline", 5000)

hocVien1 = HocVien("A001", "Phạm Khôi", "23/07/2002", [])
hocVien2 = HocVien("A002", "Khôi Phạm", "23/07/2002", [])

hocVien1.dangKyKhoaHoc(khoaHoc1)
hocVien1.dangKyKhoaHoc(khoaHoc2)

hocVien2.dangKyKhoaHoc(khoaHoc2)

hocVien1.hienThiKhoaHoc()
hocVien2.hienThiKhoaHoc()
