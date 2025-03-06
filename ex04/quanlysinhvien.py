from Sinhvien import SinhVien
class QuanLySinhvien:
    listsinhvien=[]
    def generateID(self):
        maxId=1
        if(self.soluongsinhvien()>0):
            maxId =self.listsinhvien[0]._id
            for sv in self.listsinhvien:
                if(maxId<sv._id):
                    maxId = sv._id
            maxId =maxId+1
        return maxId
    def soluongsinhvien(self):
        return self.listsinhvien.__len__()

    def nhapsinhvien(self):
        svId=self.generateID()
        name =input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("nhap chuyen nganh cua sinh vien: ")
        diemtb= float(input("nhap diem cua sinh vien: "))
        sv = SinhVien(svId,name,sex,major,diemtb)
        self.xeploaihocluc(sv)
        self.listsinhvien.append(sv)

    def updatesinhvien(self,id):
        sv:SinhVien=self.findByID(id)
        if(sv!=None):
            name =input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh sinh vien: ")
            major = input("nhap chuyen nganh cua sinh vien: ")
            diemtb= float(input("nhap diem cua sinh vien: "))   
            sv._name=name
            sv._sex=sex
            sv._major=major
            sv._diemtb=diemtb
            self.xeploaihocluc(sv)
        else:
            print("sinh vien co Id= {} khong ton tai.".format(id))
    
    def sortByID(self):
        self.listsinhvien.sort(key=lambda x: x._id,reversed=False)
    
    def sortByName(self):
        self.listsinhvien.sort(key=lambda x: x._name,reverse=False)
    def sortByDiemTB(self):
        self.listsinhvien.sort(key=lambda X: X._diemTB,reverse=False)

    def findByID(self,Id):
        searchResult =None
        if(self.soluongsinhvien() > 0):
            for sv in self.listsinhvien:
                if(sv._id == Id):
                    searchResult=sv
        return searchResult
    def findByName(self, keyword):
        listSV=[]
        if(self.soluongsinhvien() >0):
              for sv in self.listsinhvien:
                  if(keyword.upper()in sv._name.upper()):
                      listSV.append(sv)
        return listSV
    
    def deleteById(self,Id):
        isDeleted = False
        sv=self.findByID(Id)
        if(sv!=None):
            self.listsinhvien.remove(sv)
            isDeleted=True
        return isDeleted
    def xeploaihocluc(self,sv: SinhVien):
        if(sv._diemtb >=8):
            sv._hocluc="gioi"
        elif(sv._diemtb>=6.5):
            sv._hocluc="kha"
        elif(sv._diemtb>=5):
            sv._hocluc="trung binh"
        else:
            sv._hocluc = "kem"
        
    def showsinhvien(self, listSV):
        print("{:<8} {:<18} {:<8} {:<15} {:<8} {:<8}".format("ID", "Name", "Sex", "Major", "DiemTb", "HocLuc"))
        if len(listSV) > 0:
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<15} {:<8} {:<8}".format(
                    sv._id, sv._name, sv._sex, sv._major, sv._diemtb, sv._hocluc))
        print("\n")
    
    def getListSinhVien(self):
        return self.listsinhvien
