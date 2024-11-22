print("Hallo, world!")

print("Hallo, GitHub!")

from tkinter import *
from tkinter import messagebox as mb



def check():
    #answer = mb.askyesno(title="Вопрос", message="Передать данные?")
    answer = mb.askokcancel(title="gtkmvtym", message="bthtnjym?")
    #answer = mb.askretrycancel(title="Вопрос"#название окна
           # ,message="Передать данные?")#вопрос в окне
    if answer:
        s = e.get()
        e.delete(0, END)
        m['text'] = s

window = Tk()
e = Entry()
e.pack()
b = Button(text="Передать", command=check)
b.pack()
m = Label(height=3)
m.pack()
window.mainloop()
