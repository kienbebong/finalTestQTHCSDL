import tkinter as tk
from tkinter import ttk, messagebox
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from datetime import datetime
# Khởi tạo cơ sở dữ liệu và khung mẫu ORM
Base = declarative_base()

# Định nghĩa các thực thể trong cơ sở dữ liệu
class BorrowingTicket(Base):
    __tablename__ = 'borrowing_ticket'
    ma_phieu_muon = Column(Integer, primary_key=True, autoincrement=True)
    ma_doc_gia = Column(String, ForeignKey('the_doc_gia.ma_doc_gia', ondelete='CASCADE', onupdate='CASCADE'))
    ma_thu_thu = Column(String, ForeignKey('thu_thu.ma_thu_thu', ondelete='CASCADE', onupdate='CASCADE'))
    ma_dau_sach = Column(String, ForeignKey('dau_sach.ma_dau_sach', ondelete='CASCADE', onupdate='CASCADE'))
    so_ngay_muon = Column(Integer)


# Định nghĩa lớp ORM cho bảng DauSach
class DauSach(Base):
    __tablename__ = 'dau_sach'
    ma_dau_sach = Column(String, primary_key=True)
    ten_dau_sach = Column(String)
    nha_xuat_ban = Column(String)
    so_trang = Column(Integer)
    kich_thuoc = Column(String)
    tac_gia = Column(String)
    so_luong_sach = Column(Integer)
    ma_chuyen_nganh = Column(String, ForeignKey('chuyen_nganh.ma_chuyen_nganh'))
    
    # Mối quan hệ với bảng PhieuMuon
    phieu_muons = relationship('PhieuMuon', back_populates='dau_sach', cascade='all, delete-orphan')

class ChuyenNganh(Base):
    __tablename__ = 'chuyen_nganh'
    ma_chuyen_nganh = Column(String, primary_key=True)
    ten_chuyen_nganh = Column(String)
    mo_ta = Column(String)

class TheDocGia(Base):
    __tablename__ = 'the_doc_gia'
    ma_doc_gia = Column(String, primary_key=True)
    ho_ten = Column(String)
    ngay_sinh = Column(Date)
    gioi_tinh = Column(String)
    cmnd = Column(String)
    the_hoc_sinh = Column(String)

class PhieuMuon(Base):
    __tablename__ = 'phieu_muon'
    ma_phieu_muon = Column(Integer, primary_key=True, autoincrement=True)
    ma_doc_gia = Column(String, ForeignKey('the_doc_gia.ma_doc_gia', ondelete='CASCADE', onupdate='CASCADE'))
    ma_thu_thu = Column(String, ForeignKey('thu_thu.ma_thu_thu', ondelete='CASCADE', onupdate='CASCADE'))
    ma_dau_sach = Column(String, ForeignKey('dau_sach.ma_dau_sach', ondelete='CASCADE', onupdate='CASCADE'))
    ngay_muon = Column(Date)
    ngay_tra = Column(Date, nullable=True)
    
    # Mối quan hệ với bảng DauSach
    dau_sach = relationship('DauSach', back_populates='phieu_muons')


class ThuThu(Base):
    __tablename__ = 'thu_thu'
    ma_thu_thu = Column(String, primary_key=True)
    ho_ten = Column(String)
    chuc_nang = Column(String)



# Tạo cơ sở dữ liệu và bảng dữ liệu
db_directory = '/Users/dinhchikien/Desktop/finalTestQTHCSDL'
engine = create_engine(f'sqlite:///{db_directory}/finalTest.db')
Base.metadata.create_all(engine)

# Tạo phiên giao dịch để làm việc với cơ sở dữ liệu
Session = sessionmaker(bind=engine)
session = Session()

# Tạo đối tượng BorrowingTicket
borrowing_tickets = [
    BorrowingTicket(ma_dau_sach="DS001", ma_doc_gia="DG001", ma_thu_thu="TT001", so_ngay_muon=30),
    BorrowingTicket(ma_dau_sach="DS002", ma_doc_gia="DG002", ma_thu_thu="TT002", so_ngay_muon=20),
    BorrowingTicket(ma_dau_sach="DS003", ma_doc_gia="DG003", ma_thu_thu="TT003", so_ngay_muon=25),
    BorrowingTicket(ma_dau_sach="DS004", ma_doc_gia="DG004", ma_thu_thu="TT004", so_ngay_muon=15)
]

