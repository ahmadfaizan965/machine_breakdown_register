from datetime import date
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("600x300")
root.title("Machine Breakdown Register | Md. Faizan Ahmad")




# Entry Date Input Feild
date_entry_label = ttk.Label(text="Date of Entry (DD/MM/YY)", padding=15, font=('calibre',10,'bold'))
date_input = ttk.Entry(root, width=30, font=('calibre',10,'normal'))


# Entry Machine Name
machine_entry_label = ttk.Label(text="Name of The Equipment", padding=15, font=('calibre',10,'bold'))
machine_input = ttk.Entry(root, width=30, font=('calibre',10,'normal'))


# Entry Failure Description
failure_entry_label = ttk.Label(text="Failure Description", padding=15, font=('calibre',10,'bold'))
failure_input = ttk.Entry(root, width=30, font=('calibre',10,'normal'))


# Entry start time
start_time_label= ttk.Label(text="Start Time (HH:MM)",padding=15, font=('calibre',10,'bold'))
start_input = ttk.Entry(root, width=30, font=('calibre',10,'normal'))


# Entry end time
end_time_label = ttk.Label(text="End Time (HH:MM)",padding=15, font=('calibre',10,'bold'))
end_input = ttk.Entry(root, width=30, font=('calibre',10,'normal'))

# label & inputs layout
date_entry_label.grid(column=0, row=0)
date_input.grid(column=1, row=0)
machine_entry_label.grid(column=0, row=1)
machine_input.grid(column=1, row=1)
failure_entry_label.grid(column=0, row=2)
failure_input.grid(column=1, row=2)
start_time_label.grid(column=0, row=3)
start_input.grid(column=1, row=3)
end_time_label.grid(column=0, row=4)
end_input.grid(column=1, row=4)


# buttons layout
clear_btn = ttk.Button(root,text = "Clear Log File").grid(column=0, row=6)
submit_btn= ttk.Button(root,text = "Submit").grid(column=1, row=6)
open_file = ttk.Button(root,text = "Open Log File ").grid(column=2, row=6)


root.mainloop()