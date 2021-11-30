from tkinter import *
from tkinter import messagebox


# 버튼을 사용하여 알림 창 띄우기
def clickButtion() :
    messagebox.showinfo('버튼 클릭', '닫아줘')


# GUI 화면 코딩

window = Tk()
window.title("입력관리 연습")
window.geometry("400x400")
# 프레임 : 영역 나누기
# 엔트리 : 입력상자 ( 사용자에게 입력 받는 <input type=text>)
# 리스트박스 : 목록(결과 화면 여러개의 row를 표현해야 할 때)

# 프레임으로 upFrame, downFrame으로 나눠서 영역을 사용
upFrame = Frame(window)
upFrame.pack()

midFrame = Frame(window)
midFrame.pack()

downFrame = Frame(window)
downFrame.pack()

# 입력상자를 upFrame에 배치
editBox = Entry(upFrame, width=10)
editBox.pack(padx=20, pady=20)

button = Button(midFrame, text='중간')
button.pack(padx=20, pady=20)

# 리스트박스는 downFrame에 배치
listBox = Listbox(downFrame)
listBox.pack()

listBox.insert(END, '하나')
listBox.insert(END, '둘')
listBox.insert(END, '셋')


window.mainloop()