# Tạo đối tượng ChuyenNganh
chuyen_nganhs = [
    ChuyenNganh(ma_chuyen_nganh="CN001", ten_chuyen_nganh="Computer Science", mo_ta="Study of computers and computational systems"),
    ChuyenNganh(ma_chuyen_nganh="CN002", ten_chuyen_nganh="Mathematics", mo_ta="Study of numbers, shapes, and patterns"),
    ChuyenNganh(ma_chuyen_nganh="CN003", ten_chuyen_nganh="Physics", mo_ta="Study of matter and energy"),
    ChuyenNganh(ma_chuyen_nganh="CN004", ten_chuyen_nganh="Chemistry", mo_ta="Study of substances and their properties")
]

# Tạo đối tượng TheDocGia
the_doc_gias = [
    TheDocGia(ma_doc_gia="DG001", ho_ten="Nguyen Van A", ngay_sinh=datetime(1990, 1, 1), gioi_tinh="Nam", cmnd="123456789", the_hoc_sinh="Yes"),
    TheDocGia(ma_doc_gia="DG002", ho_ten="Tran Thi B", ngay_sinh=datetime(1992, 2, 2), gioi_tinh="Nu", cmnd="987654321", the_hoc_sinh="No"),
    TheDocGia(ma_doc_gia="DG003", ho_ten="Le Van C", ngay_sinh=datetime(1988, 3, 3), gioi_tinh="Nam", cmnd="456789123", the_hoc_sinh="Yes"),
    TheDocGia(ma_doc_gia="DG004", ho_ten="Hoang Thi D", ngay_sinh=datetime(1995, 4, 4), gioi_tinh="Nu", cmnd="789123456", the_hoc_sinh="No")
]

# Tạo đối tượng ThuThu
thu_thus = [
    ThuThu(ma_thu_thu="TT001", ho_ten="Pham Van E", chuc_nang="Librarian"),
    ThuThu(ma_thu_thu="TT002", ho_ten="Nguyen Thi F", chuc_nang="Assistant Librarian"),
    ThuThu(ma_thu_thu="TT003", ho_ten="Tran Van G", chuc_nang="Archivist"),
    ThuThu(ma_thu_thu="TT004", ho_ten="Le Thi H", chuc_nang="Clerk")
]

# Tạo đối tượng DauSach
dau_sachs = [
    DauSach(ma_dau_sach="DS001", ten_dau_sach="Learn Python Programming", nha_xuat_ban="NXB Tre", so_trang=300, kich_thuoc="15x21 cm", tac_gia="Nguyen Van C", so_luong_sach=10, ma_chuyen_nganh="CN001"),
    DauSach(ma_dau_sach="DS002", ten_dau_sach="Advanced Mathematics", nha_xuat_ban="NXB Giao Duc", so_trang=450, kich_thuoc="16x24 cm", tac_gia="Le Van D", so_luong_sach=15, ma_chuyen_nganh="CN002"),
    DauSach(ma_dau_sach="DS003", ten_dau_sach="Physics for Scientists", nha_xuat_ban="NXB Khoa Hoc", so_trang=500, kich_thuoc="17x25 cm", tac_gia="Tran Van E", so_luong_sach=20, ma_chuyen_nganh="CN003"),
    DauSach(ma_dau_sach="DS004", ten_dau_sach="Organic Chemistry", nha_xuat_ban="NXB Hoa Hoc", so_trang=350, kich_thuoc="18x26 cm", tac_gia="Hoang Thi F", so_luong_sach=25, ma_chuyen_nganh="CN004")
]

# Tạo đối tượng PhieuMuon
phieu_muons = [
    PhieuMuon(ma_doc_gia="DG001", ma_thu_thu="TT001", ma_dau_sach="DS001", ngay_muon=datetime(2024, 5, 1), ngay_tra=datetime(2025, 5, 1)),
    PhieuMuon(ma_doc_gia="DG002", ma_thu_thu="TT002", ma_dau_sach="DS002", ngay_muon=datetime(2024, 5, 2), ngay_tra=datetime(2025, 5, 2)),
    PhieuMuon(ma_doc_gia="DG003", ma_thu_thu="TT003", ma_dau_sach="DS003", ngay_muon=datetime(2024, 5, 3), ngay_tra=datetime(2025, 5, 3)),
    PhieuMuon(ma_doc_gia="DG004", ma_thu_thu="TT004", ma_dau_sach="DS004", ngay_muon=datetime(2024, 5, 4), ngay_tra=datetime(2025, 5, 4))
]

