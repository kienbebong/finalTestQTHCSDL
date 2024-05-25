import tkinter as tk
from tkinter import ttk, messagebox
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from datetime import datetime
import atexit
import os

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

    dau_sach = relationship('DauSach', back_populates='phieu_muons')

class ThuThu(Base):
    __tablename__ = 'thu_thu'
    ma_thu_thu = Column(String, primary_key=True)
    ho_ten = Column(String)
    chuc_nang = Column(String)

# Tạo cơ sở dữ liệu và bảng dữ liệu
engine = create_engine('sqlite:///finalTest.db')
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
    PhieuMuon(ma_doc_gia= "DG004", ma_thu_thu="TT004", ma_dau_sach="DS004", ngay_muon=datetime(2024, 5, 4), ngay_tra=datetime(2025, 5, 4))
]

# Lưu các đối tượng vào cơ sở dữ liệu
session.add_all(borrowing_tickets)
session.add_all(chuyen_nganhs)
session.add_all(the_doc_gias)
session.add_all(thu_thus)
session.add_all(dau_sachs)
session.add_all(phieu_muons)
session.commit()

# Đóng phiên làm việc khi chương trình kết thúc
atexit.register(lambda: session.close())

# Tạo ứng dụng Tkinter
root = tk.Tk()
root.title("Quản Lý Thư Viện")
root.geometry("1500x600")

# Tạo các tab trong ứng dụng
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

frame_dau_sach = ttk.Frame(notebook, width=1000, height=600)
frame_phieu_muon = ttk.Frame(notebook, width=1000, height=600)

frame_dau_sach.pack(fill='both', expand=True)
frame_phieu_muon.pack(fill='both', expand=True)

notebook.add(frame_dau_sach, text='Quản Lý Đầu Sách')
notebook.add(frame_phieu_muon, text='Quản Lý Phiếu Mượn')

# Widgets cho quản lý đầu sách
labels_dau_sach = [
    "Mã Đầu Sách", "Tên Đầu Sách", "Nhà Xuất Bản", "Số Trang",
    "Kích Thước", "Tác Giả", "Số Lượng Sách", "Mã Chuyên Ngành"
]
entries_dau_sach = []

for i, label in enumerate(labels_dau_sach):
    lbl = ttk.Label(frame_dau_sach, text=label)
    lbl.grid(row=i, column=0, padx=5, pady=5, sticky='W')
    entry = ttk.Entry(frame_dau_sach)
    entry.grid(row=i, column=1, padx=5, pady=5, sticky='W')
    entries_dau_sach.append(entry)

# Treeview cho quản lý đầu sách
tree_dau_sach = ttk.Treeview(frame_dau_sach, columns=(1, 2, 3, 4, 5, 6, 7, 8), show='headings', height=10)
tree_dau_sach.grid(row=0, column=2, rowspan=8, padx=5, pady=5)

# Đặt tên cho các cột trong Treeview cho quản lý đầu sách
tree_dau_sach.heading(1, text='Mã Đầu Sách')
tree_dau_sach.heading(2, text='Tên Đầu Sách')
tree_dau_sach.heading(3, text='Nhà Xuất Bản')
tree_dau_sach.heading(4, text='Số Trang')
tree_dau_sach.heading(5, text='Kích Thước')
tree_dau_sach.heading(6, text='Tác Giả')
tree_dau_sach.heading(7, text='Số Lượng Sách')
tree_dau_sach.heading(8, text='Mã Chuyên Ngành')

# Đặt kích thước cho các cột trong Treeview cho quản lý đầu sách
for col in range(1, 9):
    tree_dau_sach.column(col, width=100)

# Hàm thêm mới đầu sách
def add_dau_sach():
    ma_dau_sach = entries_dau_sach[0].get()
    ten_dau_sach = entries_dau_sach[1].get()
    nha_xuat_ban = entries_dau_sach[2].get()
    so_trang = int(entries_dau_sach[3].get())
    kich_thuoc = entries_dau_sach[4].get()
    tac_gia = entries_dau_sach[5].get()
    so_luong_sach = int(entries_dau_sach[6].get())
    ma_chuyen_nganh = entries_dau_sach[7].get()

    new_dau_sach = DauSach(
        ma_dau_sach=ma_dau_sach, ten_dau_sach=ten_dau_sach,
        nha_xuat_ban=nha_xuat_ban, so_trang=so_trang,
        kich_thuoc=kich_thuoc, tac_gia=tac_gia,
        so_luong_sach=so_luong_sach, ma_chuyen_nganh=ma_chuyen_nganh
    )

    session.add(new_dau_sach)
    session.commit()
    messagebox.showinfo("Thông Báo", "Thêm đầu sách thành công!")
    load_dau_sach()

# Hàm tải dữ liệu đầu sách vào Treeview
def load_dau_sach():
    for i in tree_dau_sach.get_children():
        tree_dau_sach.delete(i)

    dau_sachs = session.query(DauSach).all()
    for ds in dau_sachs:
        tree_dau_sach.insert('', 'end', values=(
            ds.ma_dau_sach, ds.ten_dau_sach, ds.nha_xuat_ban,
            ds.so_trang, ds.kich_thuoc, ds.tac_gia,
            ds.so_luong_sach, ds.ma_chuyen_nganh
        ))

