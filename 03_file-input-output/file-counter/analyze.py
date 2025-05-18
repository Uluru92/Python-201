# Use the `csv` module to read in and count the different file types.
import csv  #cvs stands for comma-separated values
from pathlib import Path
filecounts_path = Path("Python-201-main/03_file-input-output/file-counter/filecounts.csv")
folder_path = Path("Python-201-main/03_file-input-output/file-counter")
# -- snip --

def count_file_types(folder_path):
    folder = Path(folder_path)
    file_types = {"": 0, ".csv": 0, ".md": 0, ".png": 0, ".jpg":0, ".html": 0, ".py": 0, ".js": 0}
    
    for file in folder.iterdir():
        if file.is_file():
            ext = file.suffix.lower()
            file_types[ext] = file_types.get(ext, 0) + 1
    return file_types

def save_to_csv(file_types, output_csv):
    with open(output_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["File Type", "Count"])
        for ext, count in file_types.items():
            writer.writerow([ext, count])

folder_path = "Python-201-main/03_file-input-output/file-counter"
output_csv = "Python-201-main/03_file-input-output/file-counter/file_counts_.csv"

file_counts = count_file_types(folder_path)
save_to_csv(file_counts, output_csv)

print(f"file_counts: {file_counts}")

with open(filecounts_path, "w") as csvfile:
    countwriter = csv.writer(csvfile)
    data = [file_counts[""], file_counts[".csv"], file_counts[".md"], file_counts[".png"], file_counts[".jpg"], file_counts[".html"], file_counts[".py"], file_counts[".js"]]
    countwriter.writerow(data)

with open(filecounts_path, "r") as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=["Folder", "CSV", "MD", "PNG","JPG","HTML","PY","JS"])
    counts = list(reader)

print(reader)
print(counts)
print(counts[0]["CSV"])
print(type(counts))
print(counts.__len__())