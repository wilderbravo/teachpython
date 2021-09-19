# https://www.w3schools.com/python/python_mysql_select.asp
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  port="3306",
  database="Tienda"
)

mycursor = mydb.cursor()
mycursor.execute("select * from producto;")
# mycursor.execute("select * from togo.tbl_citizen limit 2")
myresult = mycursor.fetchall()

mycursor = mydb.cursor()
mycursor.execute("select * from producto where producto_id=1;")
# mycursor.execute("select * from togo.tbl_citizen limit 2")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)