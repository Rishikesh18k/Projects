import mysql.connector

db = mysql.connector.connect(host='localhost', user='root', password='root', database='fitmenu')
cursor = db.cursor()
cursor.execute('CREATE Table details(Username Varchar(50), Password Varchar(255), Email Varchar(254))')