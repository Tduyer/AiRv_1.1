from my_flight_package.database import init_db
import tkinter as tk
from my_flight_package.gui import BookingApp

init_db()

root = tk.Tk()
app = BookingApp(root)
root.mainloop()
