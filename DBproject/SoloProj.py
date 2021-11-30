import tkinter
import pymysql
from tkinter import *
from tkinter import messagebox

# 고객 정보 추가 함수
def insertData():
    conn = None
    cur = None

    # 데이버베이스 접속
    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='sqlDB', charset='utf8')
    # 커서
    cur = conn.cursor()


    # 사용자에게 입력 받은 회원 정보 초기화
    Customer_ID, Customer_Name, Customer_Age, Customer_Gender, Customer_Addr, Customer_Mobile = "", "", "", "", "", ""

    # GUI에서 입력한 데이터 담기
    Customer_ID = edt1.get()
    Customer_Name = edt2.get()
    Customer_Age = edt3.get()
    Customer_Gender = edt4.get()
    Customer_Addr = edt5.get()
    Customer_Mobile = edt6.get()

    # SQL 쿼리 만들기
    sql = "INSERT INTO customerTBL (Customer_ID, Customer_Name, Customer_Age, Customer_Gender, Customer_Addr , Customer_Mobile, mDate) VALUES " \
          "('" + Customer_ID + "', '" + Customer_Name + "', " + Customer_Age + ", '" + Customer_Gender +"', '" + Customer_Addr + "', '"+ Customer_Mobile + "', CURDATE())"

    # 쿼리 실행
    try :
        cur.execute(sql)
    except :
        messagebox.showerror("입력오류", "이미 등록된 아이디 입니다.")
    else :
        # 쿼리 실행이 완료(오류 없이)
        # 1) 메시지 박스로 성공 알림
        messagebox.showinfo("성공", "회원 정보가 등록되었습니다.")
        # 2) 데이터 커밋(저장)
        conn.commit()
        # 3) 테이블 조회(새로고침)
        selectData()

    # GUI에 입력한 데이터 삭제
    edt1.delete(0, "end")
    edt2.delete(0, "end")
    edt3.delete(0, "end")
    edt4.delete(0, "end")
    edt5.delete(0, "end")
    edt6.delete(0, "end")

    conn.close()

# 고객 정보 조회 함수
def selectData():
    conn = None
    cur = None
    # 데이버베이스 접속
    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='sqlDB', charset='utf8')
    # 커서
    cur = conn.cursor()
    conn.commit()
    lCustomerID, lName, lAge, lGender, lAddr, lMobile = [], [], [], [], [], []

    # 데이터 초기화
    lCustomerID.append("고객 ID")
    lCustomerID.append("---------")

    lName.append("고객 명")
    lName.append("---------")

    lAge.append("고객 나이")
    lAge.append("---------")

    lGender.append("고객 성별")
    lGender.append("---------")

    lAddr.append("고객 주소")
    lAddr.append("---------")

    lMobile.append("휴대폰 번호")
    lMobile.append("----------")

    # select 기능 구현
    sql = "SELECT Customer_ID, Customer_Name, Customer_Age, Customer_Gender, Customer_Addr, Customer_Mobile from CustomerTBL ORDER BY mDate DESC"
    cur.execute(sql)

    while(True):
        row = cur.fetchone()

        if row == None:
            break

        lCustomerID.append(row[0])
        lName.append(row[1])
        lAge.append(row[2])
        lGender.append(row[3])
        lAddr.append(row[4])
        lMobile.append(row[5])

    # GUI ListBox에 insert
    # listUserID, listName, listBirthYear, listAddr
    # 1) 리스트 박스 초기화
    listCustomerID.delete(0, listCustomerID.size()-1)   #
    listName.delete(0, listName.size()-1)
    listAge.delete(0, listAge.size()-1)
    listGender.delete(0, listGender.size()-1)
    listAddr.delete(0, listAddr.size()-1)
    listMobile.delete(0, listMobile.size() - 1)

    # 2) select 해온 데이터 insert
    for item1, item2, item3, item4, item5, item6 in zip(lCustomerID, lName, lAge, lGender, lAddr, lMobile) :  # 직접 가져온 데이터
        listCustomerID.insert(END, item1)
        listName.insert(END, item2)
        listAge.insert(END, item3)
        listGender.insert(END, item4)
        listAddr.insert(END, item5)
        listMobile.insert(END, item6)
    conn.close()

