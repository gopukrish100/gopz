import mysql.connector
db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Password@123'
)
cursor=db.cursor()

cursor.execute('SELECT VERSION()')

data=cursor.fetchone()
print('Database version : %s' % data)

db.close()