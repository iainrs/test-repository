import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()
# responsible for connection

#create_table = "CREATE TABLE users (id int, username text, password text)"

#cursor.execute(create_table)

#user = (1, 'jose', 'asdf')

#users = [
#    (2,'rolf','ghjk'),
#    (3,'anne','zxcv')
#]

#insert_query = "INSERT INTO users VALUES (?, ?, ?)"
#cursor.executemany(insert_query,users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)


connection.commit()
connection.close()