# Nút thêm mới đầu sách
btn_add_dau_sach = ttk.Button(frame_dau_sach, text="Thêm Đầu Sách", command=add_dau_sach)
btn_add_dau_sach.grid(row=8, column=0, columnspan=2, pady=10)
# Nút xóa đầu sách
def delete_dau_sach():
    selected_item = tree_dau_sach.selection()
    if not selected_item:
        messagebox.showwarning("Cảnh Báo", "Vui lòng chọn một đầu sách để xóa!")
        return
    ma_dau_sach = tree_dau_sach.item(selected_item, 'values')[0]
    dau_sach = session.query(DauSach).filter_by(ma_dau_sach=ma_dau_sach).first()
    if dau_sach:
        phieu_muon_lien_quan = session.query(PhieuMuon).filter_by(ma_dau_sach=ma_dau_sach).all()
        if phieu_muon_lien_quan:
            for phieu_muon in phieu_muon_lien_quan:
                # Xoá phiếu mượn liên quan
                session.delete(phieu_muon)
                load_phieu_muon()
        session.delete(dau_sach)
        session.commit()
        messagebox.showinfo("Thông Báo", "Xóa đầu sách và các phiếu mượn có liên quan thành công!")
        load_dau_sach()
    else:
        messagebox.showerror("Lỗi", "Đầu sách không tồn tại trong cơ sở dữ liệu!")

btn_delete_dau_sach = ttk.Button(frame_dau_sach, text="Xóa Đầu Sách", command=delete_dau_sach)
btn_delete_dau_sach.grid(row=8, column=1, columnspan=2, pady=10)

# Nút sửa đầu sách
def update_dau_sach():
    selected_item = tree_dau_sach.selection()
    if not selected_item:
        messagebox.showwarning("Cảnh Báo", "Vui lòng chọn một đầu sách để sửa!")
        return
    ma_dau_sach = tree_dau_sach.item(selected_item, 'values')[0]
    dau_sach = session.query(DauSach).filter_by(ma_dau_sach=ma_dau_sach).first()
    if dau_sach:
        ma_dau_sach = entries_dau_sach[0].get()
        ten_dau_sach = entries_dau_sach[1].get()
        nha_xuat_ban = entries_dau_sach[2].get()
        so_trang = int(entries_dau_sach[3].get())
        kich_thuoc = entries_dau_sach[4].get()
        tac_gia = entries_dau_sach[5].get()
        so_luong_sach = int(entries_dau_sach[6].get())
        ma_chuyen_nganh = entries_dau_sach[7].get()

        dau_sach.ma_dau_sach = ma_dau_sach
        dau_sach.ten_dau_sach = ten_dau_sach
        dau_sach.nha_xuat_ban = nha_xuat_ban
        dau_sach.so_trang = so_trang
        dau_sach.kich_thuoc = kich_thuoc
        dau_sach.tac_gia = tac_gia
        dau_sach.so_luong_sach = so_luong_sach
        dau_sach.ma_chuyen_nganh = ma_chuyen_nganh

        session.commit()
        messagebox.showinfo("Thông Báo", "Cập nhật đầu sách thành công!")
        load_dau_sach()
    else:
        messagebox.showerror("Lỗi", "Đầu sách không tồn tại trong cơ sở dữ liệu!")

btn_update_dau_sach = ttk.Button(frame_dau_sach, text="Sửa Đầu Sách", command=update_dau_sach)
btn_update_dau_sach.grid(row=8, column=3, columnspan=2, pady=10)


load_dau_sach()

# Widgets cho quản lý phiếu mượn
labels_phieu_muon = [
    "Mã Phiếu Mượn", "Mã Độc Giả", "Mã Thủ Thư", "Mã Đầu Sách",
    "Ngày Mượn", "Ngày Trả"
]
entries_phieu_muon = []

for i, label in enumerate(labels_phieu_muon):
    lbl = ttk.Label(frame_phieu_muon, text=label)
    lbl.grid(row=i, column=0, padx=5, pady=5, sticky='W')
    entry = ttk.Entry(frame_phieu_muon)
    entry.grid(row=i, column=1, padx=5, pady=5, sticky='W')
    entries_phieu_muon.append(entry)

# Treeview cho quản lý phiếu mượn
tree_phieu_muon = ttk.Treeview(frame_phieu_muon, columns=(1, 2, 3, 4, 5, 6), show='headings', height=10)
tree_phieu_muon.grid(row=0, column=2, rowspan=8, padx=5, pady=5)

# Đặt tên cho các cột trong Treeview cho quản lý phiếu mượn
tree_phieu_muon.heading(1, text='Mã Phiếu Mượn')
tree_phieu_muon.heading(2, text='Mã Độc Giả')
tree_phieu_muon.heading(3, text='Mã Thủ Thư')
tree_phieu_muon.heading(4, text='Mã Đầu Sách')
tree_phieu_muon.heading(5, text='Ngày Mượn')
tree_phieu_muon.heading(6, text='Ngày Trả')

