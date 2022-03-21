import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin@123",
  database="tasksdb"
#   database="jtrac_28_dec_21"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)


print("---------------------------------------------") 


mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)