# Thêm các đối tượng vào phiên giao dịch
session.add_all(borrowing_tickets)
session.add_all(chuyen_nganhs)
session.add_all(the_doc_gias)
session.add_all(thu_thus)
session.add_all(dau_sachs)
session.add_all(phieu_muons)

# Commit phiên giao dịch để lưu các thay đổi vào cơ sở dữ liệu
session.commit()


def them_dau_sach():
    ma_dau_sach = entry_ma_dau_sach.get()
    ten_dau_sach = entry_ten_dau_sach.get()
    nha_xuat_ban = entry_nha_xuat_ban.get()
    so_trang = entry_so_trang.get()
    kich_thuoc = entry_kich_thuoc.get()
    tac_gia = entry_tac_gia.get()
    so_luong_sach = entry_so_luong_sach.get()
    ma_chuyen_nganh = entry_ma_chuyen_nganh_sach.get()
    
    if not ma_dau_sach:
        messagebox.showerror("Lỗi", "Mã đầu sách không được để trống")
        return
    
    dau_sach = DauSach(ma_dau_sach=ma_dau_sach, ten_dau_sach=ten_dau_sach, nha_xuat_ban=nha_xuat_ban, so_trang=so_trang, kich_thuoc=kich_thuoc, tac_gia=tac_gia, so_luong_sach=so_luong_sach, ma_chuyen_nganh=ma_chuyen_nganh)
    session.add(dau_sach)
    session.commit()
    messagebox.showinfo("Thành công", "Đã thêm đầu sách thành công")
    hien_thi_dau_sach()

# Hàm sửa thông tin đầu sách
def sua_dau_sach():
    ma_dau_sach = entry_ma_dau_sach.get()
    ten_dau_sach = entry_ten_dau_sach.get()
    nha_xuat_ban = entry_nha_xuat_ban.get()
    so_trang = entry_so_trang.get()
    kich_thuoc = entry_kich_thuoc.get()
    tac_gia = entry_tac_gia.get()
    so_luong_sach = entry_so_luong_sach.get()
    ma_chuyen_nganh = entry_ma_chuyen_nganh_sach.get()
    
    dau_sach = session.query(DauSach).filter_by(ma_dau_sach=ma_dau_sach).first()
    if dau_sach:
        if ten_dau_sach:
            dau_sach.ten_dau_sach = ten_dau_sach
        if nha_xuat_ban:
            dau_sach.nha_xuat_ban = nha_xuat_ban
        if so_trang:
            dau_sach.so_trang = so_trang
        if kich_thuoc:
            dau_sach.kich_thuoc = kich_thuoc
        if tac_gia:
            dau_sach.tac_gia = tac_gia
        if so_luong_sach:
            dau_sach.so_luong_sach = so_luong_sach
        if ma_chuyen_nganh:
            dau_sach.ma_chuyen_nganh = ma_chuyen_nganh
        session.commit()
        messagebox.showinfo("Thành công", "Đã sửa thông tin đầu sách thành công")
        hien_thi_dau_sach()
    else:
        messagebox.showerror("Lỗi", "Không tìm thấy đầu sách")

def xoa_dau_sach():
    # Lấy mã đầu sách từ giao diện người dùng
    ma_dau_sach = entry_ma_dau_sach.get()
    
    # Tìm đầu sách trong cơ sở dữ liệu
    dau_sach = session.query(DauSach).filter_by(ma_dau_sach=ma_dau_sach).first()
    
    if dau_sach:
        # Kiểm tra xem có bất kỳ phiếu mượn nào liên quan đến cuốn sách bị xoá hay không
        phieu_muon_lien_quan = session.query(PhieuMuon).filter_by(ma_dau_sach=ma_dau_sach).all()
        
        if phieu_muon_lien_quan:
            # Nếu có, cập nhật hoặc xoá những phiếu mượn đó
            for phieu_muon in phieu_muon_lien_quan:
                # Xoá phiếu mượn liên quan
                session.delete(phieu_muon)
                hien_thi_phieu_muon()
        
        # Xóa đầu sách khỏi cơ sở dữ liệu
        session.delete(dau_sach)
        session.commit()
        messagebox.showinfo("Thành công", "Đã xóa đầu sách thành công cùng với các phiếu mượn sách liên quan")
        hien_thi_dau_sach()  # Cập nhật giao diện sau khi xóa
    else:
        messagebox.showerror("Lỗi", "Không tìm thấy đầu sách")


