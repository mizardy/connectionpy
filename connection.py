#install module pymysql
#create base from MySQL
#write code for connnection
#write code for adding in table
import pymysql
from pymysql.cursors import DictCursor
connection = pymysql.connect(
    host='localhost',
    user='yourlogin',
    password='yourpass',
    db='mydb',
    charset='utf8mb4',
    cursorclass=DictCursor
)
addinto = connection.cursor()
sql = "INSERT INTO users (id, login, password) VALUES (%s, %s,%s)"
val = ("1","admin","password")
addinto.execute(sql,val)
connection.commit()
print(addinto.rowcount, "record inserted.")