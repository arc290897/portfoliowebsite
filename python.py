#!C:/Users/LENOVO/AppData/Local/Programs/Python/Python38/python


print("Content-Type:text/html")
print()


import cgi


form=cgi.FieldStorage()

name=form.getvalue("name")
email=form.getvalue("email")
address=form.getvalue("address")

import mysql.connector

con=mysql.connector.connect(user='root',password='',host='localhost',database='a')
cur=con.cursor()

cur.execute("insert into student values(%s,%s,%s)",(name,email,address))
con.commit()

cur.close()
con.close()
print("<h4>Thanks for contacting")