# Hàm hiển thị đầu sách trong data gridview
def hien_thi_dau_sach():
    # Xóa tất cả các hàng hiện tại trong Treeview
    dausach_treeview.delete(*dausach_treeview.get_children())

    # Lấy dữ liệu đầu sách từ cơ sở dữ liệu
    dau_sach_list = session.query(DauSach).all()

    # Thêm dữ liệu vào Treeview
    for dau_sach in dau_sach_list:
        dausach_treeview.insert("", tk.END, values=(dau_sach.ma_dau_sach, dau_sach.ten_dau_sach, dau_sach.nha_xuat_ban, dau_sach.so_trang, dau_sach.kich_thuoc, dau_sach.tac_gia, dau_sach.so_luong_sach))

# Hàm thêm phiếu mượn sách
def them_phieu_muon():
    ma_phieu_muon = entry_ma_phieu_muon.get()
    ma_doc_gia = entry_ma_doc_gia_pm.get()
    ma_thu_thu = entry_ma_thu_thu_pm.get()
    ma_dau_sach = entry_ma_dau_sach_pm.get()
    ngay_muon = entry_ngay_muon.get()
    ngay_tra = entry_ngay_tra.get()
    
    # Chuyển đổi ngày mượn và ngày trả thành đối tượng date của Python
    try:
        ngay_muon = datetime.strptime(ngay_muon, '%Y-%m-%d').date() if ngay_muon else None
        ngay_tra = datetime.strptime(ngay_tra, '%Y-%m-%d').date() if ngay_tra else None
    except ValueError:
        messagebox.showerror("Lỗi", "Ngày mượn hoặc ngày trả không hợp lệ. Định dạng phải là YYYY-MM-DD.")
        return
    
    # Tạo đối tượng phiếu mượn sách
    phieu_muon = PhieuMuon(
        ma_phieu_muon=ma_phieu_muon,
        ma_doc_gia=ma_doc_gia,
        ma_thu_thu=ma_thu_thu,
        ma_dau_sach=ma_dau_sach,
        ngay_muon=ngay_muon,
        ngay_tra=ngay_tra
    )
    
    # Thêm phiếu mượn sách vào cơ sở dữ liệu
    session.add(phieu_muon)
    session.commit()
    messagebox.showinfo("Thành công", "Đã thêm phiếu mượn thành công")
    hien_thi_phieu_muon()

# Hàm sửa phiếu mượn sách
def sua_phieu_muon():
    ma_phieu_muon = entry_ma_phieu_muon.get()
    ma_doc_gia = entry_ma_doc_gia_pm.get()
    ma_thu_thu = entry_ma_thu_thu_pm.get()
    ma_dau_sach = entry_ma_dau_sach_pm.get()
    ngay_muon = entry_ngay_muon.get()
    ngay_tra = entry_ngay_tra.get()
    
    # Tìm phiếu mượn sách trong cơ sở dữ liệu
    phieu_muon = session.query(PhieuMuon).filter_by(ma_phieu_muon=ma_phieu_muon).first()
    
    if phieu_muon:
        # Cập nhật thông tin phiếu mượn sách
        if ma_doc_gia:
            phieu_muon.ma_doc_gia = ma_doc_gia
        if ma_thu_thu:
            phieu_muon.ma_thu_thu = ma_thu_thu
        if ma_dau_sach:
            phieu_muon.ma_dau_sach = ma_dau_sach
        if ngay_muon:
            phieu_muon.ngay_muon = datetime.strptime(ngay_muon, '%Y-%m-%d').date() if ngay_muon else None
        if ngay_tra:
            phieu_muon.ngay_tra = datetime.strptime(ngay_tra, '%Y-%m-%d').date() if ngay_tra else None
        
        # Lưu thay đổi vào cơ sở dữ liệu
        session.commit()
        messagebox.showinfo("Thành công", "Đã sửa phiếu mượn thành công")
        hien_thi_phieu_muon()
    else:
        messagebox.showerror("Lỗi", "Không tìm thấy phiếu mượn")

