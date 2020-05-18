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

addusers = connection.cursor()
sql = "INSERT INTO users (id, login, password) VALUES (%s, %s,%s)"
val = ("1","admin","password")
addusers.execute(sql,val)
connection.commit()
print(addusers.rowcount, "record inserted.")
