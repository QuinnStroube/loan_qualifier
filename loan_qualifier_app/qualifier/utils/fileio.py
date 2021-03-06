# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
from pathlib import Path

def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data



# def save_csv():
#     qualifying_loans = []
#     csvpath = Path("qualifying_loans.csv")
#     with open(csvpath, 'W', newline='') as csvfile:
#         csvwriter = csv.writer(csvfile)

#         for row in csvwriter:
#             csvwriter.writerow(row.values())
# def save_csv(csvpath, data, header =None):
#     """Save csv file and implement data to file, import list of list
#     from csvpath to qualify loan"""
#     with open(csvpath, "w", newline="") as csvfile:
#         csvwriter = csv.writer(csvfile, delimiter=" ,")
#         if header:
#             csvwriter.writerow(header)
#         csvwriter.writerows(data)