# Hàm xóa phiếu mượn sách
def xoa_phieu_muon():
    ma_phieu_muon = entry_ma_phieu_muon.get()
    
    # Tìm phiếu mượn sách trong cơ sở dữ liệu
    phieu_muon = session.query(PhieuMuon).filter_by(ma_phieu_muon=ma_phieu_muon).first()
    
    if phieu_muon:
        # Xóa phiếu mượn sách khỏi cơ sở dữ liệu
        session.delete(phieu_muon)
        session.commit()
        messagebox.showinfo("Thành công", "Đã xóa phiếu mượn thành công")
        hien_thi_phieu_muon()
    else:
        messagebox.showerror("Lỗi", "Không tìm thấy phiếu mượn")

# Hàm hiển thị phiếu mượn sách trong data gridview
def hien_thi_phieu_muon():
    # Xóa tất cả các hàng hiện tại trong Treeview
    phieu_muon_treeview.delete(*phieu_muon_treeview.get_children())

    # Lấy dữ liệu phiếu mượn sách từ cơ sở dữ liệu
    phieu_muon_list = session.query(PhieuMuon).all()

    # Thêm dữ liệu vào Treeview
    for phieu_muon in phieu_muon_list:
        phieu_muon_treeview.insert("", tk.END, values=(
            phieu_muon.ma_phieu_muon,
            phieu_muon.ma_doc_gia,
            phieu_muon.ma_thu_thu,
            phieu_muon.ma_dau_sach,
            phieu_muon.ngay_muon,
            phieu_muon.ngay_tra
        ))


# Tạo ứng dụng Tkinter
root = tk.Tk()
root.title("Quản lý thư viện")

# Tạo frame chính với Scrollbar để chứa nội dung
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

# Tạo Canvas để thêm Scrollbar
canvas = tk.Canvas(main_frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Tạo thanh Scrollbar và liên kết với Canvas
scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Kết nối Canvas với Scrollbar
canvas.configure(yscrollcommand=scrollbar.set)

# Tạo khung chứa các frame trong Canvas
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor=tk.NW)

# Thiết lập sự kiện để tự động cuộn khi cần thiết
def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox('all'))

frame.bind('<Configure>', on_configure)

# Khung quản lý đầu sách
frame_dau_sach = tk.LabelFrame(frame, text="Quản lý đầu sách")
frame_dau_sach.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Các ô nhập liệu đầu sách
tk.Label(frame_dau_sach, text="Mã đầu sách:").grid(row=0, column=0, sticky='e')
entry_ma_dau_sach = tk.Entry(frame_dau_sach)
entry_ma_dau_sach.grid(row=0, column=1)

tk.Label(frame_dau_sach, text="Tên đầu sách:").grid(row=1, column=0, sticky='e')
entry_ten_dau_sach = tk.Entry(frame_dau_sach)
entry_ten_dau_sach.grid(row=1, column=1)

tk.Label(frame_dau_sach, text="Nhà xuất bản:").grid(row=2, column=0, sticky='e')
entry_nha_xuat_ban = tk.Entry(frame_dau_sach)
entry_nha_xuat_ban.grid(row=2, column=1)

tk.Label(frame_dau_sach, text="Số trang:").grid(row=3, column=0, sticky='e')
entry_so_trang = tk.Entry(frame_dau_sach)
entry_so_trang.grid(row=3, column=1)

tk.Label(frame_dau_sach, text="Kích thước:").grid(row=4, column=0, sticky='e')
entry_kich_thuoc = tk.Entry(frame_dau_sach)
entry_kich_thuoc.grid(row=4, column=1)

tk.Label(frame_dau_sach, text="Tác giả:").grid(row=5, column=0, sticky='e')
entry_tac_gia = tk.Entry(frame_dau_sach)
entry_tac_gia.grid(row=5, column=1)

tk.Label(frame_dau_sach, text="Số lượng sách:").grid(row=6, column=0, sticky='e')
entry_so_luong_sach = tk.Entry(frame_dau_sach)
entry_so_luong_sach.grid(row=6, column=1)

tk.Label(frame_dau_sach, text="Mã chuyên ngành:").grid(row=7, column=0, sticky='e')
entry_ma_chuyen_nganh_sach = tk.Entry(frame_dau_sach)
entry_ma_chuyen_nganh_sach.grid(row=7, column=1)

# Nút thêm, sửa, và xóa cho đầu sách
tk.Button(frame_dau_sach, text="Thêm Đầu Sách", command=them_dau_sach).grid(row=8, column=0, columnspan=2)
tk.Button(frame_dau_sach, text="Sửa Đầu Sách", command=sua_dau_sach).grid(row=9, column=0, columnspan=2)
tk.Button(frame_dau_sach, text="Xóa Đầu Sách", command=xoa_dau_sach).grid(row=10, column=0, columnspan=2)

