#install module pymysql
#create database
#write code for connnection
#write code for adding in table
import pymysql
from tkinter import *
from tkinter import messagebox
from pymysql.cursors import DictCursor
connection = pymysql.connect(
    host='localhost',
    user='admin',
    password='userdifferent',
    db='mydb',
    charset='utf8mb4',
    cursorclass=DictCursor
)

root = Tk()
root.geometry("300x500")
root.title("Войти в систему")


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

addusers = connection.cursor()
sql = "INSERT INTO users (id, login, password) VALUES (%s, %s,%s)"
val = ("1","admin","password")
addusers.execute(sql,val)
connection.commit()
print(addusers.rowcount, "record inserted.")
