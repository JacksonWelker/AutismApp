import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime

# Initialize main window
root = tk.Tk()
root.title("Autism Support Super App")
root.geometry("400x600")
root.configure(bg="#f5f5f5")

# ===== Variables =====
reminders = []
contacts = []
font_size = 12  # Default font size

# ===== Reminders Feature =====
def add_reminder():
    reminder_text = reminder_entry.get()
    reminder_hour = hour_spinbox.get()
    reminder_minute = minute_spinbox.get()
    reminder_period = period_var.get()
    
    if reminder_text and reminder_hour and reminder_minute:
        try:
            # Validate the time format
            reminder_time_str = f"{reminder_hour}:{reminder_minute} {reminder_period}"
            reminder_time_dt = datetime.strptime(reminder_time_str, "%I:%M %p")
            # Combine reminder text and time
            full_reminder = f"{reminder_text} at {reminder_time_dt.strftime('%I:%M %p')}"
            reminders.append(full_reminder)
            reminder_entry.delete(0, tk.END)
            update_reminder_list()
        except ValueError:
            messagebox.showwarning("Warning", "Please enter a valid time.")
    else:
        messagebox.showwarning("Warning", "Please enter both reminder text and time.")

def update_reminder_list():
    reminder_list.delete(0, tk.END)
    for reminder in reminders:
        reminder_list.insert(tk.END, reminder)

def remove_reminder():
    selected_reminder_index = reminder_list.curselection()
    if selected_reminder_index:
        reminders.pop(selected_reminder_index[0])
        update_reminder_list()
    else:
        messagebox.showwarning("Warning", "Please select a reminder to remove.")

# ===== Timer Feature =====
def start_custom_timer():
    try:
        global timer_duration
        timer_duration = int(timer_entry.get())
        if timer_duration <= 0:
            messagebox.showwarning("Warning", "Please enter a positive number for the timer.")
            return
        countdown(timer_duration * 60)  # Convert minutes to seconds
    except ValueError:
        messagebox.showwarning("Warning", "Please enter a valid number for the timer.")

def countdown(count):
    minutes, seconds = divmod(count, 60)
    timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
    if count > 0:
        root.after(1000, countdown, count - 1)
    else:
        messagebox.showinfo("Timer", "Time is up!")

# ===== Communication Feature =====
def send_message():
    message = simpledialog.askstring("Send Message", "Enter your message to the support team:")
    if message:
        messagebox.showinfo("Send Message", f"Message sent to support team: '{message}'")

def send_message_to_contact():
    selected_contact_index = contact_list.curselection()
    if selected_contact_index:
        contact_name = contacts[selected_contact_index[0]][0]
        message = simpledialog.askstring("Send Message", f"Enter your message to {contact_name}:")
        if message:
            messagebox.showinfo("Send Message", f"Message sent to {contact_name}: '{message}'")
    else:
        messagebox.showwarning("Warning", "Please select a contact to send a message.")

# ===== Contact Organization Feature =====
def add_contact():
    contact_name = simpledialog.askstring("Add Contact", "Enter contact name:")
    contact_number = simpledialog.askstring("Add Contact", "Enter contact phone number:")
    if contact_name and contact_number:
        contacts.append((contact_name, contact_number))
        update_contact_list()
    else:
        messagebox.showwarning("Warning", "Please enter both name and phone number.")

def update_contact_list():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact[0]} - {contact[1]}")

def remove_contact():
    selected_contact_index = contact_list.curselection()
    if selected_contact_index:
        contacts.pop(selected_contact_index[0])
        update_contact_list()
    else:
        messagebox.showwarning("Warning", "Please select a contact to remove.")

# ===== GUI Layout =====
# Main Frame
main_frame = tk.Frame(root, bg="#f5f5f5")
main_frame.pack(pady=10, fill="both", expand=True)

# Reminders Frame
reminder_frame = tk.Frame(main_frame, bg="#ffffff", padx=10, pady=10)
reminder_frame.pack(pady=10, fill="x")

tk.Label(reminder_frame, text="📅 Reminders", font=("Helvetica", 18, 'bold'), bg="#ffffff", fg="black").pack()
reminder_entry = tk.Entry(reminder_frame, width=30, font=("Helvetica", font_size), bg="#ffffff", fg="black")
reminder_entry.pack(pady=5)
reminder_entry.insert(0, "Reminder Text")

