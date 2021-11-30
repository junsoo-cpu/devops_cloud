from tkinter import *

window = Tk()
window.title("라벨 연습")
window.geometry("400x400")  # 넓이 * 높이

# window 사이즈 고정
label1 = Label(window, text='This is MariaDB를')
label2 = Label(window, text='열심히', font=("궁서체",30), fg="blue")
label3 = Label(window, text='공부 중 입니다.', bg="magenta", width=20, height=5, anchor=SE)
# 레이블이 올라갈 윈도우, 출력될 글, 설정 : font, fg = 글자색, bg = 배경색, anchor = 글자의 위치
label1.pack()
label2.pack()
label3.pack()
# GUI 화면 코딩
window.mainloop()