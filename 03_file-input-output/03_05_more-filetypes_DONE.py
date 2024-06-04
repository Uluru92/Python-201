# Adapt your file counter script so that it records more different file types
# in your CSV file. Remember that the format of your output needs to be
# consistent across multiple runs of your script. This means you'll need to
# make a compromise and choose which file types you want to record beforehand.

import csv  #cvs stands for comma-separated values
from pathlib import Path
filecounts_path = Path("Python-201-main/03_file-input-output/filecounts.csv")
# -- snip --
count = {"": 8, ".csv": 2, ".md": 2, ".png": 11, ".jpg":7, ".html": 6, ".py": 15, ".js": 3}

with open(filecounts_path, "w") as csvfile:
    countwriter = csv.writer(csvfile)
    data = [count[""], count[".csv"], count[".md"], count[".png"], count[".jpg"], count[".html"], count[".py"], count[".js"]]
    countwriter.writerow(data)

with open(filecounts_path, "r") as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=["Folder", "CSV", "MD", "PNG","JPJ","HTML","PY","JS"])
    counts = list(reader)

print(counts)
print(type(count))
print(count.__len__())