import mysql.connector

""" 
Establish connection to MySQL database 
"""
db = mysql.connector.connect(
    host="host_name",
    user="your_username",
    password="your_pass",
    database="database_name"
)

cursor = db.cursor(buffered=True)

""" 
Create database if it does not exist 
"""
cursor.execute("CREATE DATABASE IF NOT EXISTS book_store")

""" 
Select the database 
"""
cursor.execute("USE book_store")

""" 
Create 'books' table 
"""
cursor.execute("""CREATE TABLE IF NOT EXISTS books (
               id INT AUTO_INCREMENT PRIMARY KEY,
               title VARCHAR(255) NOT NULL,
               author VARCHAR(255) NOT NULL
               )""")

""" 
Create 'borrowers' table 
"""
cursor.execute("""CREATE TABLE IF NOT EXISTS borrowers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL
            )""")

""" 
Create 'borrowed_books' table to track borrowed books 
"""
cursor.execute("""CREATE TABLE IF NOT EXISTS borrowed_books (
            id INT AUTO_INCREMENT PRIMARY KEY,
            book_id INT,
            borrower_id INT,
            borrow_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (book_id) REFERENCES books(id),
            FOREIGN KEY (borrower_id) REFERENCES borrowers(id)
            )""")

""" 
Fetch and display all records from 'borrowers' table 
"""
cursor.execute("SELECT * FROM borrowers")

print('Database and tables have been created successfully.')

for row in cursor.fetchall():
    print(row)
