import tkinter as tk

def start_countdown():
    global remaining_time
    if remaining_time > 0:
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        timer_label.config(text=f"{minutes:02}:{seconds:02}")
        remaining_time -= 1
        timer_label.after(1000, start_countdown)  # Schedule the next update after 1 second
    else:
        timer_label.config(text="Time's up!")

def on_start():
    start_button.pack_forget()  # Hide the start button
    timer_label.pack(pady=20)  # Show the timer label
    start_countdown()  # Start the countdown

# Create the main window
root = tk.Tk()
root.title("Countdown Timer")

# Initialize remaining time to 5 minutes (300 seconds)
remaining_time = 300

# Create a label to display the timer
timer_label = tk.Label(root, font=("Helvetica", 48), text="")  # Initially empty
timer_label.pack(pady=20)  # Pack it with some padding

# Create a button to start the countdown
start_button = tk.Button(root, text="Start", command=on_start)
start_button.pack()

# Run the main event loop
root.mainloop()
