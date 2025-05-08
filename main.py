from prettytable import PrettyTable
from datetime import datetime, date
from non_empty_feilds import non_empty_input
from cvs_logger import log_to_csv

table = PrettyTable()


print("Welcome to Maintenance KPI Program")

date_str = non_empty_input("Enter a date (DD/MM/YYYY): ")
date_obj = datetime.strptime(date_str, "%d/%m/%Y")


equipment = non_empty_input("Please Enter The Equipment Name: ")
failure_details = str(input("Please Enter Failure Descriptions: "))

start_time  =non_empty_input("Enter Breakdown Start time (HH:MM): ")
end_time = non_empty_input("Enter Breakdown End time (HH:MM):")

time_format = "%H:%M"
time1 = datetime.strptime(start_time, time_format)
time2 = datetime.strptime(end_time, time_format)
print(time1,time2)
diff = time2 - time1
hours =round((diff.total_seconds() / 3600),2)


table.field_names = ["Date", "Equipment Name", "Failure Description", "Breakdown Start", "Breakdown End", "Total Breakdown (in Hours)",]
table.add_row([date_obj.date(), equipment, failure_details, time1.time(), time2.time(), hours])
print(table)

# Define CSV file and header
csv_file = "breakdown-log.csv"
header = ["Date", "Equipment Name", "Failure Description", "Breakdown Start", "Breakdown End","Total Breakdown (in Hours)",]

# Save to CSV
log_to_csv(
    filename=csv_file,
    header=header,
    data_row=[date_obj.date(), equipment, failure_details, time1.time(), time2.time(), hours]
)

print(f"Data saved to {csv_file}")
