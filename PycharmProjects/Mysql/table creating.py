from pgm2 import *

db=getconnection()

print(db)

cursor=db.cursor()
cursor.execute('DROP TABLE IF EXISTS EMPLOYEE')

sql='''CREATE TABLE EMPLOYEE(
FIRST_NAME CHAR(20),
LAST_NAME CHAR(20),
AGE INT,
SEX CHAR(1),
INCOME FLOAT)'''
cursor.execute(sql)
cursor.execute('''insert into EMPLOYEE values('Gopu','Krishna',27,'M',200000)''')