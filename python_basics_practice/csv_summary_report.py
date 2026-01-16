import csv

def generate_summary(filename):
    total = 0
    count = 0

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += int(row['Score'])
            count += 1

    average = total / count
    print("Total Students:", count)
    print("Average Score:", round(average, 2))


generate_summary('students.csv')
