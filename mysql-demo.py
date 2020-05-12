import mysql.connector

mydb = mysql.connector.connect(host="127.0.0.1", user="root", passwd="123456")
mycursor = mydb.cursor()
query = "SELECT * FROM cms.performance   limit 10"
mycursor.execute(query)
myresult = mycursor.fetchall()
for x in myresult:
    for item in x:
        print(item)
