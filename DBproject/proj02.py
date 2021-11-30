from tkinter import *
from tkinter import messagebox

# 버튼을 사용하여 알림 창 띄우기
def clickButtion() :
    messagebox.showinfo('버튼 클릭', '닫아줘')


# GUI 화면 코딩

window = Tk()
window.title("버튼 이벤트 연습")
window.geometry("400x400")

button1 = Button(window, text='눌러줘', fg='red', bg='yellow', command=clickButtion)
button2 = Button(window, text='누르지마', fg='red', bg='yellow', command=clickButtion)
button3 = Button(window, text='여기 눌러', fg='red', bg='yellow', command=clickButtion)
button1.pack(side=LEFT, padx=10, pady=10)
button2.pack(side=TOP, padx=10, pady=10)
button3.pack(side=BOTTOM, padx=10, pady=10)


window.mainloop()