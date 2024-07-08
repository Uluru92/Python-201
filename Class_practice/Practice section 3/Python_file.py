import csv  #cvs stands for comma-separated values

with open("Python-201-main\Class practice\Practice section 3\input.txt", "a") as i:
    countwriter = csv.writer(i)
    text_= ["Saludos desde Cañas!"]
    countwriter.writerow(text_)

with open("Python-201-main\Class practice\Practice section 3\input.txt", "r") as i:
    print(i.read())
