import tkinter as tk
from tkinter import ttk

from gui.mySql import cursor, db
class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("600x400")
        
        # Tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True)
        
        self.books_tab = ttk.Frame(self.notebook)
        self.borrowers_tab = ttk.Frame(self.notebook)
        self.borrow_tab = ttk.Frame(self.notebook)
        
        self.notebook.add(self.books_tab, text="Books")
        self.notebook.add(self.borrowers_tab, text="Borrowers")
        self.notebook.add(self.borrow_tab, text="Borrow & Return")
        
        self.create_books_tab()
        self.create_borrowers_tab()
        self.create_borrow_tab()
    
    def create_books_tab(self):
        ttk.Label(self.books_tab, text="Book Title:").grid(row=0, column=0, padx=10, pady=5)
        self.book_title = ttk.Entry(self.books_tab)
        self.book_title.grid(row=0, column=1, padx=10, pady=5)
        
        ttk.Label(self.books_tab, text="Author:").grid(row=1, column=0, padx=10, pady=5)
        self.book_author = ttk.Entry(self.books_tab)
        self.book_author.grid(row=1, column=1, padx=10, pady=5)
        
        ttk.Button(self.books_tab, text="Add Book", command=self.add_book).grid(row=2, columnspan=2, pady=10)
        
        self.books_list = ttk.Treeview(self.books_tab, columns=("Title", "Author"), show="headings")
        self.books_list.heading("Title", text="Title")
        self.books_list.heading("Author", text="Author")
        self.books_list.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
    
    def create_borrowers_tab(self):
        ttk.Label(self.borrowers_tab, text="Borrower Name:").grid(row=0, column=0, padx=10, pady=5)
        self.borrower_name = ttk.Entry(self.borrowers_tab)
        self.borrower_name.grid(row=0, column=1, padx=10, pady=5)
        
        ttk.Button(self.borrowers_tab, text="Add Borrower", command=self.add_borrower).grid(row=1, columnspan=2, pady=10)
        
        self.borrowers_list = ttk.Treeview(self.borrowers_tab, columns=("Name",), show="headings")
        self.borrowers_list.heading("Name", text="Name")
        self.borrowers_list.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
    
    def create_borrow_tab(self):
        ttk.Label(self.borrow_tab, text="Select Book:").grid(row=0, column=0, padx=10, pady=5)
        self.selected_book = ttk.Combobox(self.borrow_tab)
        self.selected_book.grid(row=0, column=1, padx=10, pady=5)
        
        ttk.Label(self.borrow_tab, text="Select Borrower:").grid(row=1, column=0, padx=10, pady=5)
        self.selected_borrower = ttk.Combobox(self.borrow_tab)
        self.selected_borrower.grid(row=1, column=1, padx=10, pady=5)
        
        ttk.Button(self.borrow_tab, text="Borrow Book", command=self.borrow_book).grid(row=2, columnspan=2, pady=10)
        ttk.Button(self.borrow_tab, text="Return Book", command=self.return_book).grid(row=3, columnspan=2, pady=10)
    
    # def add_book(self):
    #     title = self.book_title.get()
    #     author = self.book_author.get()
    #     if title and author:
    #         self.books_list.insert("", "end", values=(title, author))
    #         self.selected_book["values"] = [title] + list(self.selected_book["values"])
    #         self.book_title.delete(0, tk.END)
    #         self.book_author.delete(0, tk.END)
    
    def add_book(self):
        title = self.book_title.get()
        author = self.book_author.get()
        if title and author:
            if not db.is_connected():
                db.reconnect()
            cursor.execute("INSERT INTO books (title, author) VALUES (%s, %s)", (title, author))
            db.commit()
            self.books_list.insert("", "end", values=(title, author))
            self.selected_book["values"] = [title] + list(self.selected_book["values"])
            self.book_title.delete(0, tk.END)
            self.book_author.delete(0, tk.END)
            cursor.execute("SELECT * FROM book_store")
            for row in cursor.fetchall():
                print(row)

    def add_borrower(self):
        name = self.borrower_name.get()
        if name:
            if not db.is_connected():
                db.reconnect()
            cursor.execute('INSERT INTO borrowers (name) VALUES (%s)',(name,))
            db.commit()
            self.borrowers_list.insert("", "end", values=(name,))
            self.selected_borrower["values"] = [name] + list(self.selected_borrower["values"])
            self.borrower_name.delete(0, tk.END)
            cursor.execute("SELECT * FROM borrowers")
            for row in cursor.fetchall():
                print(row)
                
            
                
    
    def borrow_book(self):
        book = self.selected_book.get()
        borrower = self.selected_borrower.get()
        if book and borrower:
            
            print(f"{borrower} borrowed {book}")
    
    def return_book(self):
        book = self.selected_book.get()
        if book:
            print(f"{book} returned")

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
