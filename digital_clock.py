import tkinter as tk
from time import strftime

# Function to update the time on the label
def time():
    # Get the current time in the format HH:MM:SS
    string = strftime('%H:%M:%S %p')
    # Update the label with the current time
    label.config(text=string)
    # Call the time function again after 1000ms (1 second)
    label.after(1000, time)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Create a label widget to display the time
label = tk.Label(root, font=('calibri', 40, ''), background='black', foreground='green')
label.pack(anchor='center')

# Call the time function to update the time on the label
time()

# Run the main event loop
root.mainloop()
