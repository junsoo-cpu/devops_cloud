from tkinter import *

w = Tk()
w.title("Hello Renoir!")
w.geometry("400x400")

photo = PhotoImage(file="C:\image.gif")
pLabel = Label(w, image=photo)
pLabel.pack(expand=1, anchor=CENTER)

w.mainloop()