'''import pymysql

db = pymysql.connect("localhost", "root", "", "")
cursor = db.cursor()'''

'''cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version : %s " % data)'''

# Create table
'''sql = """CREATE TABLE EMPLOYEE (
   FIRST_NAME  VARCHAR(20) NOT NULL,
   LAST_NAME  VARCHAR(20),
   AGE INT,  
   SEX CHAR(1),
   EMAIL VARCHAR(30),
   INCOME FLOAT )"""'''

'''sql = """DROP DATABASE my_db"""
cursor.execute(sql)

db.commit()
db.close()'''
