# cd C:\Users\mihai\PycharmProjects\pythonTest\SQL
# sqlite3 data_db_python.db
import  sqlite3
conn = sqlite3.connect('data_db_python.db')

cursor = conn.cursor()
# cursor.execute("CREATE TABLE car (Make TEXT, Model TEXT, Price REAL, Dollar TEXT); ")
#
# cursor.execute('INSERT INTO car (Make, Model, Price, Dollar) VALUES ("Germany", "Volvo XC 90", 15000, "$")')
# cursor.execute('INSERT INTO car (Make, Model, Price, Dollar) VALUES ("Germany", "Mercedes G63 AMG", 23260, "₽")')
# cursor.execute('INSERT INTO car (Make, Model, Price, Dollar) VALUES ("Germany", "Mercedes GLB ", 34120, "₴")')
# cursor.execute('INSERT INTO car (Make, Model, Price, Dollar) VALUES ("Germany", "Mercedes GLC ", 31900, "₴")')
# cursor.execute('INSERT INTO car (Make, Model, Price, Dollar) VALUES ("Germany", "Mercedes GLB SUV", 28640, "₴")')

# cursor.execute('DROP TABLE car')

# # Start BAD EXPIREMENT
# Make = "China"
# Model = "Mercedes GLSIS SUU"
# Price = 9229
# Dollar = "₴"
#
# insert = f'INSERT INTO car VALUES ("{Make}", "{Model}", {Price}, "{Dollar}")'
#
# conn.execute(insert)
# # End BAD EXPIREMENT

# Start BEST ! EXPIREMENT
Make = "USA"
Model = "Mercedes E-Class AMG Brabus"
Price = 179500
Dollar = "$"
insert = 'INSERT INTO car VALUES (?, ?, ?, ?)'
# conn.execute(insert, (Make, Model, Price, Dollar))
# End BEST EXPIREMENT

# Best_car = ('Audi', 'Q8', '145200', '$')
# conn.execute(insert, Best_car)

# list_car = [
#     ('Germany', 'BMW', 30.500, '€'),
#     ('Russian', 'Honda', 1910, '$'),
#     ('Britany', 'Nissan', 13600, '€'),
#     ('Japan', 'Opel', 7100, '$')
# ]
# for list_car_but_typle in list_car:
#     cursor.execute(insert, list_car_but_typle)

# cursor.execute("UPDATE car SET Price = '31650' WHERE Price = '30.5'")

# list_best_car = [
# ("USA", "Volvo XC 60", 19900, "$"),
# ("JApan", "Mercedes C AMG", 21000, "$"),
# ("USA", "Mercedes EQL ", 45330, "$"),
# ("Italy", "Mercedes Vito ", 9990, "$"),
# ("Italy", "Mercedes CLE Cab", 30000, "$")
# ]
# cursor.executemany(insert, list_best_car)

# cursor.execute("SELECT Model, Price from car WHERE Model LIKE '%GL%'")

cursor.execute("SELECT * from car")
# cursor.execute("UPDATE car SET Price = 8000 and Dollar = '₽' WHERE Model = 'Mercedes GLSIS SUU'")

# cursor.execute("DELETE from car WHERE Model = 'Opel'")
for data in cursor:
    print(data)

# print(cursor.fetchall())



conn.commit()
conn.close()

