import csv

# Open and read a CSV file
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    
    for row in reader:
        print(row)
