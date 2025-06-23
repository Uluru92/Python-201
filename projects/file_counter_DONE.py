# Add the code for the file counter script that you wrote in the course.

import csv
import pathlib
from pathlib import Path

# Set up the folder we where we want to do the searching and counting
main_path = str(input("Please enter the folder path where you want to search: "))
main_path = pathlib.Path(main_path)
count = {"": 0, ".csv": 0, ".md": 0, ".png": 0, ".jpg":0, ".html": 0, ".py": 0, ".js": 0, ".pdf": 0, ".txt": 0}

# Count every file type inside the folder
for file in main_path.iterdir():
    if file.suffix == "":
        count[""] +=1
    elif file.suffix == ".csv":
        count[".csv"] +=1
    elif file.suffix == ".md":
            count[".md"] +=1
    elif file.suffix == ".png":
            count[".png"] +=1
    elif file.suffix == ".jpg":
            count[".jpg"] +=1
    elif file.suffix == ".html":
            count[".html"] +=1
    elif file.suffix == ".py":
            count[".py"] +=1
    elif file.suffix == ".js":
            count[".js"] +=1
    elif file.suffix == ".pdf":
            count[".pdf"] +=1
    elif file.suffix == ".txt":
            count[".txt"] +=1
print(count)

filecounts_path = Path("03_file-input-output/filecounts.csv")

with open(filecounts_path, "w") as csvfile:
    countwriter = csv.writer(csvfile)
    data = [count[""], count[".csv"], count[".md"], count[".png"], count[".jpg"], count[".html"], count[".py"], count[".js"], count[".pdf"], count[".txt"]]
    countwriter.writerow(data)

with open(filecounts_path, "r") as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=["Folder", "CSV", "MD", "PNG","JPJ","HTML","PY","JS","PDF","TXT"])
    counts = list(reader)

print(f"File counts: {counts}")
print(type(count))
print(count.__len__())