import mysql.connector

# اتصال به MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",      
    password="hasaniii1234",
    database="book_store"
)

cursor = db.cursor()

# ایجاد دیتابیس در صورت عدم وجود
cursor.execute("CREATE DATABASE IF NOT EXISTS book_store")

# انتخاب دیتابیس
cursor.execute("USE book_store")

# ایجاد جدول کتاب‌ها
cursor.execute("""CREATE TABLE IF NOT EXISTS books (
               id INT AUTO_INCREMENT PRIMARY KEY,
               title VARCHAR(255) NOT NULL,
               author VARCHAR(255) NOT NULL
               )""")

# ایجاد جدول امانت‌گیرندگان
cursor.execute("""CREATE TABLE IF NOT EXISTS borrowers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL
            )""")

# ایجاد جدول کتاب‌های امانت داده‌شده
cursor.execute("""CREATE TABLE IF NOT EXISTS borrowed_books (
            id INT AUTO_INCREMENT PRIMARY KEY,
            book_id INT,
            borrower_id INT,
            borrow_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (book_id) REFERENCES books(id),
            FOREIGN KEY (borrower_id) REFERENCES borrowers(id)
            )""")

# نمایش جداول پایگاه داده

# cursor.execute("SELECT * FROM books")
cursor.execute("SELECT * FROM borrowers")




print('Database and tables have been created successfully.') 


for row in cursor.fetchall():
    print(row)


