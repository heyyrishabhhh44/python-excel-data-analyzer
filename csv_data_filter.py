import csv

# Filter CSV data based on a score threshold

def filter_high_scores(filename, threshold):
    result = []

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row['Score']) >= threshold:
                result.append(row)

    return result


filtered_students = filter_high_scores('students.csv', 80)

print("Students with scores >= 80:")
for student in filtered_students:
    print(student['Name'], student['Score'])
