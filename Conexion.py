# https://www.w3schools.com/python/python_mysql_select.asp
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  port="3306",
  database="togo"
)

mycursor = mydb.cursor()
mycursor.execute("select identity,names,lastnames,birthdate from togo.tbl_citizen where identity = '1204825390';")
# mycursor.execute("select * from togo.tbl_citizen limit 2")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

# print(mydb)