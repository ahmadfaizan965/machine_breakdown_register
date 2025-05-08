import csv
import os


def log_to_csv(filename, data_row, header=None):
    """
    Function to log data to a CSV file.

    filename: str
        The name of the CSV file where data will be stored.
    data_row: list
        A list of values (data) to append to the CSV file.
    header: list (optional)
        A list of column names (header) to write if the file does not exist.
    """
    file_exists = os.path.isfile(filename)

    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)

        # Write header only if file does not exist
        if not file_exists and header:
            writer.writerow(header)

        writer.writerow(data_row)
