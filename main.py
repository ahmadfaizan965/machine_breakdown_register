from email import header
import csv
from prettytable import PrettyTable
from datetime import datetime, date
from non_empty_feilds import non_empty_input
from cvs_logger import log_to_csv
import artwork

table = PrettyTable()

# Define CSV file and header
csv_file = "breakdown-log.csv"
header = ["Date", "Equipment Name", "Failure Description", "Breakdown Start", "Breakdown End",
              "Total Breakdown (in Hours)"]

def main():
    # take user input for date and format it
    date_str = non_empty_input("Please Enter Entry's date (DD/MM/YYYY): >> ")
    date_obj = datetime.strptime(date_str, "%d/%m/%Y")

    # User inputs for other details

    equipment = non_empty_input("Please Enter The Equipment Name: >> ")
    failure_details = str(input("Please Enter Failure Descriptions: >> "))

    # user input for time and format it
    start_time = non_empty_input("Enter Breakdown Start time (HH:MM): >> ")
    end_time = non_empty_input("Enter Breakdown End time (HH:MM): >> ")

    time_format = "%H:%M"
    time1 = datetime.strptime(start_time, time_format)
    time2 = datetime.strptime(end_time, time_format)
    diff = time2 - time1
    hours = round((diff.total_seconds() / 3600), 2)

    table.field_names = ["Date", "Equipment Name", "Failure Description", "Breakdown Start", "Breakdown End",
                         "Total Breakdown (in Hours)", ]
    table.add_row([date_obj.date(), equipment, failure_details, time1.time(), time2.time(), hours])

    # Save to CSV
    log_to_csv(
        filename=csv_file,
        header=header,
        data_row=[date_obj.date(), equipment, failure_details, time1.time(), time2.time(), hours]
    )

    print(f"Entry Details:")
    print(table)
    print(f" \n### Your Breakdown Data saved to {csv_file} ###\n")

def clear_csv_data(filename, header):
    filename = csv_file
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
    print(f"\n### All Previous Log data cleared from {filename} ###\n")


def re_run():
    prompt = input("Want to Add More Entries ? (Y/N) >>")
    if prompt == "y" or prompt == "Y":
        main()
    elif prompt == "n" or prompt == "N":
        print("Thank You! for using this program!")
    else:
        print("Invalid Input")
        print("Program Terminated\n")



print(artwork.art)
print("*** A CLI Program Register All of Your Machine Breakdown ***\n")
main_prompt = input("\nPlease Type 'entry' for *New Entry* or 'clear' to Remove ALL Previous Entry >>")
if main_prompt == "entry":
    main()
    re_run()
elif main_prompt == "clear":
    clear_csv_data(csv_file, header)
else:
    print("Invalid Input")
    print("Program Terminated")