# 경품 당첨자 추첨 함수
def btn_select():
    conn = None
    cur = None
    # 데이버베이스 접속
    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='sqlDB', charset='utf8')
    # 커서
    cur = conn.cursor()
    lName = []

    sql = "SELECT Customer_Name FROM entryTBL WHERE Entry_Situ = 'O' ORDER BY RAND() LIMIT 1"
    cur.execute(sql)
    while (True):
        row = cur.fetchone()

        if row == None:
            break
        lName.append(row[0])
    messagebox.showinfo("당첨자", f"축하드립니다! 당첨자는 {lName}입니다.")
    conn.close()

# 새 창을 띄우는 함수
def createNewWindow():
    global new
    new = Toplevel()
    new.geometry("800x600")
    new.title("응모자 현황")

    # 추가 응모자 입력 함수
    def insertDT():
        conn = None
        cur = None

        # 데이버베이스 접속
        conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='sqlDB', charset='utf8')
        # 커서
        cur = conn.cursor()

        # 사용자에게 입력 받은 회원 정보 초기화
        Customer_ID, name, entry_situ = "", "", ""

        # GUI에서 입력한 데이터 담기
        Customer_ID = edt7.get()
        Customer_Name = edt8.get()
        Entry_Situ = edt9.get()

        # SQL 쿼리 만들기
        sql = "INSERT INTO entryTBL (Customer_ID, Customer_Name, Entry_situ) VALUES " \
              "('" + Customer_ID + "', '" + Customer_Name + "', '" + Entry_Situ + "')"

        print(sql)
        # 쿼리 실행
        try:
            cur.execute(sql)
        except:
            messagebox.showerror("입력오류", "등록되지 않은 고객입니다.")
        else:
            messagebox.showinfo("성공", "회원 정보가 등록되었습니다.")
            conn.commit()
            selectDT()

        edt1.delete(0, "end")
        edt2.delete(0, "end")
        edt3.delete(0, "end")
        conn.close()

        """"""
    # 응모 현황 조회 함수
    def selectDT():
        conn = None
        cur = None
        # 데이버베이스 접속
        conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='sqlDB', charset='utf8')
        # 커서
        cur = conn.cursor()
        conn.commit()
        lCustomerID, lName, lEntry_Situ, = [], [], []
        # 데이터 초기화
        lCustomerID.append("고객 ID")
        lCustomerID.append("---------")

        lName.append("고객 명")
        lName.append("---------")

        lEntry_Situ.append("고객 나이")
        lEntry_Situ.append("---------")

        # select 기능 구현
        sql = "SELECT Customer_ID, Customer_Name, Entry_Situ from EntryTBL ORDER BY Customer_Name ASC"
        cur.execute(sql)

        while (True):
            row = cur.fetchone()

            if row == None:
                break

            lCustomerID.append(row[0])
            lName.append(row[1])
            lEntry_Situ.append(row[2])

        # GUI ListBox에 insert
        # 1) 리스트 박스 초기화
        listCustomerID.delete(0, listCustomerID.size() - 1)  #
        listName.delete(0, listName.size() - 1)
        listEntry_Situ.delete(0, listAge.size() - 1)

        # 2) select 해온 데이터 insert
        for item1, item2, item3 in zip(lCustomerID, lName, lEntry_Situ):  # 직접 가져온 데이터
            listCustomerID.insert(END, item1)
            listName.insert(END, item2)
            listEntry_Situ.insert(END, item3)

        conn.close()

    conn = None
    cur = None
    # 데이버베이스 접속
    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='sqlDB', charset='utf8')
    cur = conn.cursor()
    conn.commit()
    lCustomerID, lName, lEntry_Situ = [], [], []

    # 데이터 초기화
    lCustomerID.append("고객 ID")
    lCustomerID.append("---------")

    lName.append("고객 명")
    lName.append("---------")

    lEntry_Situ.append("응모(O/X)")
    lEntry_Situ.append("---------")

    # select 기능 구현
    sql = "SELECT Customer_ID, Customer_Name, Entry_Situ from EntryTBL ORDER BY Customer_Name ASC"
    cur.execute(sql)

    while (True):
        row = cur.fetchone()

        if row == None:
            break

        lCustomerID.append(row[0])
        lName.append(row[1])
        lEntry_Situ.append(row[2])

    editFrame = Frame(new)
    editFrame.pack()

    listFrame = Frame(new)
    listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

    photo = PhotoImage(file="C:\image.gif")
    pLabel = Label(new, image=photo)
    pLabel.pack(side=TOP, padx=10, pady=10)

    label7 = Label(editFrame, text="고객 ID")
    label7.pack(side=LEFT, padx=10, pady=10)

    edt7 = Entry(editFrame, width=10)
    edt7.pack(side=LEFT, padx=10, pady=10)

    label8 = Label(editFrame, text="고객 명")
    label8.pack(side=LEFT, padx=10, pady=10)

    edt8 = Entry(editFrame, width=10)
    edt8.pack(side=LEFT, padx=10, pady=10)

    label9 = Label(editFrame, text="응모 현황")
    label9.pack(side=LEFT, padx=10, pady=10)

    edt9 = Entry(editFrame, width=10)
    edt9.pack(side=LEFT, padx=10, pady=10)

    btnIns = Button(editFrame, text="추가 응모자 입력", command=insertDT)
    btnIns.pack(side=LEFT, padx=10, pady=10)

    btnEvent = Button(editFrame, text="당첨자", command=btn_select)
    btnEvent.pack(side=LEFT, padx=10, pady=10)

    listCustomerID = Listbox(listFrame)
    listCustomerID.pack(side=LEFT, fill=BOTH, expand=1)

    listName = Listbox(listFrame)
    listName.pack(side=LEFT, fill=BOTH, expand=1)

    listEntry_Situ = Listbox(listFrame)
    listEntry_Situ.pack(side=LEFT, fill=BOTH, expand=1)

    # 1) 리스트 박스 초기화
    listCustomerID.delete(0, listCustomerID.size() - 1)  #
    listName.delete(0, listName.size() - 1)
    listEntry_Situ.delete(0, listAge.size() - 1)

    # 2) select 해온 데이터 insert
    for item1, item2, item3 in zip(lCustomerID, lName, lEntry_Situ):  # 직접 가져온 데이터
        listCustomerID.insert(END, item1)
        listName.insert(END, item2)
        listEntry_Situ.insert(END, item3)

    conn.close()
    new.mainloop()

