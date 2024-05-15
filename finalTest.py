from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

# Khởi tạo cơ sở dữ liệu và khung mẫu ORM
Base = declarative_base()

# Định nghĩa các thực thể trong cơ sở dữ liệu
class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    ma_doc_gia = Column(String, unique=True)
    ho_ten = Column(String)
    ngay_sinh = Column(Date)
    gioi_tinh = Column(String)
    cmnd = Column(String)
    the_hoc_sinh = Column(String)

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
    ma_doc_gia = Column(String, ForeignKey('the_doc_gia.ma_doc_gia'))
    ma_thu_thu = Column(String, ForeignKey('thu_thu.ma_thu_thu'))
    ma_dau_sach = Column(String, ForeignKey('dau_sach.ma_dau_sach'))
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
engine = create_engine('sqlite:///finalTest.db')
Base.metadata.create_all(engine)

# Tạo phiên giao dịch để làm việc với cơ sở dữ liệu
Session = sessionmaker(bind=engine)
session = Session()