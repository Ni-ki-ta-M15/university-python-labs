# cd C:\Users\mihai\PycharmProjects\pythonTest\SQL
# sqlite3 users_db_python.db
import sqlite3
conn = sqlite3.connect('users_db_python.db')
table_users = "CREATE TABLE User (UserName TEXT, UserLastName TEXT , UserPassword REAL)"

cursor = conn.cursor()
# cursor.execute(table_users)
# users = [
#     ('Nikitos', 'Maliy', 78551),
#     ('Rav', 'Green', 99912),
#     ('Efim33', 'Kary', 13025)
# ]
# insert = 'INSERT INTO User VALUES (?, ?, ?)'
#
# cursor.executemany(insert, users)
# cursor.execute("SELECT * from User")
#
# for data in cursor:
#     print(data)

userName = input('Input your username')
userPassword = input('Input your userPassword')

select = f"SELECT * FROM User WHERE userName = '{userName}' and userPassword = '{userPassword}'"
cursor.execute((select))
data = cursor.fetchone()
if (data):
    print('All okay')
else:
    print('Lose')

conn.commit()
conn.close()