# Create a frame for time selection
time_frame = tk.Frame(reminder_frame, bg="#ffffff")
time_frame.pack(pady=5)

# Hour selection
hour_var = tk.StringVar(value="12")  # Default hour
hour_spinbox = tk.Spinbox(time_frame, from_=1, to=12, textvariable=hour_var, width=3, font=("Helvetica", font_size), bg="#ffffff", fg="black")
hour_spinbox.pack(side=tk.LEFT)

# Minute selection
minute_var = tk.StringVar(value="00")  # Default minute
minute_spinbox = tk.Spinbox(time_frame, from_=0, to=59, textvariable=minute_var, format="%02.0f", width=3, font=("Helvetica", font_size), bg="#ffffff", fg="black")
minute_spinbox.pack(side=tk.LEFT)

# Period selection (AM/PM)
period_var = tk.StringVar(value="AM")
period_option = tk.OptionMenu(time_frame, period_var, "AM", "PM")
period_option.config(font=("Helvetica", font_size), bg="#ffffff", fg="black")
period_option.pack(side=tk.LEFT)

add_reminder_button = tk.Button(reminder_frame, text="➕ Add Reminder", command=add_reminder, bg="#4caf50", fg="black", font=("Helvetica", font_size))
add_reminder_button.pack(pady=5)

remove_reminder_button = tk.Button(reminder_frame, text="❌ Remove Selected", command=remove_reminder, bg="#d32f2f", fg="black", font=("Helvetica", font_size))
remove_reminder_button.pack(pady=5)

reminder_list = tk.Listbox(reminder_frame, height=5, width=40, font=("Helvetica", font_size), bg="#ffffff", fg="black")
reminder_list.pack(pady=5)

# Timer Frame
timer_frame = tk.Frame(main_frame, bg="#ffffff", padx=10, pady=10)
timer_frame.pack(pady=10, fill="x")

tk.Label(timer_frame, text="⏳ Timer", font=("Helvetica", 18, 'bold'), bg="#ffffff", fg="black").pack()
timer_entry = tk.Entry(timer_frame, width=10, font=("Helvetica", font_size), bg="#ffffff", fg="black")
timer_entry.pack(pady=5)
timer_entry.insert(0, "25")  # Default value

start_timer_button = tk.Button(timer_frame, text="🔔 Start Timer", command=start_custom_timer, bg="#4caf50", fg="black", font=("Helvetica", font_size))
start_timer_button.pack(pady=5)

timer_label = tk.Label(timer_frame, text="25:00", font=("Helvetica", 48, 'bold'), bg="#ffffff", fg="black")
timer_label.pack(pady=10)

# Contacts Frame
contacts_frame = tk.Frame(main_frame, bg="#ffffff", padx=10, pady=10)
contacts_frame.pack(pady=10, fill="x")

tk.Label(contacts_frame, text="📞 Contacts", font=("Helvetica", 18, 'bold'), bg="#ffffff", fg="black").pack()
add_contact_button = tk.Button(contacts_frame, text="➕ Add Contact", command=add_contact, bg="#4caf50", fg="black", font=("Helvetica", font_size))
add_contact_button.pack(pady=5)

remove_contact_button = tk.Button(contacts_frame, text="❌ Remove Selected", command=remove_contact, bg="#d32f2f", fg="black", font=("Helvetica", font_size))
remove_contact_button.pack(pady=5)

contact_list = tk.Listbox(contacts_frame, height=5, width=40, font=("Helvetica", font_size), bg="#ffffff", fg="black")
contact_list.pack(pady=5)

message_contact_button = tk.Button(contacts_frame, text="💬 Send Message", command=send_message_to_contact, bg="#4caf50", fg="black", font=("Helvetica", font_size))
message_contact_button.pack(pady=5)

# Need Help Frame
need_help_frame = tk.Frame(main_frame, bg="#ffffff", padx=10, pady=10)
need_help_frame.pack(pady=10, fill="x")

tk.Label(need_help_frame, text="🆘 Need Help?", font=("Helvetica", 18, 'bold'), bg="#ffffff", fg="black").pack()
send_message_button = tk.Button(need_help_frame, text="📲 Send Message", command=send_message, bg="#4caf50", fg="black", font=("Helvetica", font_size))
send_message_button.pack(pady=5)

# Run the app
root.mainloop()