# GUI 화면 구성
window = Tk()
window.geometry("1300x500")
window.title("고객 현황")

editFrame = Frame(window)
editFrame.pack()

listFrame = Frame(window)
listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

label1 = Label(editFrame, text="고객 ID")
label1.pack(side=LEFT, padx=10, pady=10)

edt1 = Entry(editFrame, width=10)
edt1.pack(side=LEFT, padx=10, pady=10)

label2 = Label(editFrame, text="고객 명")
label2.pack(side=LEFT, padx=10, pady=10)

edt2 = Entry(editFrame, width=10)
edt2.pack(side=LEFT, padx=10, pady=10)

label3 = Label(editFrame, text="고객 나이")
label3.pack(side=LEFT, padx=10, pady=10)

edt3 = Entry(editFrame, width=10)
edt3.pack(side=LEFT, padx=10, pady=10)

label4 = Label(editFrame, text="고객 성별")
label4.pack(side=LEFT, padx=10, pady=10)

edt4 = Entry(editFrame, width=10)
edt4.pack(side=LEFT, padx=10, pady=10)

label5 = Label(editFrame, text="고객 주소")
label5.pack(side=LEFT, padx=10, pady=10)

edt5 = Entry(editFrame, width=10)
edt5.pack(side=LEFT, padx=10, pady=10)

label6 = Label(editFrame, text="휴대폰 번호")
label6.pack(side=LEFT, padx=10, pady=10)

edt6 = Entry(editFrame, width=10)
edt6.pack(side=LEFT, padx=10, pady=10)

# 버튼
btnInsert = Button(editFrame, text="입력", command=insertData)
btnInsert.pack(side=LEFT, padx=10, pady=10)

btnSelect = Button(editFrame, text="조회", command=selectData)
btnSelect.pack(side=LEFT, padx=10, pady=10)

btnEntry = Button(editFrame, text="응모 현황", command=createNewWindow)
btnEntry.pack(side=LEFT, padx=10, pady=10)

# Listbox
listCustomerID = Listbox(listFrame)
listCustomerID.pack(side=LEFT, fill=BOTH, expand=1)

listName = Listbox(listFrame)
listName.pack(side=LEFT, fill=BOTH, expand=1)

listAge = Listbox(listFrame)
listAge.pack(side=LEFT, fill=BOTH, expand=1)

listGender = Listbox(listFrame)
listGender.pack(side=LEFT, fill=BOTH, expand=1)

listAddr = Listbox(listFrame)
listAddr.pack(side=LEFT, fill=BOTH, expand=1)

listMobile = Listbox(listFrame)
listMobile.pack(side=LEFT, fill=BOTH, expand=1)

window.mainloop()






