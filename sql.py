import mysql.connector
from dotenv import load_dotenv

import os 

load_dotenv()
db_name=os.getenv("DB_NAME")
host = os.getenv("DB_HOST_NAME")
user = os.getenv("DB_USER_NAME")
password = os.getenv("DB_PASSWORD")
port = os.getenv("DB_PORT")

print(db_name)
print(user)
print(host)
print(password)
print(port)

# Connection
try:
    conn = mysql.connector.connect(
        database=db_name,
        host = host,
        port = port,
        user = user,
        password = password
    )
    cur = conn.cursor()
    print("Connection Successful")
except mysql.connector.Error as err:
    print(err)

table = """
    CREATE TABLE student(
        RollNo INT NOT NULL PRIMARY KEY,
        Name VARCHAR(25),
        Email VARCHAR(30),
        Domain VARCHAR(25),
        Division VARCHAR(1),
        Marks INT
    )

"""
cur.execute(table)

# Creating Sample Records
data_to_insert = [
    (101, 'Amit Kumar', 'amit@example.com', 'Data Science', 'A', 85),
    (102, 'Priya Sharma', 'priya@example.com', 'Web Developer', 'B', 78),
    (103, 'Rahul Verma', 'rahul@example.com', 'DevOps', 'A', 92),
    (104, 'Neha Singh', 'neha@example.com', 'UI/UX', 'B', 75),
    (105, 'Vikas Gupta', 'vikas@example.com', 'Web Developer', 'A', 88)
]
insert_query = "INSERT INTO student (RollNo, Name, Email, Domain, Division, Marks) VALUES (%s, %s, %s, %s, %s, %s)"

for record in data_to_insert:
    cur.execute(insert_query, record)
    conn.commit()

data = cur.execute('''SELECT * FROM student''')

for row in data:
    print(row)

conn.commit()
conn.close()