# 📚 Library Management System  

## 🎯 Introduction  
A **Library Management System** built with **Python (Tkinter)** and **MySQL** to efficiently manage books, borrowers, and borrowing/returning operations.  

## 🚀 Features  
- ✅ **Book Management:** Add, list, and manage books in the library.  
- ✅ **Borrower Management:** Add and track borrowers.  
- ✅ **Borrow & Return:** Manage book borrowing and return operations.  
- ✅ **Persistent Data:** Uses MySQL to store book and borrower details.  
- ✅ **GUI Interface:** Built with Tkinter for an intuitive user experience.  

## 🏗️ Project Structure  
```plaintext
Bookstore-App/
│── gui/
│   ├── __init__.py
│   ├── mySql.py  # Database connection and queries
│── README.md      # Project documentation
└── requirements.txt  # Dependencies
```

## 🔧 Installation  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/erfanrazavi1/Bookstore-App.git
```

### 2️⃣ Install Dependencies  
Ensure you have **Python (>=3.8)** installed, then run:  
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up MySQL Database  
- Install **MySQL** and create a database named **book_store**.  
- Update your **mySql.py** file with your **MySQL host, user, and password**.  

### 4️⃣ Run the Application  
```bash
python -m gui.tk
```

## 🛠️ Technologies Used  
- **Python** (Tkinter for GUI)  
- **MySQL** (Database Management)  
- **MySQL Connector** (Python Library for MySQL)  

## 📸 Screenshots  
| Books Tab | Borrowers Tab | Borrow & Return |
|-----------|-------------|----------------|
| 📚 | 🧑‍💼 | 🔄 |

## 🔥 To-Do  
- ✅ Implement basic CRUD operations  
- ✅ GUI interface with Tkinter  
- ⏳ Improve borrowing/return functionality  
- ⏳ Add user authentication  

## 📝 License  
This project is **MIT Licensed**. Feel free to use and modify it.
