import tkinter as tk
from tkinter import messagebox
from my_flight_package.destinations import get_destinations, get_price
from my_flight_package.iterators import FlightIterator
from my_flight_package.decorators import db_error_handler
import psycopg2

class BookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flight Booking System")

        tk.Label(root, text="First Name:").grid(row=0, column=0)
        self.first_name_entry = tk.Entry(root)
        self.first_name_entry.grid(row=0, column=1)

        tk.Label(root, text="Last Name:").grid(row=1, column=0)
        self.last_name_entry = tk.Entry(root)
        self.last_name_entry.grid(row=1, column=1)

        tk.Label(root, text="Destination:").grid(row=2, column=0)
        self.destination_var = tk.StringVar(root)
        self.destination_var.set("Select Destination")
        destinations = get_destinations()
        self.destination_menu = tk.OptionMenu(root, self.destination_var, *destinations, command=self.update_price)
        self.destination_menu.grid(row=2, column=1)

        tk.Label(root, text="Class:").grid(row=3, column=0)
        self.class_var = tk.StringVar(value="Economy")
        self.economy_radio = tk.Radiobutton(root, text="Economy", variable=self.class_var, value="Economy", command=self.update_price)
        self.economy_radio.grid(row=3, column=1)
        self.business_radio = tk.Radiobutton(root, text="Business", variable=self.class_var, value="Business", command=self.update_price)
        self.business_radio.grid(row=3, column=2)

        self.price_label = tk.Label(root, text="Price: Not Selected")
        self.price_label.grid(row=4, column=0, columnspan=2)

        tk.Label(root, text="Date (YYYY-MM-DD):").grid(row=5, column=0)
        self.date_entry = tk.Entry(root)
        self.date_entry.grid(row=5, column=1)

        tk.Button(root, text="Add Flight", command=self.add_flight).grid(row=6, column=0, columnspan=2)

        tk.Label(root, text="Available Flights:").grid(row=7, column=0, columnspan=2)
        self.flight_listbox = tk.Listbox(root, width=50, height=10)
        self.flight_listbox.grid(row=8, column=0, columnspan=2)

        tk.Button(root, text="Load Flights", command=self.show_flights).grid(row=9, column=0, columnspan=2)

    def update_price(self, *args):
        destination = self.destination_var.get()
        flight_class = self.class_var.get()
        price = get_price(destination, flight_class)
        self.price_label.config(text=f"Price: ${price}" if price else "Price: Not Selected")

    @db_error_handler
    def add_flight(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        destination = self.destination_var.get()
        flight_class = self.class_var.get()
        flight_date = self.date_entry.get()
        price = get_price(destination, flight_class)

        if first_name and last_name and destination and flight_date and price:
            conn = psycopg2.connect(dbname="flights", user="postgres", password="18181818", host="localhost", port="5432")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO flights (first_name, last_name, destination, price, flight_date, class) VALUES (%s, %s, %s, %s, %s, %s)",
                           (first_name, last_name, destination, price, flight_date, flight_class))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Flight added successfully!")
            self.show_flights()
        else:
            messagebox.showerror("Error", "All fields must be filled correctly.")

    @db_error_handler
    def show_flights(self):
        conn = psycopg2.connect(dbname="flights", user="postgres", password="18181818", host="localhost", port="5432")
        cursor = conn.cursor()
        cursor.execute("SELECT id, first_name, last_name, destination, price, flight_date, class FROM flights")
        flights = cursor.fetchall()
        conn.close()

        self.flight_listbox.delete(0, tk.END)
        for flight in FlightIterator(flights):
            self.flight_listbox.insert(tk.END, f"{flight[0]} - {flight[1]} {flight[2]} | {flight[3]} | ${flight[4]} | {flight[5]} | {flight[6]}")
