import csv

with open('menu.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for i in csv_reader:
        print(i)