import psycopg2
from tkinter import messagebox

def db_error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except psycopg2.Error as e:
            messagebox.showerror("Database Error", str(e))
    return wrapper
