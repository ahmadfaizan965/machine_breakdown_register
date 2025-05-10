from prettytable import PrettyTable
from datetime import datetime, date
from non_empty_feilds import non_empty_input
from cvs_logger import log_to_csv
import artwork

table = PrettyTable()
#
# print(artwork.art)
# print("*** A CLI Program Register All of Your Machine Breakdown ***\n")
#
# def main():
#
#     # take user input for date and format it
#     date_str = non_empty_input("Please Enter Entry's date (DD/MM/YYYY): >> ")
#     date_obj = datetime.strptime(date_str, "%d/%m/%Y")
#
#     # User inputs for other details
#
#     equipment = non_empty_input("Please Enter The Equipment Name: >> ")
#     failure_details = str(input("Please Enter Failure Descriptions: >> "))
#
#     # user input for time and format it
#     start_time = non_empty_input("Enter Breakdown Start time (HH:MM): >> ")
#     end_time = non_empty_input("Enter Breakdown End time (HH:MM): >> ")
#
#     time_format = "%H:%M"
#     time1 = datetime.strptime(start_time, time_format)
#     time2 = datetime.strptime(end_time, time_format)
#     diff = time2 - time1
#     hours = round((diff.total_seconds() / 3600), 2)
#
#     table.field_names = ["Date", "Equipment Name", "Failure Description", "Breakdown Start", "Breakdown End",
#                          "Total Breakdown (in Hours)", ]
#     table.add_row([date_obj.date(), equipment, failure_details, time1.time(), time2.time(), hours])
#
#     # Define CSV file and header
#     csv_file = "breakdown-log.csv"
#     header = ["Date", "Equipment Name", "Failure Description", "Breakdown Start", "Breakdown End",
#               "Total Breakdown (in Hours)", ]
#
#     # Save to CSV
#     log_to_csv(
#         filename=csv_file,
#         header=header,
#         data_row=[date_obj.date(), equipment, failure_details, time1.time(), time2.time(), hours]
#     )
#
#     print(f"Entry Details:")
#     print(table)
#     print(f" \n### Your Breakdown Data saved to {csv_file} ###\n")
#
# def re_run():
#     prompt = input("Want to Add More Entries ? (Y/N) >>")
#     if prompt == "y" or prompt == "Y":
#         main()
#     elif prompt == "n" or prompt == "N":
#         print("Thanks for using the Program\n")
#     else:
#         print("Invalid Input")
#         print("Program Terminated\n")
#
# main()
# re_run()
import tkinter as tk
from tkinter import filedialog, messagebox
import datetime

def clear_log():
    for entry in entries.values():
        entry.delete(0, tk.END)

def save_to_log():
    data = {label: entry.get() for label, entry in entries.items()}
    try:
        with open("log.txt", "a") as f:
            f.write(f"{datetime.datetime.now()} | {data}\n")
        messagebox.showinfo("Success", "Data saved to log.txt")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            with open(file_path, "r") as f:
                content = f.read()
            messagebox.showinfo("File Content", content)
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Create main window
root = tk.Tk()
root.title("Equipment Failure Log")
root.geometry("400x400")

# Field labels
fields = [
    "Date",
    "Equipment Name",
    "Failure Description",
    "Start Time (HH:MM)",
    "End Time (HH:MM)"
]

entries = {}

# Create input fields
for field in fields:
    label = tk.Label(root, text=field)
    label.pack(pady=2)
    entry = tk.Entry(root, width=40)
    entry.pack(pady=2)
    entries[field] = entry

# Buttons frame
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# Buttons
btn_clear = tk.Button(button_frame, text="Clear the Log", command=clear_log)
btn_clear.grid(row=0, column=0, padx=10)

btn_save = tk.Button(button_frame, text="Save to Log", command=save_to_log)
btn_save.grid(row=0, column=1, padx=10)

btn_open = tk.Button(button_frame, text="Open File", command=open_file)
btn_open.grid(row=0, column=2, padx=10)

# Run the app
root.mainloop()
