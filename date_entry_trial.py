import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import date

def submit():
    selected_date = date_entry.get_date()
    print(f"Selected Date: {selected_date}")

root = tk.Tk()
root.title("Date Picker Example")

# Create a frame
engine_info_frame = ttk.Frame(root, padding="10")
engine_info_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create a label for the date entry
date_label = ttk.Label(engine_info_frame, text="Select a Date")
date_label.grid(row=2, column=0)

# Get today's date as a datetime.date object
today = date.today()

# Create a DateEntry widget with mindate set to today
date_entry = DateEntry(engine_info_frame, date_pattern='dd', mindate=today)
date_entry.grid(row=3, column=0)

# Create a submit button
submit_button = ttk.Button(engine_info_frame, text="Submit", command=submit)
submit_button.grid(row=4, column=0)

root.mainloop()
