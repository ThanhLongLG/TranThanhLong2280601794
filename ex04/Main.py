from quanlysinhvien import QuanLySinhvien

qlsv =QuanLySinhvien()
while(1==1):
    print("\n CHUONG TRINH QUAN LY SINH VIEN")
    print("***********************************************")
    print("** 1.Them Sinh vien **")
    print("** 2.Cap Nhat Sinh vien boi ID **")
    print("** 3.Xoa sinh vien boi ID **")
    print("** 4.Tim Sinh vien theo ten **")
    print("** 5.Sap xep sinh vien theo diem TB **")
    print("** 6.Sap xep sinh vien theo diem chuyen nganh **")
    print("** 7.hien thi danh sach sinh vien **")
    print("** 0.Thoat **")
    print("***********************************************")
    key = int(input("Nhap tuy chon: "))
    if(key == 1 ):
        print("\n1.Them sinh vien")
        qlsv.nhapsinhvien()
        print("\nThem sinh vien thanh cong!")
    elif(key ==2):
        if(qlsv.soluongsinhvien()>0):
            print("\n2.Cap nhat thong tin sinh vien")
            print("\nNhap Id: ")
            Id =int(input())
            qlsv.updatesinhvien(Id)
        else:
            print("\nsanh sach sinh vien trong!")
    elif(key==3):
        if(qlsv.soluongsinhvien()>0):
            print("\n3.xoa sinh vien.")
            print("\n Nhap ID: ")
            ID=int(input())
            if(qlsv.deleteById(ID)):
                print("\n sinh vien co id= ",ID,"da bi xoa")
            else:
                print("\n Sinh vien co id= ",ID,"Khong ton tai.")
        else:
            print("\n danh sach sinh vien trong!")
    elif(key==4):
        if(qlsv.soluongsinhvien()>0):
            print("\n4.tim kiem theo ten.")
            print("\nNhap ten de tim kiem: ")
            name = input()
            searchResult=qlsv.findByName(name)
            qlsv.showsinhvien(searchResult)
        else:
            print("\n danh sach sinh vien trong")
    elif(key==5):
        if(qlsv.soluongsinhvien()>0):
            print("\n5. sap xep sinh vien theo diem trung binh (GPA)")
            qlsv.sortByDiemTB()
            qlsv.showsinhvien(qlsv.getListSinhVien())
        else:
            print("\n danh sinh vien trong")
    elif(key==6):
        if(qlsv.soluongsinhvien()>0):
            print("\n6. sap xep sinh vien theo ten.")
            qlsv.sortByName()
            qlsv.showsinhvien(qlsv.getListSinhVien())
        else:
            print("\ndanh sach sinh vien trong!")
    elif(key==7):
        if(qlsv.soluongsinhvien()>0):
            print("\n7.hien thi danh sach sinh vien.")
            qlsv.showsinhvien(qlsv.getListSinhVien())
        else:
            print("danh sach siunh vien trong!")
    elif(key==0):
        print("\n ban da thoat")
        break
    else:
        print("\nKhong co chuc nang nay!")
        print("\nHay chon chuc nang trong menu!")