# Đặt kích thước cho các cột trong Treeview cho quản lý phiếu mượn
for col in range(1, 7):
    tree_phieu_muon.column(col, width=100)

# Hàm thêm mới phiếu mượn
def add_phieu_muon():
    ma_phieu_muon = entries_phieu_muon[0].get()
    ma_doc_gia = entries_phieu_muon[1].get()
    ma_thu_thu = entries_phieu_muon[2].get()
    ma_dau_sach = entries_phieu_muon[3].get()
    ngay_muon = entries_phieu_muon[4].get()
    ngay_tra = entries_phieu_muon[5].get()

    new_phieu_muon = PhieuMuon(
        ma_phieu_muon=ma_phieu_muon, ma_doc_gia=ma_doc_gia,
        ma_thu_thu=ma_thu_thu, ma_dau_sach=ma_dau_sach,
        ngay_muon=ngay_muon, ngay_tra=ngay_tra
    )

    session.add(new_phieu_muon)
    session.commit()
    messagebox.showinfo("Thông Báo", "Thêm phiếu mượn thành công!")
    load_phieu_muon()

# Hàm tải dữ liệu phiếu mượn vào Treeview
def load_phieu_muon():
    for i in tree_phieu_muon.get_children():
        tree_phieu_muon.delete(i)

    phieu_muons = session.query(PhieuMuon).all()
    for pm in phieu_muons:
        tree_phieu_muon.insert('', 'end', values=(
            pm.ma_phieu_muon, pm.ma_doc_gia, pm.ma_thu_thu,
            pm.ma_dau_sach, pm.ngay_muon, pm.ngay_tra
        ))

# Nút thêm mới phiếu mượn
btn_add_phieu_muon = ttk.Button(frame_phieu_muon, text="Thêm Phiếu Mượn", command=add_phieu_muon)
btn_add_phieu_muon.grid(row=8, column=0, columnspan=2, pady=10)
# Nút xóa phiếu mượn
def delete_phieu_muon():
    selected_item = tree_phieu_muon.selection()
    if not selected_item:
        messagebox.showwarning("Cảnh Báo", "Vui lòng chọn một phiếu mượn để xóa!")
        return
    ma_phieu_muon = tree_phieu_muon.item(selected_item, 'values')[0]
    phieu_muon = session.query(PhieuMuon).filter_by(ma_phieu_muon=ma_phieu_muon).first()
    if phieu_muon:
        session.delete(phieu_muon)
        session.commit()
        messagebox.showinfo("Thông Báo", "Xóa phiếu mượn thành công!")
        load_phieu_muon()
    else:
        messagebox.showerror("Lỗi", "Phiếu mượn không tồn tại trong cơ sở dữ liệu!")

btn_delete_phieu_muon = ttk.Button(frame_phieu_muon, text="Xóa Phiếu Mượn", command=delete_phieu_muon)
btn_delete_phieu_muon.grid(row=8, column=2, columnspan=2, pady=10)

# Nút sửa phiếu mượn
def update_phieu_muon():
    selected_item = tree_phieu_muon.selection()
    if not selected_item:
        messagebox.showwarning("Cảnh Báo", "Vui lòng chọn một phiếu mượn để sửa!")
        return
    ma_phieu_muon = tree_phieu_muon.item(selected_item, 'values')[0]
    phieu_muon = session.query(PhieuMuon).filter_by(ma_phieu_muon=ma_phieu_muon).first()
    if phieu_muon:
        ma_phieu_muon = entries_phieu_muon[0].get()
        ma_doc_gia = entries_phieu_muon[1].get()
        ma_thu_thu = entries_phieu_muon[2].get()
        ma_dau_sach = entries_phieu_muon[3].get()
        ngay_muon = entries_phieu_muon[4].get()
        ngay_tra = entries_phieu_muon[5].get()

        phieu_muon.ma_phieu_muon = ma_phieu_muon
        phieu_muon.ma_doc_gia = ma_doc_gia
        phieu_muon.ma_thu_thu = ma_thu_thu
        phieu_muon.ma_dau_sach = ma_dau_sach
        phieu_muon.ngay_muon = ngay_muon
        phieu_muon.ngay_tra = ngay_tra

        session.commit()
        messagebox.showinfo("Thông Báo", "Cập nhật phiếu mượn thành công!")
        load_phieu_muon()
    else:
        messagebox.showerror("Lỗi", "Phiếu mượn không tồn tại trong cơ sở dữ liệu!")

btn_update_phieu_muon = ttk.Button(frame_phieu_muon, text="Sửa Phiếu Mượn", command=update_phieu_muon)
btn_update_phieu_muon.grid(row=8, column=4, columnspan=2, pady=10)

load_phieu_muon()

def cleanup():
    # Đảm bảo tệp cơ sở dữ liệu tồn tại trước khi xóa
    if os.path.exists('finalTest.db'):
        os.remove('finalTest.db')

# Đăng ký hàm dọn dẹp với atexit
atexit.register(cleanup)

# Tiếp tục với việc khởi tạo engine và các hoạt động khác
engine = create_engine('sqlite:///librarytest.db')

root.mainloop()