# Data gridview để hiển thị dữ liệu đầu sách
dausach_treeview = ttk.Treeview(frame, columns=("ma_dau_sach", "ten_dau_sach", "nha_xuat_ban", "so_trang", "kich_thuoc", "tac_gia", "so_luong_sach"), show="headings")
dausach_treeview.heading("ma_dau_sach", text="Mã đầu sách")
dausach_treeview.heading("ten_dau_sach", text="Tên đầu sách")
dausach_treeview.heading("nha_xuat_ban", text="Nhà xuất bản")
dausach_treeview.heading("so_trang", text="Số trang")
dausach_treeview.heading("kich_thuoc", text="Kích thước")
dausach_treeview.heading("tac_gia", text="Tác giả")
dausach_treeview.heading("so_luong_sach", text="Số lượng sách")
dausach_treeview.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Hiển thị dữ liệu lên Treeview ban đầu
hien_thi_dau_sach()

# Khung quản lý phiếu mượn sách
frame_phieu_muon = tk.LabelFrame(frame, text="Quản lý phiếu mượn sách")
frame_phieu_muon.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Các ô nhập liệu phiếu mượn sách
tk.Label(frame_phieu_muon, text="Mã phiếu mượn:").grid(row=0, column=0, sticky='e')
entry_ma_phieu_muon = tk.Entry(frame_phieu_muon)
entry_ma_phieu_muon.grid(row=0, column=1)

tk.Label(frame_phieu_muon, text="Mã độc giả:").grid(row=1, column=0, sticky='e')
entry_ma_doc_gia_pm = tk.Entry(frame_phieu_muon)
entry_ma_doc_gia_pm.grid(row=1, column=1)

tk.Label(frame_phieu_muon, text="Mã thủ thư:").grid(row=2, column=0, sticky='e')
entry_ma_thu_thu_pm = tk.Entry(frame_phieu_muon)
entry_ma_thu_thu_pm.grid(row=2, column=1)

tk.Label(frame_phieu_muon, text="Mã đầu sách:").grid(row=3, column=0, sticky='e')
entry_ma_dau_sach_pm = tk.Entry(frame_phieu_muon)
entry_ma_dau_sach_pm.grid(row=3, column=1)

tk.Label(frame_phieu_muon, text="Ngày mượn:").grid(row=4, column=0, sticky='e')
entry_ngay_muon = tk.Entry(frame_phieu_muon)
entry_ngay_muon.grid(row=4, column=1)

tk.Label(frame_phieu_muon, text="Ngày trả:").grid(row=5, column=0, sticky='e')
entry_ngay_tra = tk.Entry(frame_phieu_muon)
entry_ngay_tra.grid(row=5, column=1)

# Nút thêm, sửa, và xóa cho phiếu mượn sách
tk.Button(frame_phieu_muon, text="Thêm Phiếu Mượn", command=them_phieu_muon).grid(row=6, column=0, columnspan=2)
tk.Button(frame_phieu_muon, text="Sửa Phiếu Mượn", command=sua_phieu_muon).grid(row=7, column=0, columnspan=2)
tk.Button(frame_phieu_muon, text="Xóa Phiếu Mượn", command=xoa_phieu_muon).grid(row=8, column=0, columnspan=2)

# Data gridview để hiển thị dữ liệu phiếu mượn sách
phieu_muon_treeview = ttk.Treeview(
    frame,
    columns=("ma_phieu_muon", "ma_doc_gia", "ma_thu_thu", "ma_dau_sach", "ngay_muon", "ngay_tra"),
    show="headings"
)
phieu_muon_treeview.heading("ma_phieu_muon", text="Mã phiếu mượn")
phieu_muon_treeview.heading("ma_doc_gia", text="Mã độc giả")
phieu_muon_treeview.heading("ma_thu_thu", text="Mã thủ thư")
phieu_muon_treeview.heading("ma_dau_sach", text="Mã đầu sách")
phieu_muon_treeview.heading("ngay_muon", text="Ngày mượn")
phieu_muon_treeview.heading("ngay_tra", text="Ngày trả")
phieu_muon_treeview.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Hiển thị dữ liệu lên Treeview phiếu mượn sách ban đầu
hien_thi_phieu_muon()


# Chạy vòng lặp chính của ứng dụng
root.mainloop()

# Đóng phiên cơ sở dữ liệu
session.close()
