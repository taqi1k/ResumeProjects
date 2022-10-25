import mysql.connector
from mysql.connector import Error

def create_con(hostname, username, userpw, dbname):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = hostname,
            user = username,
            password = userpw,
            database = dbname
        )
        print("success")
    except Error as e:
        print(f'the error {e} occured')
    return connection

conn = create_con('cis3368.c83qjlqec0fg.us-east-2.rds.amazonaws.com', 'admin', 'Taqi12345', 'cis3368db')
cursor = conn.cursor(dictionary = True)
sql = 'select * from users'
cursor.execute(sql)
rows = cursor.fetchall()
for user in rows:
    print(user)
