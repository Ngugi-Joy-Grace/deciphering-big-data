import csv

with open('../../data/unit 2/data-text.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:
        print(row)
