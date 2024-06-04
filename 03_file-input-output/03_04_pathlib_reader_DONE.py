# Refactor your file counter script to use `pathlib` also for
# reading and writing to your CSV file. Make sure to handle the
# path in a way so that you can run the script from anywhere.

import csv  #cvs stands for comma-separated values
from pathlib import Path

filecounts_path = Path("Python-201-main/03_file-input-output/filecounts.csv")
count = {"": 9, ".csv": 3, ".md": 2, ".png": 11}

with open(filecounts_path, "a") as csvfile:
    countwriter = csv.writer(csvfile)
    data = [count[""], count[".csv"], count[".md"], count[".png"]]
    countwriter.writerow(data)

with open(filecounts_path, "r") as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=["Folder", "CSV", "MD", "PNG"])
    counts = list(reader)

print(counts)
print(type(count))
print(count.__len__())