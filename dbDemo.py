import mysql.connector
from utilities.configurations import *

# conn = mysql.connector.connect(host='localhost', database='APIDevelop',
#                               user='root', password='root')
conn = getConnection()
print(conn.is_connected())

cursor = conn.cursor()

cursor.execute('select * from CustomerInfo')
rows = cursor.fetchall()
print(rows)

sum = 0
for row in rows:
    sum = sum + row[2]

assert sum == 340
print(sum)

query_update = "update CustomerInfo set Location = %s where CourseName = %s"
data_update = ('Europe', 'selenium')
query_delete = "delete from CustomerInfo where CourseName = 'WebServices'"
cursor.execute(query_update,data_update)
cursor.execute(query_delete)



conn.commit()
conn.close()