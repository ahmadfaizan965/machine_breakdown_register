import tkinter as tk
from tkinter import messagebox, ttk
import csv
import os
import platform
import subprocess
from datetime import datetime

class BreakdownApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Machine Breakdown Logger")
        self.root.geometry("500x400")
        self.csv_file = "breakdown-log.csv"
        self.header = ["Date", "Equipment Name", "Failure Description", "Start Time", "End Time", "Total Hours"]

        self.init_csv()
        self.create_widgets()

    def init_csv(self):
        """Creates the CSV file if it doesn't exist."""
        if not os.path.exists(self.csv_file):
            with open(self.csv_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(self.header)

    def open_excel(self):
        """Opens the CSV file in the system's default spreadsheet app (Excel)."""
        if not os.path.exists(self.csv_file):
            messagebox.showerror("Error", "File not found!")
            return
        
        try:
            if platform.system() == "Windows":
                os.startfile(self.csv_file)
            elif platform.system() == "Darwin":  # macOS
                subprocess.call(["open", self.csv_file])
            else:  # Linux
                subprocess.call(["xdg-open", self.csv_file])
        except Exception as e:
            messagebox.showerror("Error", f"Could not open file: {e}")

    def create_widgets(self):
        # Header
        tk.Label(self.root, text="Machine Breakdown Logger", font=("Arial", 18, "bold"), pady=20).pack()
        footer_frame = tk.Frame(self.root)
        footer_frame.pack(side="bottom", fill="x", pady=10)
        tk.Label(footer_frame, text="Developed & Maintain by: https://github.com/ahmadfaizan965", font=("Arial", 9), fg="#555555").pack()
        # Input Area
        input_frame = tk.Frame(self.root)
        input_frame.pack(padx=30, fill="x")

        self.entries = {}
        fields = [
            ("Date (DD/MM/YYYY):", "date"),
            ("Equipment Name:", "equip"),
            ("Failure Description:", "desc"),
            ("Start Time (HH:MM):", "start"),
            ("End Time (HH:MM):", "end")
        ]

        for label_text, key in fields:
            row = tk.Frame(input_frame)
            row.pack(fill="x", pady=5)
            tk.Label(row, text=label_text, width=20, anchor="w").pack(side="left")
            ent = tk.Entry(row)
            ent.pack(side="right", expand=True, fill="x")
            self.entries[key] = ent

        # Set default date
        self.entries["date"].insert(0, datetime.now().strftime("%d/%m/%Y"))

        # Main Button Row
        btn_row = tk.Frame(self.root)
        btn_row.pack(pady=30)

        # Action Buttons
        tk.Button(btn_row, text=" + Add Entry", command=self.submit_data, bg="#27ae60", fg="white", width=12, font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5)
        tk.Button(btn_row, text="Open Excel", command=self.open_excel, bg="#2980b9", fg="white", width=12, font=("Arial", 10, "bold")).grid(row=0, column=1, padx=5)
        tk.Button(btn_row, text="X Clear Data", command=self.clear_csv, bg="#c0392b", fg="white", width=12, font=("Arial", 10, "bold")).grid(row=0, column=2, padx=5)

        # Secondary Links
        tk.Button(self.root, text="View History Table", command=self.view_table, relief="flat", fg="#080808", cursor="hand2").pack()

    def submit_data(self):
        try:
            data = {k: v.get() for k, v in self.entries.items()}
            
            # Validation
            if not all([data['date'], data['equip'], data['start'], data['end']]):
                messagebox.showwarning("Incomplete", "Please fill in all required fields.")
                return

            # Logic
            t1 = datetime.strptime(data['start'], "%H:%M")
            t2 = datetime.strptime(data['end'], "%H:%M")
            hours = round(((t2 - t1).total_seconds() / 3600), 2)

            with open(self.csv_file, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([data['date'], data['equip'], data['desc'], data['start'], data['end'], hours])

            messagebox.showinfo("Success", "Data logged successfully!")
            self.entries["equip"].delete(0, tk.END)
            self.entries["desc"].delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Invalid Time Format. Use HH:MM (e.g. 14:30)")

    def view_table(self):
        """Shows data in a popup window."""
        top = tk.Toplevel(self.root)
        top.title("Breakdown History")
        top.geometry("600x400")
        
        tree = ttk.Treeview(top, columns=self.header, show='headings')
        for col in self.header:
            tree.heading(col, text=col)
            tree.column(col, width=90)
        
        if os.path.exists(self.csv_file):
            with open(self.csv_file, "r") as f:
                reader = csv.reader(f)
                next(reader) # Skip header
                for row in reader:
                    tree.insert("", "end", values=row)
        
        tree.pack(expand=True, fill="both")

    def clear_csv(self):
        if messagebox.askyesno("Confirm", "Delete all logged records permanently?"):
            with open(self.csv_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(self.header)
            messagebox.showinfo("Cleared", "All data removed.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BreakdownApp(root)
    root.mainloop()