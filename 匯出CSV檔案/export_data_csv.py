import csv
csvFile = "example.csv"
with open(csvFile, "r") as fp:
    reader = csv.reader(fp)
    for row in reader:
        print(',', join(row))
