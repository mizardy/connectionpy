from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("300x600")
root.title("Войти в систему Dev5")

def registration():
    text = Label(text="Для входа в систему зарегистрируйтесь")
    text_log = Label (text="Введите ваш логин:")
    reg_login = Entry()
    text_password = Label (text="Введите ваш пароль:")
    reg_password = Entry(show="*")  
    button_registration = Button(text="Зарегистрироваться")
    text.pack()
    text_log.pack()
    reg_login.pack()
    text_password.pack()
    reg_password.pack()
    button_registration.pack()

registration()
root.mainloop()